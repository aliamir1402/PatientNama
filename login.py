import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import os

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500, 500, 500, 500)
    win.setWindowTitle("PatientNama - Login")
    win.setWindowIcon(QIcon("Me.jpg"))
    win.setToolTip("PatientNama - Patient Record Management APP")
    win.setStyleSheet("background-color:#222021;border:0px solid #48494B;border-radius:5px;color:white;padding:0px;margin-left:5px;")
    
    a=200
    bg_image = QtWidgets.QLabel(win)
    bg_image.setGeometry(580, 0, a, a)
    bg_image.setPixmap(QtGui.QPixmap("Me.jpg").scaled(a, a))
    bg_image.resize(250,250)
    
    def clicked(self):
        print("Button Clicked.")
        if lbl_username1.text()=="admin" and lbl_password1.text()=="12345":
            os.system('python main.py')
            lbl_message.setStyleSheet("background-color: lightgreen;color:black;")
            lbl_message.setText("Access Allowed")
        else:
            lbl_message.setStyleSheet("background-color: red")
            lbl_message.setText("Invalid Username / Password")
            
    

    lbl_username = QtWidgets.QLabel(win)
    lbl_username.setText("Enter Username:")
    lbl_username.move(600, 300)
    lbl_username1 = QtWidgets.QLineEdit(win)
    lbl_username1.move(700, 300)

    lbl_password = QtWidgets.QLabel(win)
    lbl_password.setText("Enter Password:")
    lbl_password.move(600, 350)
    lbl_password1 = QtWidgets.QLineEdit(win)
    lbl_password1.move(700, 350)

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Login')
    btn_save.clicked.connect(clicked)
    btn_save.move(700, 400)
    btn_save.setStyleSheet("background-color: #3b5998; color: white; border-radius: 5px; padding: 5px;")

    lbl_message = QtWidgets.QLabel(win)
    lbl_message.setText("")
    lbl_message.move(600,230)
    lbl_message.resize(200,50)
    lbl_message.setStyleSheet("font-weight: bold;")

    # Add CSS to labels and line edits
    lbl_username.setStyleSheet("font-weight: bold;")
    lbl_password.setStyleSheet("font-weight: bold;")
    lbl_username1.setStyleSheet("border: 1px solid black; border-radius: 5px; padding: 5px;")
    lbl_password1.setStyleSheet("border: 1px solid black; border-radius: 5px; padding: 5px;")

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
