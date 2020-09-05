# lineedit.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton)
from PyQt5.QtCore import Qt

class EntryWindow(QWidget): # Inherits QWidget
    def __init__(self): # Constructor
        super().__init__() # Initializer which calls constructor for QWidget
        self.initializeUI() # Call function used to set up window

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QLineEdit Widget')
        self.displayWidgets()
        self.show()

    def displayWidgets(self):
        '''
        Setup the QLineEdit and other widgets.
        '''
        # Create name label and line edit widgets
        QLabel("Please enter your name below.", self).move(130, 10)
        name_label = QLabel("Name:", self)
        name_label.move(70, 50)
        self.name_entry = QLineEdit(self)               # Creacion campo de texto
        self.name_entry.setAlignment(Qt.AlignCenter)    # Alineamiento de texto
        self.name_entry.move(130, 50)                   # Posicionamiento
        self.name_entry.resize(200, 20)                 # Change size of entry field
        self.clear_button = QPushButton('Clear', self)  # Creacion de boton
        self.clear_button.clicked.connect(self.clearEntries)    # Referenciar a su aplicacion 
        self.clear_button.move(160, 110)                        # Posicionamiento
        self.clear_button.resize(100,30)                         # Resize
    def clearEntries(self):
        '''
        If button is pressed, clear the line edit input field.
        '''
        sender = self.sender()          # Creacion de sender ¿?
        if sender.text() == 'Clear':
            self.name_entry.clear()     # Limpieza de contenido de entrada

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EntryWindow()
    sys.exit(app.exec_())