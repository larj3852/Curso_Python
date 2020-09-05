# loginUI.py
# Import necessary modules
"""
TurboGears  is a Python web application framework consisting of several WSGI 
            components such as WebOb, SQLAlchemy, Genshi and Repoze.
            TurboGears is designed around the model–view–controller (MVC) architecture, 
            much like Struts or Ruby on Rails, designed to make rapid web application 
            development in Python easier and more maintainable.
"""
import sys
#Apicacion, Widget, Labels Message Boxes, Botones, Chequeos, Lineas editables
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QMessageBox,
QLineEdit, QPushButton, QCheckBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class LoginUI(QWidget):
    def __init__(self): # Constructor
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle('3.1 – Login GUI')
        self.loginUserInterface()
        self.show()

    def loginUserInterface(self):
        """
        Create the login GUI.
        """
        login_label = QLabel(self)
        login_label.setText("login")
        login_label.move(180, 10)
        login_label.setFont(QFont('Arial', 20))
        # Username and password labels and line edit widgets
        name_label = QLabel("username:", self)
        name_label.move(30, 60)
        self.name_entry = QLineEdit(self)
        self.name_entry.move(110, 60)
        self.name_entry.resize(220, 20)
        password_label = QLabel("password:", self)
        password_label.move(30, 90)
        self.password_entry = QLineEdit(self)
        self.password_entry.move(110, 90)
        self.password_entry.resize(220, 20)
        # Sign in push button
        sign_in_button = QPushButton('login', self)
        sign_in_button.move(100, 140)
        sign_in_button.resize(200, 40)
        sign_in_button.clicked.connect(self.clickLogin)
        # Display show password checkbox
        show_pswd_cb = QCheckBox("show password", self)
        show_pswd_cb.move(110, 115)
        show_pswd_cb.stateChanged.connect(self.showPassword) 
        show_pswd_cb.toggle()
        show_pswd_cb.setChecked(False)
        # Display sign up label and push button
        not_a_member = QLabel("Not a member?", self)
        not_a_member.move(70, 200)
        sign_up = QPushButton("Create New User", self)
        sign_up.move(160, 195)
        sign_up.clicked.connect(self.createNewUser)

    def clickLogin(self):
        """
        When user clicks sign in button, check if username and password
        match any existing profiles in users.txt.
        If they exist, display messagebox and close program.
        If they don't, display error messagebox.
        """
        users = {} # Create empty dictionary to store user information
        # Check if users.txt exists, otherwise create new file
        try:
            with open("files/users.txt", 'r') as f:
                for line in f:
                    user_fields = line.split(" ")
                    username = user_fields[0]
                    password = user_fields[1].strip('\n')
                    users[username] = password
        except FileNotFoundError:
            print("The file does not exist. Creating a new file.")
            f = open ("files/users.txt", "w")
            username = self.name_entry.text()
            password = self.password_entry.text()
            
        if (username, password) in users.items():
            QMessageBox.information(self, "Login Successful!", "Login Successful!", QMessageBox.Ok, QMessageBox.Ok)
            self.close() # close program
        else:
            QMessageBox.warning(self, "Error Message", "The username or password is incorrect.", QMessageBox.Close, QMessageBox.Close)
    
    def showPassword(self, state):
        '''
        If checkbox is enabled, view password.
        Else, mask password so others cannot see it.
        '''
        if state == Qt.Checked:
            self.password_entry.setEchoMode(QLineEdit.Normal) 
        else:
            self.password_entry.setEchoMode(QLineEdit.Password) #Mostrar Pasword

    def createNewUser(self):
        """
        When the sign up button is clicked, open
        a new window and allow the user to create a new account.
        """
        self.create_new_user_dialog = CreateNewUser()
        self.create_new_user_dialog.show()

    def closeEvent(self, event):
        """
        Display a QMessageBox when asking the user if they want to quit the
        program.
        """
        # Set up message box
        quit_msg = QMessageBox.question(self, "Quit Application?",
        "Are you sure you want to Quit?", QMessageBox.No | QMessageBox.Yes,
        QMessageBox.Yes)
        if quit_msg == QMessageBox.Yes:
            event.accept() # accept the event and close the application
        else:
            event.ignore() # ignore the close event






"""
------------------------------------------------------------------------------------------------------- 
"""
# Registration.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox,
QPushButton, QLabel, QLineEdit)
from PyQt5.QtGui import QPixmap  



class CreateNewUser(QWidget):
 
    def __init__(self):
        super().__init__()
        self.initializeUI() # Call our function used to set up window
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('3.2 - Create New User')
        self.displayWidgetsToCollectInfo()
        self.show()

    def displayWidgetsToCollectInfo(self):
        """
        Create widgets that will be used to collect information
        from the user to create a new account.
        """
        # Create label for image
        new_user_image = "images/new_user_icon.png"
        try:
            with open(new_user_image):
                new_user = QLabel(self)
                pixmap = QPixmap(new_user_image)
                new_user.setPixmap(pixmap)
                new_user.move(150, 60)
        except FileNotFoundError:
            print("Image not found.")
    
        login_label = QLabel(self)
        login_label.setText("create new account")
        login_label.move(110, 20)
        login_label.setFont(QFont('Arial', 20))
        # Username and fullname labels and line edit widgets
        name_label = QLabel("username:", self)
        name_label.move(50, 180)
        self.name_entry = QLineEdit(self)
        self.name_entry.move(130, 180)
        self.name_entry.resize(200, 20)
        name_label = QLabel("full name:", self)
        name_label.move(50, 210)
        name_entry = QLineEdit(self)
        name_entry.move(130, 210)
        name_entry.resize(200, 20)

        # Create password and confirm password labels and line edit widgets
        pswd_label = QLabel("password:", self)
        pswd_label.move(50, 240)
        self.pswd_entry = QLineEdit(self)
        self.pswd_entry.setEchoMode(QLineEdit.Password) #Modo contraseña
        self.pswd_entry.move(130, 240)
        self.pswd_entry.resize(200, 20)
        confirm_label = QLabel("confirm:", self)
        confirm_label.move(50, 270)
        self.confirm_entry = QLineEdit(self)
        self.confirm_entry.setEchoMode(QLineEdit.Password)
        self.confirm_entry.move(130, 270)
        self.confirm_entry.resize(200, 20)

        # Create sign up button
        sign_up_button = QPushButton("sign up", self)
        sign_up_button.move(100, 310)
        sign_up_button.resize(200, 40)
        sign_up_button.clicked.connect(self.confirmSignUp)

    def confirmSignUp(self):
        """
        When user presses sign up, check if the passwords match.
        If they match, then save username and password text to users.txt.
        """
        pswd_text = self.pswd_entry.text()
        confirm_text = self.confirm_entry.text()
        if pswd_text != confirm_text:
            # Display messagebox if passwords don't match
            QMessageBox.warning(self, "Error Message","The passwords you entered do not match. Please tryagain.", QMessageBox.Close,QMessageBox.Close)
        else:
            # If passwords match, save passwords to file and return to login
            # and test if you can log in with new user information.
            with open("files/users.txt", 'a+') as f:
                f.write(self.name_entry.text() + " ")
                f.write(pswd_text + "\n")
                self.close()



# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginUI()
    sys.exit(app.exec_())










# %%
