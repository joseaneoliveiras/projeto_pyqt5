from PyQt5 import uic, QtWidgets

def chama_seg_tela():
   seg_tela.show()
   seg_tela.label.setText("abcd")



    
app = QtWidgets.QApplication([])
prim_tela=uic.loadUi("prim_tela.ui")
seg_tela=uic.loadUi("seg_tela.ui")

prim_tela.pushButton.clicked.connect(chama_seg_tela)

prim_tela.show()
app.exec()