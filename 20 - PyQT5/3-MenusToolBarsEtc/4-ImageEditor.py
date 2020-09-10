"""
QStatusBar      Sometimes an icon’s or menu item’s function is not explicitly
                understood. This widget is very useful for displaying extra information 
                to the user about the capabilities of an action.
                To create a status bar object, you can use the setStatusBar() method 
                which is part of the QMainWindow class. To create an empty status bar, 
                pass QStatusBar as an argument.

QToolBar        provides ways to create a toolbar with icons, text, or standard Qt widgets for quick access
                to frequently used commands.
                Toolbars are generally located under the menubar like in Figure 5-14, 
                but can also be placed vertically or at the bottom of the main window 
                above the status bar. Refer to the image in Figure 5-2 for an idea of 
                arranging the different widgets in the main window.

QDockWidget     is used to create detachable or floating tool palettes or widget
                panels. Dock widgets are secondary windows that provide additional 
                functionality to GUI windows.
""" 

# menu_framework2.py
# # Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QStatusBar,
QAction, QTextEdit, QToolBar, QDockWidget)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 350, 350) # x, y, width, height
        self.setWindowTitle('Basic Menu Example 2')
        # Set central widget for main window
        self.setCentralWidget(QTextEdit())
        self.createMenu()
        self.createToolBar()
        self.createDockWidget()
        self.show()

    def createMenu(self):
        """
        Create menubar and menu actions
        """
        # Create actions for file menu
        self.exit_act = QAction(QIcon('images/exit.png'), 'Exit', self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setStatusTip('Quit program')
        self.exit_act.triggered.connect(self.close)
      # Create actions for view menu
        full_screen_act = QAction('Full Screen', self, checkable=True)
        full_screen_act.setStatusTip('Switch to full screen mode')
        full_screen_act.triggered.connect(self.switchToFullScreen)
        # Create menubar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.exit_act)
        # Create view menu, Appearance submenu, and add actions
        view_menu = menu_bar.addMenu('View')
        appearance_submenu = view_menu.addMenu('Appearance')
        appearance_submenu.addAction(full_screen_act)
        # Display info about tools, menu, and view in the status bar
        self.setStatusBar(QStatusBar(self))        

    def createToolBar(self):
        """
        Create toolbar for GUI
        """
        # Set up toolbar
        tool_bar = QToolBar("Main Toolbar")
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)
        # Add actions to toolbar
        tool_bar.addAction(self.exit_act)

    def createDockWidget(self):
        """
        Create dock widget
        """
        # Set up dock widget
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Example Dock")
        dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)
        # Set main widget for the dock widget
        dock_widget.setWidget(QTextEdit())
        # Set initial location of dock widget in main window
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

    def switchToFullScreen(self, state):
        """
        If state is True, then display the main window in full screen.
        Otherwise, return the window to normal.
        """
        if state:
            self.showFullScreen()
        else:
            self.showNormal()

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec_())