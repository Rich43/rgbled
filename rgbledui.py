# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rgbled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiDialog(object):
    def __init__(self):
        self.gridLayout: QtWidgets.QGridLayout = None
        self.formLayout: QtWidgets.QFormLayout = None
        self.label: QtWidgets.QLabel = None
        self.redSlider: QtWidgets.QSlider = None
        self.greenSlider: QtWidgets.QSlider = None
        self.blueSlider: QtWidgets.QSlider = None
        self.redLabel: QtWidgets.QLabel = None
        self.greenLabel: QtWidgets.QLabel = None
        self.blueLabel: QtWidgets.QLabel = None
        self.brightnessLabel: QtWidgets.QLabel = None
        self.brightnessSlider: QtWidgets.QSlider = None

    def setup_ui(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.resize(500, 130)
        dialog.setMinimumSize(QtCore.QSize(500, 130))
        dialog.setMaximumSize(QtCore.QSize(500, 130))
        dialog.setBaseSize(QtCore.QSize(500, 130))
        dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0)")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.label)
        self.redSlider = QtWidgets.QSlider(dialog)
        self.redSlider.setMaximum(255)
        self.redSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.redSlider.setObjectName("redSlider")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                  self.redSlider)
        self.greenLabel = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.greenLabel.setFont(font)
        self.greenLabel.setStyleSheet("color: rgb(0, 255, 0)")
        self.greenLabel.setObjectName("greenLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.greenLabel)
        self.greenSlider = QtWidgets.QSlider(dialog)
        self.greenSlider.setMaximum(255)
        self.greenSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenSlider.setObjectName("greenSlider")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                  self.greenSlider)
        self.blueLabel = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.blueLabel.setFont(font)
        self.blueLabel.setStyleSheet("color: rgb(0, 0, 255)")
        self.blueLabel.setObjectName("blueLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.blueLabel)
        self.blueSlider = QtWidgets.QSlider(dialog)
        self.blueSlider.setMaximum(255)
        self.blueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueSlider.setObjectName("blueSlider")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.blueSlider)
        self.brightnessLabel = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.brightnessLabel.setFont(font)
        self.brightnessLabel.setObjectName("brightnessLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.brightnessLabel)
        self.brightnessSlider = QtWidgets.QSlider(dialog)
        self.brightnessSlider.setMaximum(255)
        self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                  self.brightnessSlider)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslate_ui(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslate_ui(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configure RGB LED"))
        self.label.setText(_translate("Dialog", "Red"))
        self.greenLabel.setText(_translate("Dialog", "Green"))
        self.blueLabel.setText(_translate("Dialog", "Blue"))
        self.brightnessLabel.setText(_translate("Dialog", "Brightness"))
