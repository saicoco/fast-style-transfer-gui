# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1145, 650)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 60, 541, 401))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.style_label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.style_label.setText(_fromUtf8(""))
        self.style_label.setObjectName(_fromUtf8("style_label"))
        self.horizontalLayout.addWidget(self.style_label)
        self.formLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(1010, 60, 101, 92))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(11)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.youhua = QtGui.QPushButton(self.formLayoutWidget_2)
        self.youhua.setObjectName(_fromUtf8("youhua"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.youhua)
        self.shanshui = QtGui.QPushButton(self.formLayoutWidget_2)
        self.shanshui.setObjectName(_fromUtf8("shanshui"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.shanshui)
        self.shuimohua = QtGui.QPushButton(self.formLayoutWidget_2)
        self.shuimohua.setObjectName(_fromUtf8("shuimohua"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.SpanningRole, self.shuimohua)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 60, 281, 401))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.content_label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.content_label.setText(_fromUtf8(""))
        self.content_label.setObjectName(_fromUtf8("content_label"))
        self.horizontalLayout_2.addWidget(self.content_label)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(160, 30, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(640, 30, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.styleButton = QtGui.QPushButton(self.centralWidget)
        self.styleButton.setGeometry(QtCore.QRect(120, 480, 136, 25))
        self.styleButton.setObjectName(_fromUtf8("styleButton"))
        self.contentButton = QtGui.QPushButton(self.centralWidget)
        self.contentButton.setGeometry(QtCore.QRect(640, 480, 111, 25))
        self.contentButton.setObjectName(_fromUtf8("contentButton"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen_file = QtGui.QAction(MainWindow)
        self.actionOpen_file.setObjectName(_fromUtf8("actionOpen_file"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.mainToolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.youhua, QtCore.SIGNAL(_fromUtf8("clicked()")), self.youhua.click)
        QtCore.QObject.connect(self.shanshui, QtCore.SIGNAL(_fromUtf8("clicked()")), self.shanshui.click)
        QtCore.QObject.connect(self.shuimohua, QtCore.SIGNAL(_fromUtf8("clicked()")), self.shuimohua.click)
        QtCore.QObject.connect(self.styleButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.styleButton.click)
        QtCore.QObject.connect(self.contentButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.contentButton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.youhua.setText(_translate("MainWindow", "youhua", None))
        self.shanshui.setText(_translate("MainWindow", "shanshui", None))
        self.shuimohua.setText(_translate("MainWindow", "shuimohua", None))
        self.label.setText(_translate("MainWindow", "Style Image", None))
        self.label_2.setText(_translate("MainWindow", "Content Image", None))
        self.styleButton.setText(_translate("MainWindow", "open style", None))
        self.contentButton.setText(_translate("MainWindow", "open content", None))
        self.actionOpen_file.setText(_translate("MainWindow", "open file", None))
        self.actionOpen_file.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave.setText(_translate("MainWindow", "Save ", None))

