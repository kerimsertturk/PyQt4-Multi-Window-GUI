## PyQt4 GUI with Multiple Windows and Home Page
---

#### Intro
Graphical User Interfaces (GUI) utilize visual tools to allow users to more easily interact with computers and achieve tasks.
Most mobile and desktop applications are, in essence, GUIs.
An important element of these apps is that there are many windows that the user can switch between. The simplest
form of window switching is beetween a Home Page, which is the first window that pops up when you run the program,
and multiple other pages. You want to be able to go to a page and go back to the main page without having to restart. 

#### Setup
PyQt is a popular python binding for Qt's gui functions. More information on it can be found [here.](https://riverbankcomputing.com/software/pyqt/intro)
The easiest way to install the package is to download the [wheel file](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4) that works for your system
and `pip install` it. I developed this module on a 32 bit machine with Python 2 so after going into the directory where my python.exe
and the pyqt4 wheel file are located, I ran `pip install PyQt4‑4.11.4‑cp27‑cp27m‑win32.whl`.

---

#### Code Breakdown
Some of the important code pieces are explained for better understanding.


Import the packages first
```python
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
```
Create the main window. This will be the "Home Page"
```python
class MainWindow(QtGui.QMainWindow):
```
Signals can be used for many purposes. In our case they will allow switching from main window to pages
and the other way around. It will be more clear when these are used later. 
For more information on signal and slot connection you can refer to the [Riverbank document](https://www.riverbankcomputing.com/static/Docs/PyQt4/new_style_signals_slots.html)
For now you can see it as a means of communication. There are 3 pages in this gui so creating 3 signals.
```python
window_signal1 = QtCore.pyqtSignal(str)
window_signal2 = QtCore.pyqtSignal(str)
window_signal3 = QtCore.pyqtSignal(str)
```
Initialize the main attributes of the window like title and size. On my computer the geometry
values below worked well but the output depends on the screen resolution and dimensions
so feel free to change the values. The first two control where the gui pops up on your screen 
and the other two are the size. 
```python
def __init__(self):
    super(MainWindow,self).__init__()
    self.setWindowTitle("Multi Page Gui test")
    self.setGeometry(120,120,400,260)
```
Labels below are used as identifiers. They don't need to be labels. 
Any PyQt object can be used. The point is to create something, anything that can be emitted to be able 
to navigate to the right page. So basically it's used as a message saying "go to this page". 

Once these are emitted the names like "go_to_page1" etc. won't matter. The only thing that will matter
to the Controller is that something is emitted to the signal. I named them descriptively
so that they help with understanding.

```python
self.page1_pointer = QtGui.QLabel("go_to_page1",self)
self.page1_pointer.hide()

self.page2_pointer = QtGui.QLabel("go_to_page2",self)
self.page2_pointer.hide()

self.page3_pointer = QtGui.QLabel("go_to_page3",self)
self.page3_pointer.hide()
```
Creating buttons for pages.
```python
self.btn1=QtGui.QPushButton("Page1", self)
self.btn1.clicked.connect(self.page1)
self.btn1.move(40,150)
```
Once the button is pushed, we will emit the pointer labels to the signals to 
indicate which page to go to. For instance, if Page1 button is pressed, we will emit "page1_pointer" 
to "window_signal1". Later the Controller will pickup that something was emitted to 
the singal, and will show the right page.

```python
def page1(self):
    self.window_signal1.emit(self.page1_pointer.text())
```
At this point the home page  will look similar to the one below

![alt text](base_home.jpg "Home Page")

Now we will create the first page. We have to also create `window_signal1` again because 
each page is a different class from the Main Window hence the signals are local objects. 
```python
class WindowOne(QtGui.QWidget):
  
    window_signal1 = QtCore.pyqtSignal(str)
```
Similar to before we are using a label to indicate that we want to go to a Page.
In this case we are already in Page 1 so they only place we can go is back to Home Page
```pyton
    self.backfrom1_pointer = QtGui.QLabel("go_back_from_one",self)
    self.backfrom1_pointer.hide()
```
Create the button to go to home page
```python
    self.homebtn=QtGui.QPushButton("Home Page", self)
    self.homebtn.move(25,20)
    self.homebtn.resize(self.homebtn.minimumSizeHint())
    self.homebtn.clicked.connect(self.home)
```
When button is clicked, call the method below. This does something very similar to page1 method 
in Main Window, but it's used to go back from Page 1 to Home Page.
```python
def home(self):
    self.window_signal1.emit(self.backfrom1_pointer.text())
```
This is how Page 1 will more or less look like

![alt text](base_one.jpg "Page 1")


The Controller will pick up signals and control the switching between the pages and the home page. 
```python
class Controller:
    
    def __init__(self):
        pass
```
If in the MainWindow a label is emitted to a signal corresponding to the page we want to go to,
call the necessary method to show the page that was intended.

For example, if "page1_pointer" is emitted to "window_signal1" , then call the "show_window_one" method
which will show Page 1. The same logic is used for all pages. So in **signal-slot** terms
we are connecting "window_signal1" signal to "show_window_one" slot.
```python
def show_main(self):
        self.window_home=MainWindow()
        self.window_home.window_signal1.connect(self.show_window_one)
        self.window_home.window_signal2.connect(self.show_window_two)
        self.window_home.window_signal3.connect(self.show_window_three)
        self.window_home.show()
```

The `show_window` methods close the main window (Home Page) and show the page window. When the user pushes the "Home Page" button, thus 
emitting the pointer to the locally defined window signal, call the corresponding method that will close the current Page and show back the Home Page.

We are practically creating the illusion that we are going back a page while in fact we are just closing and showing windows
```python    
def show_window_one(self, text):
    self.window_home.close()
    self.window_one = WindowOne(text)
    self.window_one.window_signal1.connect(self.home_page_from_one)
    self.window_one.show()
```

To go back to the Home Page, close the page currently at and call the show_main method
which shows the main window and you are back to the beginning. 
```python
def home_page_from_one(self):
    self.window_one.close()
    self.show_main()
```

The main function is usually standard with all GUIs. Ours will be slightly different as we will call
the `show_main()` method in the Controller class so that the program always starts in the main window (Home Page).
```python
def main():
    app = QtGui.QApplication(sys.argv)
    controller=Controller()
    controller.show_main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```