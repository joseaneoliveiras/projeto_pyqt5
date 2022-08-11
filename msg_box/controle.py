from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def exibir_msg():
   dado_lido = janela.lineEdit.text()
   print(dado_lido)
   janela.lineEdit.setText("")
   
   if dado_lido == "":
        QMessageBox.about(janela, "Alerta", "Nenhum nome digitado")
   else:
        QMessageBox.about(janela, "Alerta", "Olá "+dado_lido)



    
app = QtWidgets.QApplication([])
janela=uic.loadUi("caixa_msg.ui")
janela.pushButton.clicked.connect(exibir_msg)

janela.show()
app.exec()