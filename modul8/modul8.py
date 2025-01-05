from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow,QLabel,QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit
from modul2 import *
from modul4 import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Module 8")

        #vertical line
        mainlayout = QVBoxLayout()

        label = QLabel()
        label.setText('''Тема модуля 8: Графічні інтерфеси
Виконала студентка гр.КМ-42 Пошелюк Єлизавета Андрійовна
Варіант №19''')
        mainlayout.addWidget(label)

        self.modulcontainer = ModuleWidget()
        #self.modulcontainer.setFixedSize(QSize(400, 300))
        mainlayout.addWidget(self.modulcontainer)

        # -- horizintal line
        mainButtonsContainer = QWidget()
        mainbuttonslayout=QHBoxLayout()

        self.modul1Button=QPushButton()
        self.modul1Button.setText("Модуль 1")
        self.modul1Button.clicked.connect(self.modul1ButtonClicked)
        mainbuttonslayout.addWidget(self.modul1Button)

        self.modul2Button=QPushButton()
        self.modul2Button.setText("Модуль 2")
        self.modul2Button.clicked.connect(self.modul2ButtonClicked)
        mainbuttonslayout.addWidget(self.modul2Button)

        label2 = QLabel()
        label2.setText('''Обрати модуль
або закінчити''')
        mainbuttonslayout.addWidget(label2)

        self.exitButton=QPushButton()
        self.exitButton.setText("Закінчити")
        self.exitButton.clicked.connect(self.close)
        mainbuttonslayout.addWidget(self.exitButton)

        
        mainButtonsContainer.setLayout(mainbuttonslayout)
        # -- horizonal line end
        mainlayout.addWidget(mainButtonsContainer)

        maincontainer = QWidget()
        maincontainer.setLayout(mainlayout)

        self.setCentralWidget(maincontainer)

    def modul1ButtonClicked(self):
        SetModule2(self.modulcontainer)

    def modul2ButtonClicked(self):
        SetModule4(self.modulcontainer)

class ModuleWidget(QWidget):
    def __init__(self):
        super().__init__()

        #vertical line
        mainlayout = QVBoxLayout(self)

        self.label = QLabel()
        self.label.setText("Оберіть модуль")
        mainlayout.addWidget(self.label)

        self.taskcontainer = QWidget()
        self.taskcontainerLayout = QVBoxLayout(self)
        #self.taskcontainer.setFixedSize(QSize(400, 200))
        self.taskcontainer.setLayout(self.taskcontainerLayout)
        mainlayout.addWidget(self.taskcontainer)

        # -- horizintal line
        mainButtonsContainer = QWidget()
        mainbuttonslayout=QHBoxLayout(mainButtonsContainer)

        self.task1Button=QPushButton()
        self.task1Button.setText("Завдання 1")
        self.task1Button.hide()
        mainbuttonslayout.addWidget(self.task1Button)

        self.task2Button=QPushButton()
        self.task2Button.setText("Завдання 2")
        self.task2Button.hide()
        mainbuttonslayout.addWidget(self.task2Button)

        
        mainButtonsContainer.setLayout(mainbuttonslayout)
        # -- horizonal line end
        mainlayout.addWidget(mainButtonsContainer)

        self.setLayout(mainlayout)



app = QApplication([])

window = MainWindow()
window.show()  

app.exec()