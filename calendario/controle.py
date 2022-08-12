from PyQt5 import uic, QtWidgets

def pegar_data():
    data = str(janela.calendarWidget.selectedDate())
    data_formatada = data[19:30]
    janela.label.setText("Data Selecionada: "+data_formatada)

    
app = QtWidgets.QApplication([])
janela=uic.loadUi("calendario.ui")

janela.calendarWidget.selectionChanged.connect(pegar_data)
janela.show()
app.exec()