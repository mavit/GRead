# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/twidi/Projets/gread/ui/itemlist.ui'
#
# Created: Thu Aug 12 09:12:56 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_winItemList(object):
    def setupUi(self, winItemList):
        winItemList.setObjectName("winItemList")
        winItemList.resize(800, 480)
        self.centralWidget = QtGui.QWidget(winItemList)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listItemList = QtGui.QListView(self.centralWidget)
        self.listItemList.setObjectName("listItemList")
        self.verticalLayout.addWidget(self.listItemList)
        winItemList.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(winItemList)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menuBar.setObjectName("menuBar")
        winItemList.setMenuBar(self.menuBar)

        self.retranslateUi(winItemList)
        QtCore.QMetaObject.connectSlotsByName(winItemList)

    def retranslateUi(self, winItemList):
        winItemList.setWindowTitle(QtGui.QApplication.translate("winItemList", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    winItemList = QtGui.QMainWindow()
    ui = Ui_winItemList()
    ui.setupUi(winItemList)
    winItemList.show()
    sys.exit(app.exec_())
