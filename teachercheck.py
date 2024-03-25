from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
class AdminView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x720+200+45")
        self.root.title("student")

        img_path = r"./bg.png"
        img3 = Image.open(img_path)
        img3 = img3.resize(
            (1080, 710), resample=Image.LANCZOS
        )
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1080, height=720)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=0, y=0, width=1080, height=720)

        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Students Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=0, y=0, width=1000, height=700)

        img_path = r"./bg.png"
        img_right = Image.open(img_path)
        img_right = img_right.resize(
            (1530, 710), resample=Image.LANCZOS
        )  # Use LANCZOS for antialiasing
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        bg_img_right = Label(Right_frame, image=self.photoimg_right)
        bg_img_right.place(x=5, y=5, width=980, height=130)

        #   search system

        search_frame = LabelFrame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search system ",
            font=("times new roman", 12, "bold"),
        )
        search_frame.place(x=5, y=135, width=950, height=70)

        search_label = Label(
            search_frame,
            text="Search By:",
            font=("times new roman", 15, "bold"),
            bg="red",
        )
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(
            search_frame,
            font=("times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        search_combo["values"] = (
            "Select ",
            "RollNo",
            "IV",
            "III",
            "IV",
            "V",
            "VI",
            "VII",
            "VIII",
        )
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        self.search_var = StringVar()
        search_entry = ttk.Entry(
            search_frame, width=15, font=("times new roman", 12, "bold"),textvariable=self.search_var
        )
        search_entry.grid(row=0, column=2, padx=10, sticky=W)
        # button
        search_btn = Button(
            search_frame,
            text="Search",
            command=self.search_data,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width="10",
        )
        search_btn.grid(row=0, column=3)

        # showall_btn = Button(
        #     search_frame,
        #     text="Show All",
        #     font=("times new roman", 12, "bold"),
        #     bg="blue",
        #     fg="white",
        #     width="10",
        # )
        # showall_btn.grid(row=0, column=4)

        # table
        table_frame = Frame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            # font=("times new roman", 12, "bold"),
        )
        table_frame.place(x=5, y=210, width=950, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)


        self.student_table = ttk.Treeview(
            table_frame,
            column=("studentid", "dep", "course", "year", "semester", "studentname","studentdiv","studentgender","dob","email" ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("studentid", text="RollNo")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("studentname", text="Name")
        self.student_table.heading("studentdiv", text="Division")
        self.student_table.heading("studentgender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table["show"] = "headings"

        self.student_table.column("studentid", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("studentname", width=100)
        self.student_table.column("studentdiv", width=100)
        self.student_table.column("studentgender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)


        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        # get cursor no use self.student_table.bind("<ButtonRelease>", self.get_cursor)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Pratik@6878",
            database="face_recognition",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select* from studentdetails")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    def search_data(self):
        search_query = self.search_var.get()
        if search_query:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Pratik@6878",
                database="face_recognition",
            )
            my_cursor = conn.cursor()
            query = "SELECT * FROM studentdetails WHERE studentid LIKE %s OR dep LIKE %s OR course LIKE %s OR year LIKE %s OR semester LIKE %s OR studentname LIKE %s OR studentdiv LIKE %s OR studentgender LIKE %s OR dob LIKE %s OR email LIKE %s"
            my_cursor.execute(query, ('%' + search_query + '%',) * 10)
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        else:
            # If search query is empty, fetch all data
            self.fetch_data()


if __name__ == "__main__":
    root = Tk()
    obj = AdminView(root)
    root.mainloop()
