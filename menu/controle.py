from PyQt5 import uic, QtWidgets

def menu_verde():
    tela.label_2.setText("Verde")
    tela.label_2.setStyleSheet("color: green")
    
def menu_vermelho():
    tela.label_2.setText("Vermelho")
    tela.label_2.setStyleSheet("color: red")

def menu_amarelo():
    tela.label_2.setText("Amarelo")
    tela.label_2.setStyleSheet("color: yellow")
app = QtWidgets.QApplication([])
tela=uic.loadUi("menu.ui")

tela.actionVerde.triggered.connect(menu_verde)
tela.actionVermelho.triggered.connect(menu_vermelho)
tela.actionAmarelo.triggered.connect(menu_amarelo)
tela.show()
app.exec()