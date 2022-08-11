from PyQt5 import uic, QtWidgets

def lista_dados():
    dado_lido = lista.lineEdit.text()
    lista.listWidget.addItem(dado_lido)
    lista.lineEdit.setText("")

def deleta():
    lista.listWidget.clear()


    
app = QtWidgets.QApplication([])
lista=uic.loadUi("lista.ui")
lista.pushButton.clicked.connect(lista_dados)
lista.pushButton_2.clicked.connect(deleta)

lista.show()
app.exec()