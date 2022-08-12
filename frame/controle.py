from PyQt5 import uic, QtWidgets

def frame1():
  janela.frame_2.close()

def frame2():
  janela.frame_2.show()

app = QtWidgets.QApplication([])
janela=uic.loadUi("frame.ui")

janela.pushButton_2.clicked.connect(frame1)
janela.pushButton_3.clicked.connect(frame2)
janela.show()
app.exec()