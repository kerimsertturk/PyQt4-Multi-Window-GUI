import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QtGui.QMainWindow):

    #Signals
    window_signal1 = QtCore.pyqtSignal(str)
    window_signal2 = QtCore.pyqtSignal(str)
    window_signal3 = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Multi Page Gui test")
        self.setGeometry(120,120,400,260)

        #Home Page Title
        self.labelTitle=QtGui.QLabel(self)
        self.titleFont=QtGui.QFont()
        self.titleFont.setBold(True)
        self.titleFont.setPointSize(15)
        self.labelTitle.setText("Home Page")
        self.labelTitle.setFont(self.titleFont)
        self.labelTitle.resize(self.labelTitle.minimumSizeHint())
        self.labelTitle.move(142,40)

        #Pointer Labels
        self.page1_pointer = QtGui.QLabel("go_to_page1",self)
        self.page1_pointer.hide()

        self.page2_pointer = QtGui.QLabel("go_to_page2",self)
        self.page2_pointer.hide()

        self.page3_pointer = QtGui.QLabel("go_to_page3",self)
        self.page3_pointer.hide()

        #Buttons for Pages
        self.btn1=QtGui.QPushButton("Page1", self)
        self.btn1.clicked.connect(self.page1)
        self.btn1.move(40,150)

        self.btn2=QtGui.QPushButton("Page2", self)
        self.btn2.clicked.connect(self.page2)
        self.btn2.move(150,150)

        self.btn3=QtGui.QPushButton("Page3", self)
        self.btn3.clicked.connect(self.page3)
        self.btn3.move(260,150)


    def page1(self):
        self.window_signal1.emit(self.page1_pointer.text())
        
    def page2(self):
        self.window_signal2.emit(self.page2_pointer.text())

    def page3(self):
        self.window_signal3.emit(self.page3_pointer.text())


#Page 1
class WindowOne(QtGui.QWidget):
    
    window_signal1 = QtCore.pyqtSignal(str)
    
    def __init__(self,text):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Page 1")
        self.setGeometry(120,120,400,260)

        self.backfrom1_pointer = QtGui.QLabel("go_back_from_one",self)
        self.backfrom1_pointer.hide()

        #Page 1 LAbel
        self.page1Label=QtGui.QLabel("Page 1",self)
        self.page1Label.move(170,130)
        self.pageLabelFont=QtGui.QFont()
        self.pageLabelFont.setPointSize(15)
        self.page1Label.setFont(self.pageLabelFont)
		
		#Button to go back to the Home Page
        self.homebtn=QtGui.QPushButton("Home Page", self)
        self.homebtn.move(25,20)
        self.homebtn.resize(self.homebtn.minimumSizeHint())
        self.homebtn.clicked.connect(self.home)

    def home(self):
        self.window_signal1.emit(self.backfrom1_pointer.text())

#Page 2
class WindowTwo(QtGui.QWidget):
    
    window_signal2 = QtCore.pyqtSignal(str)
    
    def __init__(self,text):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Page 2")
        self.setGeometry(120,120,400,260)

        self.backfrom2_pointer = QtGui.QLabel("go_back_from_two",self)
        self.backfrom2_pointer.hide()

        #Page 2 Label
        self.page2Label=QtGui.QLabel("Page 2",self)
        self.page2Label.move(170,130)
        self.pageLabelFont=QtGui.QFont()
        self.pageLabelFont.setPointSize(15)
        self.page2Label.setFont(self.pageLabelFont)

        # Button to go back to the Home Page
        self.homebtn = QtGui.QPushButton("Home Page", self)
        self.homebtn.move(25, 20)
        self.homebtn.resize(self.homebtn.minimumSizeHint())
        self.homebtn.clicked.connect(self.home)

    def home(self):
        self.window_signal2.emit(self.backfrom2_pointer.text())

#Page 3
class WindowThree(QtGui.QWidget):
    
    window_signal3 = QtCore.pyqtSignal(str)
    
    def __init__(self,text):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Page 3")
        self.setGeometry(120,120,400,260)

        self.backfrom3_pointer = QtGui.QLabel("go_back_from_three",self)
        self.backfrom3_pointer.hide()

        #Page 3 Label
        self.page3Label=QtGui.QLabel("Page 3",self)
        self.page3Label.move(170,130)
        self.pageLabelFont=QtGui.QFont()
        self.pageLabelFont.setPointSize(15)
        self.page3Label.setFont(self.pageLabelFont)

        #Button to go back to the Home Page
        self.homebtn = QtGui.QPushButton("Home Page", self)
        self.homebtn.move(25, 20)
        self.homebtn.resize(self.homebtn.minimumSizeHint())
        self.homebtn.clicked.connect(self.home)

    def home(self):
        self.window_signal3.emit(self.backfrom3_pointer.text())
		

#Controller
class Controller:
    
    def __init__(self):
        pass

    def show_main(self):
        self.window_home=MainWindow()
        self.window_home.window_signal1.connect(self.show_window_one)
        self.window_home.window_signal2.connect(self.show_window_two)
        self.window_home.window_signal3.connect(self.show_window_three)
        self.window_home.show()

    def show_window_one(self, text):
        self.window_home.close()
        self.window_one = WindowOne(text)
        self.window_one.window_signal1.connect(self.home_page_from_one)
        self.window_one.show()

    def show_window_two(self,text):
        self.window_home.close()
        self.window_two = WindowTwo(text)
        self.window_two.window_signal2.connect(self.home_page_from_two)
        self.window_two.show()

    def show_window_three(self,text):
        self.window_home.close()
        self.window_three = WindowThree(text)
        self.window_three.window_signal3.connect(self.home_page_from_three)
        self.window_three.show()

    def home_page_from_one(self):
        self.window_one.close()
        self.show_main()

    def home_page_from_two(self):
        self.window_two.close()
        self.show_main()

    def home_page_from_three(self):
        self.window_three.close()
        self.show_main()


def main():
    app = QtGui.QApplication(sys.argv)
    controller=Controller()
    controller.show_main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
