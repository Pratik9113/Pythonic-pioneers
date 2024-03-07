
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mysql

import credentials as cr
class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("1080x720+200+45")
        self.window.config(bg="white")

        self.bg_img = ImageTk.PhotoImage(file=r"C:\Users\91799\Desktop\Pythonic-pioneers\Tkinter Login Page\images\background1.png")
        background = Label(self.window, image=self.bg_img).place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.window, bg="white")
        frame.place(x=350, y=100, width=500, height=500)

        title1 = Label(frame, text="Sign Up", font=("times new roman", 25, "bold"), bg="white").place(x=20, y=10)
        title2 = Label(frame, text="Join with us", font=("times new roman", 13), bg="white", fg="gray").place(x=20, y=50)

        f_name = Label(frame, text="First name", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=100)
        l_name = Label(frame, text="Last name", font=("helvetica", 15, "bold"), bg="white").place(x=240, y=100)

        self.fname_txt = Entry(frame, font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame, font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Email", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=180)

        self.email_txt = Entry(frame, font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        password = Label(frame, text="New password", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=250)

        self.password_txt = Entry(frame, font=("arial"))
        self.password_txt.place(x=20, y=290, width=420)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame, text="I Agree The Terms & Conditions", variable=self.terms,
                                    onvalue=1, offvalue=0, bg="white", font=("times new roman", 12)).place(x=20, y=350)
        self.signup = Button(frame, text="Sign Up", command=self.signup_func, font=("times new roman", 18, "bold"),
                            bd=0, cursor="hand2", bg="red", fg="white").place(x=50, y=400, width=150)
        self.create_button = Button(frame,text="Login",command=self.redirect_window,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=400,width=150)

    def signup_func(self):
        if not all((self.fname_txt.get(), self.lname_txt.get(), self.email_txt.get(), self.password_txt.get())):
            messagebox.showerror("Error!", "All fields are required", parent=self.window)
        elif self.terms.get() == 0:
            messagebox.showerror("Error!", "Please agree with our Terms & Conditions", parent=self.window)
        else:
            try:
                connection = mysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("SELECT * FROM student_register WHERE email=%s", (self.email_txt.get(),))
                row = cur.fetchone()

                if row:
                    messagebox.showerror("Error!", "The email id already exists, please try again with another email id",
                                        parent=self.window)
                else:
                    cur.execute("INSERT INTO student_register (f_name, l_name, email, password) VALUES (%s, %s, %s, %s)",
                                (self.fname_txt.get(), self.lname_txt.get(), self.email_txt.get(), self.password_txt.get()))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!", "Registration Successful", parent=self.window)
                    self.reset_fields()
            except mysql.Error as es:
                messagebox.showerror("Error!", f"MySQL Error: {es}", parent=self.window)
                
    # def redirect_window(self):
    #     self.window.destroy()
    #     # Importing the signup window.
    #     # The page must be in the same directory
    #     root = Tk()
    #     obj = login_page(root)
    #     root.mainloop()
    def redirect_window(self):
    # Withdraw the current window (SignUp)
        self.window.withdraw()
        from LoginPage import login_page
        # Create a new Toplevel window for the login page
        root = Toplevel()
        obj = login_page(root)
        root.mainloop()

        
    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.password_txt.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()
