# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 577)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_param_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.search_param_label.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.search_param_label.setObjectName("search_param_label")
        self.search_param_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.search_param_box.setGeometry(QtCore.QRect(130, 50, 121, 31))
        self.search_param_box.setObjectName("search_param_box")
        self.search_param_box.addItem("")
        self.search_param_box.addItem("")
        self.search_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.search_edit.setGeometry(QtCore.QRect(130, 90, 121, 31))
        self.search_edit.setObjectName("search_edit")
        self.view_param_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.view_param_label.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.view_param_label.setObjectName("view_param_label")
        self.view_param_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.view_param_box.setGeometry(QtCore.QRect(130, 10, 121, 31))
        self.view_param_box.setObjectName("view_param_box")
        self.view_param_box.addItem("")
        self.view_param_box.addItem("")
        self.search_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(270, 90, 191, 31))
        self.search_button.setObjectName("search_button")
        self.stacked_widget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stacked_widget.setGeometry(QtCore.QRect(0, 130, 581, 391))
        self.stacked_widget.setObjectName("stacked_widget")
        self.list_page = QtWidgets.QWidget()
        self.list_page.setObjectName("list_page")
        self.book_info_list = QtWidgets.QListWidget(parent=self.list_page)
        self.book_info_list.setGeometry(QtCore.QRect(10, 10, 561, 371))
        self.book_info_list.setObjectName("book_info_list")
        self.stacked_widget.addWidget(self.list_page)
        self.table_page = QtWidgets.QWidget()
        self.table_page.setObjectName("table_page")
        self.book_info_table = QtWidgets.QTableWidget(parent=self.table_page)
        self.book_info_table.setGeometry(QtCore.QRect(0, 0, 571, 381))
        self.book_info_table.setObjectName("book_info_table")
        self.book_info_table.setColumnCount(0)
        self.book_info_table.setRowCount(0)
        self.stacked_widget.addWidget(self.table_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_param_label.setText(_translate("MainWindow", "Параметр поиска:"))
        self.search_param_box.setItemText(0, _translate("MainWindow", "Автор"))
        self.search_param_box.setItemText(1, _translate("MainWindow", "Название"))
        self.view_param_label.setText(_translate("MainWindow", "Вид отображения:"))
        self.view_param_box.setItemText(0, _translate("MainWindow", "Список"))
        self.view_param_box.setItemText(1, _translate("MainWindow", "Таблица"))
        self.search_button.setText(_translate("MainWindow", "Искать"))
