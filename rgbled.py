import glob
import sys
from datetime import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

from rgbledui import UiDialog

# noinspection PyPackageRequirements
from serial import Serial, SerialException
import json
import time

class SerialThread(QThread):
    write = pyqtSignal('PyQt_PyObject')
    ready_signal = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)
        self.serial: Serial = None
        self.ready = False
        self.status = ""

    def run(self):
        self.write.connect(self.handle_write)
        ports = SerialThread.serial_ports()
        print(ports)
        port = ports[0]
        print("Using port " + port)
        self.serial = Serial(port, 115200)
        assert b"READY" in self.serial.read_until()
        decoded = bytes.decode(self.serial.read_until(), "UTF-8")
        self.status = [int(x) for x in decoded.strip().split(",")]
        print(self.status)
        self.ready = True
        self.ready_signal.emit()

    def handle_write(self, data):
        if self.ready:
            self.serial.write(str.encode(json.dumps(data) + "\n"))
            time.sleep(0.1)

    @staticmethod
    def serial_ports():
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith(
                'cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = Serial(port)
                s.close()
                result.append(port)
            except (OSError, SerialException):
                pass
        return result


class App(QtWidgets.QDialog):
    def __init__(self, ser: SerialThread):
        super(App, self).__init__()

        self.ser = ser
        self.ui = UiDialog()
        self.ui.setup_ui(self)

        self.ui.brightnessSlider.valueChanged.connect(self.brightness_changed)
        self.ui.redSlider.valueChanged.connect(self.red_changed)
        self.ui.greenSlider.valueChanged.connect(self.green_changed)
        self.ui.blueSlider.valueChanged.connect(self.blue_changed)
        ser.ready_signal.connect(self.serial_ready)

    def serial_ready(self):
        self.ui.redSlider.setValue(self.ser.status[0])
        self.ui.greenSlider.setValue(self.ser.status[1])
        self.ui.blueSlider.setValue(self.ser.status[2])
        self.ui.brightnessSlider.setValue(self.ser.status[3])

    def brightness_changed(self):
        value = App.set_tooltip(self.ui.brightnessSlider)
        self.ser.write.emit({"br": value})

    def red_changed(self):
        value = App.set_tooltip(self.ui.redSlider)
        self.ser.write.emit({"r": value})

    def green_changed(self):
        value = App.set_tooltip(self.ui.greenSlider)
        self.ser.write.emit({"g": value})

    def blue_changed(self):
        value = App.set_tooltip(self.ui.blueSlider)
        self.ser.write.emit({"b": value})

    @staticmethod
    def set_tooltip(obj):
        value = obj.value()
        obj.setToolTip(str(value))
        return value


def main():
    app = QtWidgets.QApplication(sys.argv)
    serial_thread = SerialThread()
    serial_thread.start()
    application = App(serial_thread)
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
