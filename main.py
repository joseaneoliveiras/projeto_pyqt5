import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"
        
        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(25,20)
        self.caixa_texto.resize(220,30)
        
        botao1 = QPushButton('Botão 1', self)
        botao1.move(150, 200)
        botao1.resize(150, 80)
        botao1.setStyleSheet('QPushButton {background-color: #FF1328;font:bold;font-size:20px}')
        botao1.clicked.connect(self.botao1_click)
        
        botao_caixa = QPushButton('Enviar texto', self)         # caixa de texto
        botao_caixa.move(550, 200)
        botao_caixa.resize(150, 80)
        botao_caixa.setStyleSheet('QPushButton {background-color: #FF1328;font:bold;font-size:20px}')
        botao_caixa.clicked.connect(self.mostra_texto)
        
        botao2 = QPushButton('Botão 2', self)
        botao2.move(350, 200)
        botao2.resize(150, 80)
        botao2.setStyleSheet('QPushButton {background-color: #0F13FF;font:bold;font-size:20px}')
        botao2.clicked.connect(self.botao2_click)
        
        self.label1 = QLabel(self)
        self.label1.setText("Aperte algum botão")
        self.label1.move(50,100)
        self.label1.setStyleSheet('QLabel {font-size:20px;font:bold}')
        self.label1.resize(260, 50)
        
        self.label_caixa = QLabel(self)
        self.label_caixa.setText("Digitou: ")
        self.label_caixa.move(450,100)
        self.label_caixa.setStyleSheet('QLabel {font-size:20px;font:bold}')
        self.label_caixa.resize(260, 50)
       
        self.carro = QLabel(self)
        self.carro.move(50,400)
        self.carro.setPixmap(QtGui.QPixmap('c1.png'))
        self.carro.resize(400,200)

        self.carregarJanela()
        
    def carregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def botao1_click(self):
        self.label1.setText('Carro 1 seleciondo')
        self.label1.setStyleSheet('QLabel {font-size:20px;color:"red"}')
        self.carro.setPixmap(QtGui.QPixmap('c1.png'))
        
    def mostra_texto(self):
        conteudo = self.caixa_texto.text()
        self.label_caixa.setText("Digitou: " + conteudo)
       
        
    def botao2_click(self):
        self.label1.setText('Carro 2 selecionado')
        self.label1.setStyleSheet('QLabel {font-size:20px;color:"blue"}')
        self.carro.setPixmap(QtGui.QPixmap('c2.png'))
aplicacao = QApplication(sys.argv)
j= Janela()
sys.exit(aplicacao.exec_())