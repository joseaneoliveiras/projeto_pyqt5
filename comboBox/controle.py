from PyQt5 import uic, QtWidgets

def opcao_selecionada():
  cidade = janela.comboBox.currentText()
  janela.label_2.setText("Cidade: "+ cidade)


app = QtWidgets.QApplication([])
janela=uic.loadUi("com_box.ui")


janela.comboBox.addItems(["São Paulo", "Rio de Janeiro"])
janela.pushButton.clicked.connect(opcao_selecionada)

janela.show()
app.exec()