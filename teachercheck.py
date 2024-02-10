from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("student")

        # Background image
        img_path = r"C:\Users\91799\Desktop\Pythonic-pioneers\Images\background.png"
        img3 = Image.open(img_path)
        img3 = img3.resize(
            (1530, 710), resample=Image.LANCZOS
        )  # Use LANCZOS for antialiasing
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Frames
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=5, y=55, width=1500, height=600)

        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Students Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=780, y=10, width=760, height=580)

        img_path = r"C:\Users\91799\Desktop\Pythonic-pioneers\Images\background.png"
        img_right = Image.open(img_path)
        img_right = img_right.resize(
            (1530, 710), resample=Image.LANCZOS
        )  # Use LANCZOS for antialiasing
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        bg_img_right = Label(Right_frame, image=self.photoimg_right)
        bg_img_right.place(x=5, y=0, width=720, height=130)

        #   search system

        search_frame = LabelFrame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search system ",
            font=("times new roman", 12, "bold"),
        )
        search_frame.place(x=5, y=135, width=710, height=70)

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

        search_entry = ttk.Entry(
            search_frame, width=15, font=("times new roman", 12, "bold")
        )
        search_entry.grid(row=0, column=2, padx=10, sticky=W)
        # button
        search_btn = Button(
            search_frame,
            text="Search",
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width="10",
        )
        search_btn.grid(row=0, column=3)

        showall_btn = Button(
            search_frame,
            text="Show All",
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
            width="10",
        )
        showall_btn.grid(row=0, column=4)

        # table
        table_frame = Frame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            # font=("times new roman", 12, "bold"),
        )
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=("dep", "course", "year", "rollno", "gender"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("rollno", text="Roll NO")
        self.student_table.heading("gender", text="Gender")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("rollno", width=100)
        self.student_table.column("gender", width=100)

        self.student_table.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
