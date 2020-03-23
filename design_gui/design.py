# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_greeting = QtWidgets.QLabel(self.centralwidget)
        self.label_greeting.setGeometry(QtCore.QRect(0, -20, 641, 98))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_greeting.sizePolicy().hasHeightForWidth())
        self.label_greeting.setSizePolicy(sizePolicy)
        self.label_greeting.setMinimumSize(QtCore.QSize(300, 98))
        self.label_greeting.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.label_greeting.setFont(font)
        self.label_greeting.setTextFormat(QtCore.Qt.AutoText)
        self.label_greeting.setWordWrap(True)
        self.label_greeting.setObjectName("label_greeting")
        self.pushButton_insert_dimencsion = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_insert_dimencsion.setGeometry(QtCore.QRect(0, 90, 91, 23))
        self.pushButton_insert_dimencsion.setObjectName("pushButton_insert_dimencsion")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 298, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_lines = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_lines.setObjectName("label_lines")
        self.horizontalLayout_6.addWidget(self.label_lines)
        self.comboBox_lines = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_lines.setObjectName("comboBox_lines")
        self.horizontalLayout_6.addWidget(self.comboBox_lines)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(320, 50, 253, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_columns = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_columns.setObjectName("label_columns")
        self.horizontalLayout_7.addWidget(self.label_columns)
        self.comboBox_columns = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_columns.setObjectName("comboBox_columns")
        self.horizontalLayout_7.addWidget(self.comboBox_columns)
        self.tableWidget_A = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_A.setGeometry(QtCore.QRect(0, 170, 900, 191))
        self.tableWidget_A.setObjectName("tableWidget_A")
        self.tableWidget_A.setColumnCount(0)
        self.tableWidget_A.setRowCount(0)
        self.label_limitations = QtWidgets.QLabel(self.centralwidget)
        self.label_limitations.setGeometry(QtCore.QRect(0, 150, 401, 16))
        self.label_limitations.setObjectName("label_limitations")
        self.label_function = QtWidgets.QLabel(self.centralwidget)
        self.label_function.setGeometry(QtCore.QRect(0, 360, 381, 16))
        self.label_function.setObjectName("label_function")
        self.tableWidget_function = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_function.setGeometry(QtCore.QRect(0, 380, 651, 51))
        self.tableWidget_function.setObjectName("tableWidget_function")
        self.tableWidget_function.setColumnCount(0)
        self.tableWidget_function.setRowCount(0)
        self.pushButton_solve_simplex = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_solve_simplex.setGeometry(QtCore.QRect(10, 540, 75, 23))
        self.pushButton_solve_simplex.setObjectName("pushButton_solve_simplex")
        self.label__limit_value = QtWidgets.QLabel(self.centralwidget)
        self.label__limit_value.setGeometry(QtCore.QRect(0, 440, 241, 16))
        self.label__limit_value.setObjectName("label__limit_value")
        self.tableWidget_limit_value = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_limit_value.setGeometry(QtCore.QRect(0, 460, 651, 71))
        self.tableWidget_limit_value.setObjectName("tableWidget_limit_value")
        self.tableWidget_limit_value.setColumnCount(0)
        self.tableWidget_limit_value.setRowCount(0)
        self.label_solve = QtWidgets.QLabel(self.centralwidget)
        self.label_solve.setGeometry(QtCore.QRect(450, 540, 151, 21))
        self.label_solve.setObjectName("label_solve")
        self.label_error_message = QtWidgets.QLabel(self.centralwidget)
        self.label_error_message.setGeometry(QtCore.QRect(10, 580, 391, 21))
        self.label_error_message.setObjectName("label_error_message")
        self.pushButton_plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plot.setGeometry(QtCore.QRect(460, 590, 121, 23))
        self.pushButton_plot.setObjectName("pushButton_plot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_greeting.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Симплексный метод решения задачи линейного программирования.</span></p></body></html>"))
        self.pushButton_insert_dimencsion.setText(_translate("MainWindow", "Ввести"))
        self.label_lines.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Выберите число строк(ограничений):</span></p></body></html>"))
        self.label_columns.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Выберите число переменных:</span></p></body></html>"))
        self.label_limitations.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Введите коэффициенты для множества ограничений:</span></p></body></html>"))
        self.label_function.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Введите коэффициенты для функции цели:</span></p></body></html>"))
        self.pushButton_solve_simplex.setText(_translate("MainWindow", "Посчитать"))
        self.label__limit_value.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Введите ограничения на неизвестные:</span></p></body></html>"))
        self.label_solve.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Решение: </span></p></body></html>"))
        self.label_error_message.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ошибка</span></p></body></html>"))
        self.pushButton_plot.setText(_translate("MainWindow", "Построить график."))