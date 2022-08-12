from PyQt5 import uic, QtWidgets

def soma():
   soma = 0
   if (janela.checkBox_2.isChecked()):
     soma += 15
     janela.checkBox_2.setChecked(False)
   if (janela.checkBox_3.isChecked()):
     soma += 10
     janela.checkBox_3.setChecked(False)
   if (janela.checkBox.isChecked()):
     soma += 20
     janela.checkBox.setChecked(False)
   if (janela.checkBox_5.isChecked()):
     soma += 32
     janela.checkBox_5.setChecked(False)
   if (janela.checkBox_4.isChecked()):
     soma += 5,50
     janela.checkBox_4.setChecked(False)
  
 


   janela.label.setText("Valor Total: " + str(soma))
    
app = QtWidgets.QApplication([])
janela=uic.loadUi("check.ui")
janela.pushButton.clicked.connect(soma)

janela.show()
app.exec()