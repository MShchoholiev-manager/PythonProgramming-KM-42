from PyQt6.QtWidgets import QWidget, QLabel,QVBoxLayout,QPushButton,QLineEdit

#**************** перевірки *******************

#CheckInputN - переверяю введення натуральних чисел
def CheckInputN(inputLineEdit, resultLabel):
     result=0

     input_str=inputLineEdit.text()
     if input_str.isnumeric():
               result=int(input_str)
     else: 
          resultLabel.setText('будь ласка введіть числове значення')
          return 0

     if result==0: 
          resultLabel.setText('будь ласка введить не нульове значення')
          return 0

     return result

#CheckInputX - переверяю введення дійсних чисел і ділення на 0
def CheckInputX(inputLineEdit, resultLabel):
     result=0

     try:
          result=float(inputLineEdit.text())
     except: 
          resultLabel.setText('введить правильне дійсне число')
          return 0

     
     if result==0:
         resultLabel.setText('увага! ділення на нуль. Введить інше х')
         return 0
     return result

#**************** завдання *******************

def SetModule2(moduleWidget):
    children=moduleWidget.taskcontainer.findChildren(QWidget)
    for child in children:
            child.deleteLater()
    moduleWidget.label.setText("Тема модуля2: Програмування циклічних алгоритмів")
    moduleWidget.task1Button.show()
    moduleWidget.task1Button.clicked.connect(lambda: SetTask1Module2(moduleWidget))
    moduleWidget.task2Button.show()
    moduleWidget.task2Button.clicked.connect(lambda: SetTask2Module2(moduleWidget))

def SetTask1Module2(moduleWidget):
    children=moduleWidget.taskcontainer.findChildren(QWidget)
    for child in children:
            child.deleteLater()
    newchildwidget=Task1Module2Widget()
    moduleWidget.taskcontainerLayout.addWidget(newchildwidget)
             

def SetTask2Module2(moduleWidget):
    children=moduleWidget.taskcontainer.findChildren(QWidget)
    for child in children:
            child.deleteLater()
    newchildwidget=Task2Module2Widget()
    moduleWidget.taskcontainerLayout.addWidget(newchildwidget)  
  


class Task1Module2Widget(QWidget):
    def __init__(self):
        super().__init__()

        #vertical line
        mainlayout = QVBoxLayout(self)

        titlelabel = QLabel()
        titlelabel.setText('''Обрано завдання 1.
Умова: розрахувати суму по і від 1 до n: x^i/(x-n)''')
        mainlayout.addWidget(titlelabel)

        label = QLabel()
        label.setText("ввести n")
        mainlayout.addWidget(label)

        self.inputn = QLineEdit()
        self.inputn.setInputMask("999")
        mainlayout.addWidget(self.inputn)

        label2 = QLabel()
        label2.setText("ввести x")
        mainlayout.addWidget(label2)

        self.inputx = QLineEdit()
        self.inputx.setInputMask("9.99")
        mainlayout.addWidget(self.inputx)

        doButton=QPushButton()
        doButton.setText("Розрахувати")
        doButton.clicked.connect(self.task1modul2)
        mainlayout.addWidget(doButton)

        self.resultlabel = QLabel()
        self.resultlabel.setText("Результат: ")
        mainlayout.addWidget(self.resultlabel)


        self.setLayout(mainlayout)

    def task1modul2(widget):
        try:
            n=CheckInputN(widget.inputn,widget.resultlabel)
            x=CheckInputX(widget.inputx,widget.resultlabel)
            if n!=0 and x!=0:
                sum = 0 
                for i in range(1,n+1):
                    sum+=pow(x,i)/(x-n)
                widget.resultlabel.setText(f'Результат: сума дорівнює {sum}')
        except Exception as e:
            str=f"Error: {e}"
            widget.resultlabel.setText(f'Результат: {str}')
            print(str)

class Task2Module2Widget(QWidget):
    def __init__(self):
        super().__init__()

        #vertical line
        mainlayout = QVBoxLayout(self)

        titlelabel = QLabel()
        titlelabel.setText('''Обрано завдання 2.
Умова:  Увести ціле число N(>1). Знайти найбільше ціле число K, при якому виконується нерівність 3K<N''')
        mainlayout.addWidget(titlelabel)

        label = QLabel()
        label.setText("введить ціле число N")
        mainlayout.addWidget(label)

        self.inputn = QLineEdit()
        self.inputn.setInputMask("9999")
        mainlayout.addWidget(self.inputn)

        doButton=QPushButton()
        doButton.setText("Розрахувати")
        doButton.clicked.connect(self.task2modul2)
        mainlayout.addWidget(doButton)

        self.resultlabel = QLabel()
        self.resultlabel.setText("Результат: ")
        mainlayout.addWidget(self.resultlabel)


        self.setLayout(mainlayout)

    def task2modul2(widget):
        try:
            N=CheckInputN(widget.inputn,widget.resultlabel)
            if N!=0:
                K = 0
                while 3*K<N:
                    K+=1
                K-=1
                #зменшуємо на 1, бо останнє значення вже завелике 
                widget.resultlabel.setText(f"Результат: K дорівнює {K}")
        except Exception as e:
            str=f"Error: {e}"
            widget.resultlabel.setText(f'Результат: {str}')
            print(str)