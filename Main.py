from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(360, 640)
        main_window.setMinimumSize(QtCore.QSize(360, 640))
        main_window.setMaximumSize(QtCore.QSize(360, 640))
        main_window.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        main_window.setLayoutDirection(QtCore.Qt.LeftToRight)
        main_window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        main_window.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menubar.setObjectName("menubar")

        self.menuSaves = QtWidgets.QMenu(self.menubar)
        self.menuSaves.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuSaves.setObjectName("menuSaves")
        main_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.actionReset = QtWidgets.QAction(main_window)
        self.actionReset.setObjectName("actionNew_Save")

        self.actionSave = QtWidgets.QAction(main_window)
        self.actionSave.setObjectName("actionSave")

        self.actionLoad = QtWidgets.QAction(main_window)
        self.actionLoad.setObjectName("actionLoad")

        self.menuSaves.addAction(self.actionSave)
        self.menuSaves.addAction(self.actionLoad)
        self.menuSaves.addAction(self.actionReset)

        self.menubar.addAction(self.menuSaves.menuAction())
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        # Function Calls
        self.actionSave.triggered.connect(lambda: self.gameSave())
        self.actionLoad.triggered.connect(lambda: self.gameLoad())
        self.actionReset.triggered.connect(lambda: self.gameReset())

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Life Ireru"))
        self.menuSaves.setTitle(_translate("MainWindow", "Saves"))
        self.actionReset.setText(_translate("MainWindow", "Full Reset"))
        self.actionReset.setStatusTip(_translate("MainWindow", "Fully reset Everything"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save your Progress"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setStatusTip(_translate("MainWindow", "Load your Progress"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+L"))

    def gameSave(self):  # Program Game Save
        pass

    def gameLoad(self):  # Program Game Load
        pass

    def gameReset(self):  # Program Game Reset
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
