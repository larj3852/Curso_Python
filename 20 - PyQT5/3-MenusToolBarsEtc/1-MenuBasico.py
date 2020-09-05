# menu_framework.py
# Import necessary modules
"""
QMainWindow      focuses on creating and managing the layout for the main
                window of an application. It allows you to set up a window with a status bar, a toolbar,
                dock widgets, or other menu options in predefined places all designed around functions
                that the main window should have.

QWidget          is the base class for all user interface objects in Qt. The widget
                is the basic building block of GUIs. It is interactive, allowing the user to communicate
                with the computer to perform some task. Many of the widgets you have already looked
                at, such as QPushButton and QTextEdit, are just subclasses of QWidget that give
                functionality to your programs.

QAction          defining actions for menus and toolbars.
                Many actions in an application are also given shortcut keys making it easier to perform
                that task, for example, Ctrl+V for the paste action (Cmd+V on MacOS) or Ctrl+X for the
                cut action (Cmd+X on MacOS). Take a look at how the Exit action is created and then
                added to file_menu.

"""
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction)

class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
 
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 350, 350) # x, y, width, height
        self.setWindowTitle('Basic Menu Example')
        self.createMenu()
        self.show()

    def createMenu(self):
        """
        Create skeleton application with a menubar
        """
        # Create actions for file menu
        exit_act = QAction('Exit', self)
        exit_act.setShortcut('Ctrl+T')
        exit_act.triggered.connect(self.close)
        # Create menubar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_act)

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec_())