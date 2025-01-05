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

#CheckInputNZero - переверяю введення натуральних чисел + 0
def CheckInputNZero(inputLineEdit, resultLabel):
     result=-1

     input_str=inputLineEdit.text()
     if input_str.isnumeric():
               result=int(input_str)
     else: 
          resultLabel.setText('будь ласка введіть числове значення')
          return -1

     return result

#**************** завдання *******************

def SetModule4(moduleWidget):
    children=moduleWidget.taskcontainer.findChildren(QWidget)
    for child in children:
            child.deleteLater()
    moduleWidget.label.setText("Тема модуля4: використання функцій")
    moduleWidget.task1Button.show()
    moduleWidget.task1Button.clicked.connect(lambda: SetTask1Module4(moduleWidget))
    moduleWidget.task2Button.show()
    moduleWidget.task2Button.clicked.connect(lambda: SetTask2Module4(moduleWidget))

def SetTask1Module4(moduleWidget):
    children=moduleWidget.taskcontainer.findChildren(QWidget)
    for child in children:
            child.deleteLater()
    newchildwidget=Task1Module4Widget()
    moduleWidget.taskcontainerLayout.addWidget(newchildwidget)
              

def SetTask2Module4(moduleWidget):
    children=moduleWidget.taskcontainer.findChildren(QWidget)
    for child in children:
            child.deleteLater()
    newchildwidget=Task2Module4Widget()
    moduleWidget.taskcontainerLayout.addWidget(newchildwidget)  
   


class Task1Module4Widget(QWidget):
    def __init__(self):
        super().__init__()

        #vertical line
        mainlayout = QVBoxLayout(self)

        titlelabel = QLabel()
        titlelabel.setText('''Обрано завдання 1.
Умова: Ввести натуральне число n. Серед чисел 1, 2, ..., n знайти всі ті, 
які можна представити у вигляді суми квадратів натуральних чисел. 
Написати функцію, що дозволяє розпізнавати повні квадрати.''')
        mainlayout.addWidget(titlelabel)

        label = QLabel()
        label.setText("ввести n")
        mainlayout.addWidget(label)

        self.inputn = QLineEdit()
        self.inputn.setInputMask("999")
        mainlayout.addWidget(self.inputn)

        doButton=QPushButton()
        doButton.setText("Розрахувати")
        doButton.clicked.connect(self.task1modul4)
        mainlayout.addWidget(doButton)

        self.resultlabel = QLabel()
        self.resultlabel.setText("Результат: ")
        mainlayout.addWidget(self.resultlabel)


        self.setLayout(mainlayout)

    def task1modul4(widget):
        try:
            n=CheckInputN(widget.inputn,widget.resultlabel)

            resultstr=widget.issquare(n)            
            squares=[]
            for i in range(1,round(n**0.5),1):
                squares.append(i*i) #створила масив квадратів натуральних чисел від 1 до n

            for length in range(2, len(squares) + 1):
                resultstr=resultstr+widget.generate_combinations(squares, [], [], 0, length,n)

            widget.resultlabel.setText(f'Результат: {resultstr}')
        except Exception as e:
            str=f"Error: {e}"
            widget.resultlabel.setText(f'Результат: {str}')
            print(str)

    def generate_combinations(widget,squares, combination, combinationIndexes, start, length, n):

        result=""
        currentSum=sum(combination)
        # зупинитися треба коли отримали комбінацію потрібної довжини
        if len(combination) == length :
            if currentSum<n:
                result=result+f"Число {currentSum} є сумою квадратів чисел: {combinationIndexes} \r\n"
            return result
        # Перевіряємо елементи починаючи з поточного індексу
        for i in range(start, len(squares)):
            # додаємо цей єлемент в комбінацію
            combination.append(squares[i])
            combinationIndexes.append(i+1)
            # для наступного елементу:
            result=result+widget.generate_combinations(squares, combination, combinationIndexes, i + 1, length,n)
            # останній елемент вже перевірили
            combination.pop()
            combinationIndexes.pop()

        return result

    def issquare(widget,n):
      result=""
      nearest=round(n**0.5)
      if nearest*nearest==n:
            result= f"До речі, {n} це повний квадрат числа {nearest} \r\n"
      else: result= ""
      return result
class Task2Module4Widget(QWidget):
    def __init__(self):
        super().__init__()

        #vertical line
        mainlayout = QVBoxLayout(self)

        titlelabel = QLabel()
        titlelabel.setText('''Обрано завдання 2.
Умова:  Функція - Overlay(s,s1,n). Призначення - перекриття частини рядка s, починаючи з позиції n, рядком s1''')
        mainlayout.addWidget(titlelabel)

        label2 = QLabel()
        label2.setText("введіть першу строку")
        mainlayout.addWidget(label2)

        self.inputstr1 = QLineEdit()
        mainlayout.addWidget(self.inputstr1)

        label3 = QLabel()
        label3.setText("введіть другу строку")
        mainlayout.addWidget(label3)

        self.inputstr2 = QLineEdit()
        mainlayout.addWidget(self.inputstr2)

        label = QLabel()
        label.setText("введіть місце вставки")
        mainlayout.addWidget(label)

        self.inputn = QLineEdit()
        self.inputn.setInputMask("999")
        mainlayout.addWidget(self.inputn)

        doButton=QPushButton()
        doButton.setText("Розрахувати")
        doButton.clicked.connect(self.task2modul4)
        mainlayout.addWidget(doButton)

        self.resultlabel = QLabel()
        self.resultlabel.setText("Результат: ")
        mainlayout.addWidget(self.resultlabel)


        self.setLayout(mainlayout)

    def task2modul4(widget):
        try:
            n=CheckInputNZero(widget.inputn,widget.resultlabel)
            str1=widget.inputstr1.text()
            str2=widget.inputstr2.text()
            if n!=-1:
                result=widget.Overlay(str1,str2,n)
                widget.resultlabel.setText(f"Результат: результат перекриття буде такий {result}")
        except Exception as e:
            str=f"Error: {e}"
            widget.resultlabel.setText(f'Результат: {str}')
            print(str)

    def Overlay(widget,str1,str2,n):
        result=""

        result+=str1[0:n] #для пайтону не буде помилкую якщо випадково n більше довжини строки1
        result+=str2
        result+=str1[n+len(str2):]
        result=result[0:len(str1)] #якщо ми випадково подовжили строку 1 зайвими символами

        return result