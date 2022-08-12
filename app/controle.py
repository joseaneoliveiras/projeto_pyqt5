from PyQt5 import uic, QtWidgets

def salvar():
  nome = janela.lineEdit.text()
  idade = janela.lineEdit_2.text()
  tel = janela.lineEdit_3.text()
  dados= "Nome: "+nome+" Idade: "+idade+" Telefone: "+tel
  
  arquivo = QtWidgets.QFileDialog.getSaveFileName()[0]

  with open (arquivo + '.txt', 'w') as a:
    a.write(dados)
def ler_arquivo():
  arquivo = QtWidgets.QFileDialog.getOpenFileName()[0]

  with open (arquivo, 'r') as a:
    janela.label_5.setText(a.read())

app = QtWidgets.QApplication([])
janela=uic.loadUi("tela.ui")

janela.actionSalva.triggered.connect(salvar)
janela.actionAbrir.triggered.connect(ler_arquivo)

janela.show()
app.exec()