import sys
import pandas as pd
from pandas_datareader import data as pdr
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import *
 
class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()
 
        self.setWindowTitle("Form")
        self.formGroupBox = QGroupBox("Stock Input")
 
        self.lineEditTicker = QLineEdit()
        self.lineEditDate = QLineEdit()
        self.lineEditCategory = QLineEdit()
       
        self.createForm()
 
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.getInfo)
 
        mainLayout=QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonBox)
 
        self.setLayout(mainLayout)
        self.displayWindow = MyWidget()
 
    def getInfo(self):
 
        stock_data = pdr.DataReader(self.lineEditTicker.text(), 'yahoo', start=self.lineEditDate.text(), end=self.lineEditDate.text())
        sdt = '${:.2f}'.format(stock_data[self.lineEditCategory.text()][0])
       
        output = QtWidgets.QLabel(str(sdt))
        self.displayWindow.text.setText(output.text())
 
        self.displayWindow.setWindowTitle(self.lineEditTicker.text() + " " +  self.lineEditCategory.text())
       
        self.displayWindow.showWindow()
       
    def createForm(self):
 
        layout = QFormLayout()
 
        layout.addRow(QLabel("Ticker Symbol: "), self.lineEditTicker)
        layout.addRow(QLabel("Date (yyyy-mm-dd): "), self.lineEditDate)
        layout.addRow(QLabel("Category"), self.lineEditCategory)
 
        self.formGroupBox.setLayout(layout)
 
 
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
 
        self.text = QLabel("", alignment=QtCore.Qt.AlignCenter)  
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
       
 
   
    def showWindow(self):
        self.resize(800, 800)
        self.show()
 
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
 
 
    form = Form()
    form.resize(900, 700)
    form.show()
 
 
    sys.exit(app.exec_())
