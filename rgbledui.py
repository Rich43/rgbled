# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rgbled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiDialog(object):
    def __init__(self):
        self.grid_layout: QtWidgets.QGridLayout = None
        self.form_layout: QtWidgets.QFormLayout = None
        self.red_label: QtWidgets.QLabel = None
        self.red_slider: QtWidgets.QSlider = None
        self.green_slider: QtWidgets.QSlider = None
        self.blue_slider: QtWidgets.QSlider = None
        self.red_label: QtWidgets.QLabel = None
        self.green_label: QtWidgets.QLabel = None
        self.blue_label: QtWidgets.QLabel = None
        self.brightness_label: QtWidgets.QLabel = None
        self.brightness_slider: QtWidgets.QSlider = None
        self.on_off_label: QtWidgets.QLabel = None
        self.on_off_checkbox: QtWidgets.QCheckBox = None

    def setup_ui(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.resize(500, 160)
        dialog.setMinimumSize(QtCore.QSize(500, 160))
        dialog.setMaximumSize(QtCore.QSize(500, 160))
        dialog.setBaseSize(QtCore.QSize(500, 160))
        dialog.setModal(False)

        self.grid_layout = QtWidgets.QGridLayout(dialog)
        self.grid_layout.setObjectName("gridLayout")
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.setObjectName("formLayout")

        self.on_off_label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.on_off_label.setFont(font)
        self.on_off_label.setObjectName("onoffLabel")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                   self.on_off_label)
        self.on_off_checkbox = QtWidgets.QCheckBox(dialog)
        self.on_off_checkbox.setObjectName("onoffCheckbox")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                   self.on_off_checkbox)

        self.red_label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.red_label.setFont(font)
        self.red_label.setStyleSheet("color: rgb(255, 0, 0)")
        self.red_label.setObjectName("redLabel")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                   self.red_label)
        self.red_slider = QtWidgets.QSlider(dialog)
        self.red_slider.setMaximum(255)
        self.red_slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.red_slider.setObjectName("redSlider")

        self.form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                   self.red_slider)
        self.green_label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.green_label.setFont(font)
        self.green_label.setStyleSheet("color: rgb(0, 255, 0)")
        self.green_label.setObjectName("greenLabel")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                   self.green_label)
        self.green_slider = QtWidgets.QSlider(dialog)
        self.green_slider.setMaximum(255)
        self.green_slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_slider.setObjectName("greenSlider")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                   self.green_slider)
        self.blue_label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.blue_label.setFont(font)
        self.blue_label.setStyleSheet("color: rgb(0, 0, 255)")
        self.blue_label.setObjectName("blueLabel")
        self.form_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                   self.blue_label)
        self.blue_slider = QtWidgets.QSlider(dialog)
        self.blue_slider.setMaximum(255)
        self.blue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.blue_slider.setObjectName("blueSlider")
        self.form_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                   self.blue_slider)
        self.brightness_label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.brightness_label.setFont(font)
        self.brightness_label.setObjectName("brightnessLabel")
        self.form_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole,
                                   self.brightness_label)
        self.brightness_slider = QtWidgets.QSlider(dialog)
        self.brightness_slider.setMaximum(255)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setObjectName("brightnessSlider")
        self.form_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                   self.brightness_slider)
        self.grid_layout.addLayout(self.form_layout, 0, 0, 1, 1)

        self.retranslate_ui(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslate_ui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Configure RGB LED"))
        self.red_label.setText(_translate("Dialog", "Red"))
        self.green_label.setText(_translate("Dialog", "Green"))
        self.blue_label.setText(_translate("Dialog", "Blue"))
        self.brightness_label.setText(_translate("Dialog", "Brightness"))
        self.on_off_label.setText(_translate("Dialog", "On/Off"))
