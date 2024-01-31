from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector as con
import bcrypt


class LoginApp(QDialog):
    def __init__(self):
        super(LoginApp, self).__init__()
        loadUi("loginform.ui", self)
        self.b1.clicked.connect(self.login)
        self.b2.clicked.connect(self.show_reg)

    def login(self):
        em = self.tb1.text()
        pw = self.tb2.text()

        try:
            with con.connect(
                host="localhost",
                user="root",
                password="Ayushi@8383",
                db="face_recognition",
            ) as db:
                cursor = db.cursor()
                cursor.execute(
                    "SELECT * FROM student WHERE email=%s AND password=%s", (em, pw)
                )
                result = cursor.fetchone()

                self.tb1.setText("")
                self.tb2.setText("")

                if result:
                    QMessageBox.information(
                        self, "Login Output", "Congrats!!! You Login"
                    )
                else:
                    QMessageBox.information(
                        self, "Login Output", "User name is not registered"
                    )

        except con.Error as err:
            print(f"Database Error: {err}")

    def show_reg(self):
        widget.setCurrentIndex(1)


class RegisterApp(QDialog):
    def __init__(self):
        super(RegisterApp, self).__init__()
        loadUi("signupform.ui", self)
        self.b3.clicked.connect(self.reg)
        self.b4.clicked.connect(self.show_login)

    def reg(self):
        un = self.tb3.text()
        pw = self.tb4.text()
        em = self.tb5.text()

        try:
            with con.connect(
                host="localhost",
                user="root",
                password="Ayushi@8383",
                db="face_recognition",
            ) as db:
                cursor = db.cursor()
                cursor.execute(
                    "SELECT * FROM student WHERE full_name = %s AND password = %s",
                    (un, pw),
                )
                result = cursor.fetchone()

                if result:
                    QMessageBox.information(
                        self, "Login form", "User already registered"
                    )
                else:
                    cursor.execute(
                        "INSERT INTO student (full_name, password, email) VALUES (%s, %s, %s)",
                        (un, pw, em),
                    )
                    db.commit()
                    QMessageBox.information(
                        self, "Login form", "User successfully registered"
                    )

        except con.Error as err:
            print(f"Database Error: {err}")

    def show_login(self):
        widget.setCurrentIndex(0)


# class Face_Recognition_System:
#     def __init__(self, root):
#         self.root = root
#         # window setup
#         self.root.geometry("1080x720")
#         self.root.title("face recognition ")

#         # image background
#         img = Image.open("./Images/backgroundimage_py.png")
#         img.thumbnail((500, 130))
#         self.photoimg = ImageTk.PhotoImage(img)

#         # window set - background
#         firstLabel = Label(self.root, image=self.photoimg)
#         firstLabel.place(width=500, height=130)


# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition_System(root)
#     root.mainloop()
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginform = LoginApp()
registrationform = RegisterApp()
widget.addWidget(loginform)
widget.addWidget(registrationform)
widget.setCurrentIndex(0)
widget.setFixedWidth(1080)
widget.setFixedHeight(720)
widget.show()

app.exec_()
