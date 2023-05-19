# pip install pyside6

# Estudo de PySide -> principais componentes QtCore, QtGui e QtWidgets.

from PySide6.QtCore import Qt  # serve para fazer o alinhamento
from PySide6.QtGui import QFont
from PySide6.QtWidgets import ( 
    QApplication, QLabel, QPushButton, QWidget, QGridLayout
) # QGridLayout serve para posicionar em grid  https://doc.qt.io/qt-6/layout.html

app = QApplication()
base = QWidget() # Widget base para inserir os outros dentro
layout = QGridLayout()

# Style
font = QFont()
font.setPixelSize(20)
font.setBold(1)

label = QLabel("Mesa de Efeitos Sonoros")
label.setFont(font)
label.setAlignment(Qt.AlignCenter)

botao = QPushButton("clique")

# Adicionando os Widgets ao layout (no caso no grid)
layout.addWidget(label)
layout.addWidget(botao)

base.setLayout(layout)
base.show()
app.exec()