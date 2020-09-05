# basic_window.py
# Import necessary modules
#pyuic5 mainwindow.ui -o MainWindow.py
#https://doc.qt.io/qtforpython/contents.html
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__() # create default constructor for QWidget
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(400, 100, 200, 500)    #x,y,with,height
        self.setWindowTitle('Empty Window in PyQt')
        self.displayLabels()                    #funcion labels
        self.displayUserInfo()                  #function user info
        self.show()                             #Display windwow

    def displayLabels(self):
        """
        Display text and images using QLabels. Check to see if image files exist, 
        if not throw an exception.
        """
        # text = QLabel(self)
        # text.setText("Hello")
        # text.move(300, 15)  #x,y
        image = "20 - PyQT5\images\world2.png"
        try:
            with open(image):
                world_image = QLabel(self)
                world_image.setGeometry(10,10,100,100)
                #world_image.move(25, 40)
                pixmap = QPixmap(image)
                world_image.setPixmap(pixmap)
                world_image.setScaledContents(True)        

        except FileNotFoundError:
                print("Image not found.")

    def displayUserInfo(self):
        """
        Create the labels to be displayed for the User Profile.
        """
        user_name = QLabel(self)
        user_name.setText("John Doe")
        user_name.move(85, 140)
        user_name.setFont(QFont('Arial', 20))
        bio_title = QLabel(self)
        bio_title.setText("Biography")
        bio_title.move(15, 170)
        bio_title.setFont(QFont('Arial', 17))
        about = QLabel(self)
        about.setText("I'm a Software Engineer with 8 years\
        experience creating awesome code.")
        about.setWordWrap(True)
        about.move(15, 190)
        skills_title = QLabel(self)
        skills_title.setText("Skills")
        skills_title.move(15, 240)
        skills_title.setFont(QFont('Arial', 17))
        skills = QLabel(self)
        skills.setText("Python | PHP | SQL | JavaScript")
        skills.move(15, 260)
        experience_title = QLabel(self)
        experience_title.setText("Experience")
        experience_title.move(15, 290)
        experience_title.setFont(QFont('Arial', 17))
        experience = QLabel(self)
        experience.setText("Python Developer")
        experience.move(15, 310)
        dates = QLabel(self)
        dates.setText("Mar 2011 - Present")
        dates.move(15, 330)
        dates.setFont(QFont('Arial', 10))
        experience = QLabel(self)
        experience.setText("Pizza Delivery Driver")
        experience.move(15, 350)
        dates = QLabel(self)
        dates.setText("Aug 2015 - Dec 2017")
        dates.move(15, 370)
        dates.setFont(QFont('Arial', 10))

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)     # 2. Create application object  
    window = EmptyWindow()
    sys.exit(app.exec_())            # Start the event loop and use sys.exit # to closethe application
        