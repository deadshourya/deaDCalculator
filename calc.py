import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from math import sqrt,sin,cos,tan,log,log10
#from math import sin
#from math import cos
#from math import tan
#from math import log
#from math import log10


 
num = 0.0
newNum = 0.0
sumA = 0.0
operator = ""
 
tf = False
sumIt = 0
 

class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        self.line = QtGui.QLineEdit(self)
        self.line.move(5,5)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.resize(200,25)
 
        zero = QtGui.QPushButton("0",self)
        zero.move(50,180)
        zero.resize(35,30)
 
        one = QtGui.QPushButton("1",self)
        one.move(10,145)
        one.resize(35,30)
 
        two = QtGui.QPushButton("2",self)
        two.move(50,145)
        two.resize(35,30)
 
        three = QtGui.QPushButton("3",self)
        three.move(90,145)
        three.resize(35,30)
 
        four = QtGui.QPushButton("4",self)
        four.move(10,110)
        four.resize(35,30)
 
        five = QtGui.QPushButton("5",self)
        five.move(50,110)
        five.resize(35,30)
 
        six = QtGui.QPushButton("6",self)
        six.move(90,110)
        six.resize(35,30)
 
        seven = QtGui.QPushButton("7",self)
        seven.move(10,75)
        seven.resize(35,30)
 
        eight = QtGui.QPushButton("8",self)
        eight.move(50,75)
        eight.resize(35,30)
 
        nine = QtGui.QPushButton("9",self)
        nine.move(90,75)
        nine.resize(35,30)
 
        switch = QtGui.QPushButton("+/-",self)
        switch.move(10,180)
        switch.resize(35,30)
        switch.clicked.connect(self.Switch)
 
        point = QtGui.QPushButton(".",self)
        point.move(90,180)
        point.resize(35,30)
        point.clicked.connect(self.pointClicked)
 
        div = QtGui.QPushButton("/",self)
        div.move(130,75)
        div.resize(35,30)
 
        mult = QtGui.QPushButton("*",self)
        mult.move(130,110)
        mult.resize(35,30)
 
        minus = QtGui.QPushButton("-",self)
        minus.move(130,145)
        minus.resize(35,30)
 
        plus = QtGui.QPushButton("+",self)
        plus.move(130,180)
        plus.resize(35,30)
 
        sqrt = QtGui.QPushButton("sqrt",self)
        sqrt.move(170,75)
        sqrt.resize(35,30)
        sqrt.clicked.connect(self.Sqrt)
 
        squared = QtGui.QPushButton("sqr",self)
        squared.move(170,110)
        squared.resize(35,30)
        squared.clicked.connect(self.Squared)

        sins = QtGui.QPushButton("sin",self)
        sins.move(10,40)
        sins.resize(35,30)
        sins.clicked.connect(self.Sins)
       
        coss = QtGui.QPushButton("cos",self)
        coss.move(50,40)
        coss.resize(35,30)
        coss.clicked.connect(self.Coss)

        tans = QtGui.QPushButton("tan",self)
        tans.move(90,40)
        tans.resize(35,30)
        tans.clicked.connect(self.Tans)

        lns = QtGui.QPushButton("ln",self)
        lns.move(130,40)
        lns.resize(35,30)
        lns.clicked.connect(self.Lns)

        logs = QtGui.QPushButton("log",self)
        logs.move(170,40)
        logs.resize(35,30)
        logs.clicked.connect(self.Logs)

        about = QtGui.QPushButton("deaDCalculator",self)
        about.move(0,250)
        about.resize(220,20)
        about.setStyleSheet("color:red;background-color:black;")
        about.clicked.connect(self.About)
 
        equal = QtGui.QPushButton("=",self)
        equal.move(170,145)
        equal.resize(35,65)
        equal.clicked.connect(self.Equal)
 
        c = QtGui.QPushButton("C",self)
        c.move(145,215)
        c.resize(60,30)
        c.clicked.connect(self.C)
 
        ce = QtGui.QPushButton("CE",self)
        ce.move(77,215)
        ce.resize(60,30)
        ce.clicked.connect(self.CE)
 
        back = QtGui.QPushButton("Back",self)
        back.move(10,215)
        back.resize(60,30)
        back.clicked.connect(self.Back)
 
        nums = [zero,one,two,three,four,five,six,seven,eight,nine]
 
        ops = [back,c,ce,div,mult,minus,plus,equal]
 
        rest = [switch,squared,sqrt,point,logs,lns,sins,coss,tans]
 
        for i in nums:
            i.setStyleSheet("color:blue;")
            i.clicked.connect(self.Nums)
 
        for i in ops:
            i.setStyleSheet("color:yellow;background-color:blue;")
 
        for i in ops[3:7]:
            i.clicked.connect(self.Operator)
        for i in rest:
	    i.setStyleSheet("color:green;") 
             
         
        self.setGeometry(300,300,215,265)
        self.setFixedSize(215,265)
        self.setWindowTitle("deaDCalculator")
        self.setWindowIcon(QtGui.QIcon("ca.jpg"))
        self.show()
 
    def Nums(self):
        global num
        global newNum
        global tf
         
        sender = self.sender()
         
        newNum = int(sender.text())
        setNum = str(newNum)
 
 
        if tf == False:
            self.line.setText(self.line.text() + setNum)
 
 
        else:
            self.line.setText(setNum)
            tf = False
             
         
 
    def pointClicked(self):
        global tf
         
        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")
             
 
    def Switch(self):
        global num
     
        num = float(self.line.text())
      
        num = num - num * 2
 
        numStr = str(num)
         
        self.line.setText(numStr)
 
    def Operator(self):
        global num
        global tf
        global operator
        global sumIt
 
        sumIt += 1
 
        if sumIt > 1:
            self.Equal()
 
        num = self.line.text()
 
        sender = self.sender()
 
        operator = sender.text()
         
        tf = True
 
 
 
    def Equal(self):
        global num
        global newNum
        global sumA
        global operator
        global tf
        global sumIt
        flg = 0 
        sumIt = 0
 
        newNum = self.line.text()
 
        print(num)
        print(newNum)
        print(operator)
         
        if operator == "+":
            sumA = float(num) + float(newNum)
 
        elif operator == "-":
            sumA = float(num) - float(newNum)
 
        elif operator == "/":
            if newNum == "0":
		flg = 3
	    else: 
                sumA = float(num) / float(newNum)
 
        elif operator == "*":
            sumA = float(num) * float(newNum)
        if flg == 3:     
          self.line.setText("error")
          tf = True
        else:
          print(sumA)
          self.line.setText(str(sumA))
          tf = True 
 
    def Back(self):
        self.line.backspace()
 
    def C(self):
        global newNum
        global sumA
        global operator
        global num
         
        self.line.clear()
 
        num = 0.0
        newNum = 0.0
        sumA = 0.0
        operator = ""
 
    def CE(self):
        self.line.clear()
 
    def Sqrt(self):
        global num
         
        num = float(self.line.text())
        n = sqrt(num)
        num = n
 
        self.line.setText(str(num))
 
    def Squared(self):
        global num  
        num = float(self.line.text())
 
        n = num ** 2
 
        num = n
 
        self.line.setText(str(n))

    def Coss(self):
        global num
         
        num = float(self.line.text())

        n = cos(num)
        num = n
 
        self.line.setText(str(num)) 

    def Sins(self):
        global num
         
        num = float(self.line.text())
        n = sin(num)
        num = n
 
        self.line.setText(str(num)) 

    def Tans(self):
        global num
         
        num = float(self.line.text())
        n = tan(num)
        num = n
 
        self.line.setText(str(num)) 

    def Lns(self):
        global num
         
        num = float(self.line.text())
        n = log(num)
        num = n
 
        self.line.setText(str(num)) 

    def Logs(self):
        global num
         
        num = float(self.line.text())
        n = log10(num)
        num = n
 
        self.line.setText(str(num)) 

    def About(self):
        self.line.clear()
        self.line.setText("made by Shourya Shashank")

  
 
def main():
    app = QtGui.QApplication(sys.argv)
    main= Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
