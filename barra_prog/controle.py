from PyQt5 import uic, QtWidgets

valor = 0

def incrementar_valor():
    global valor
    valor = valor+10
    prim_tela.progressBar.setValue(valor)

def zerar_valor():
    global valor
    valor = 0
    prim_tela.progressBar.setValue(valor)

    
app = QtWidgets.QApplication([])
prim_tela=uic.loadUi("barra.ui")

prim_tela.pushButton.clicked.connect(incrementar_valor)
prim_tela.pushButton_2.clicked.connect(zerar_valor)

prim_tela.show()
app.exec()