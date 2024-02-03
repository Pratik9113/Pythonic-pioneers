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

        # left side frame

        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Students Details",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_path = r"C:\Users\91799\Desktop\Pythonic-pioneers\Images\background.png"
        img_left = Image.open(img_path)
        img_left = img_left.resize(
            (1530, 710), resample=Image.LANCZOS
        )  # Use LANCZOS for antialiasing
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bg_img_left = Label(Left_frame, image=self.photoimg_left)
        bg_img_left.place(x=5, y=0, width=720, height=130)

        # current course frame
        current_course_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current course",
            font=("times new roman", 12, "bold"),
        )
        current_course_frame.place(x=5, y=135, width=720, height=150)

        dep_label = Label(
            current_course_frame,
            text="Department",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(
            current_course_frame,
            font=("times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        dep_combo["values"] = (
            "Select Department",
            "Computer",
            "IT",
            "ENTC",
            "EXTC",
            "INST",
            "MCA",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_label = Label(
            current_course_frame,
            text="Courses",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(
            current_course_frame,
            font=("times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        course_combo["values"] = (
            "Select Courses",
            "FE",
            "SE",
            "TE",
            "BE",
        )
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # /************ year ***********/

        # year
        year_label = Label(
            current_course_frame,
            text="Year",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(
            current_course_frame,
            font=("times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        year_combo["values"] = (
            "Select year",
            "2020-2024",
            "2021-2025",
            "2022-2026",
            "2023-2027",
        )
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        semester_label = Label(
            current_course_frame,
            text="Semester",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        semester_label.grid(row=1, column=2, padx=10)

        semester_combo = ttk.Combobox(
            current_course_frame,
            font=("times new roman", 12, "bold"),
            width=17,
            state="readonly",
        )
        semester_combo["values"] = (
            "Select Semester",
            "I",
            "II",
            "III",
            "IV",
            "V",
            "VI",
            "VII",
            "VIII",
        )
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student frame

        class_student_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="CLASS STUDENT ",
            font=("times new roman", 12, "bold"),
        )
        class_student_frame.place(x=5, y=250, width=720, height=300)

        # student id ************************
        studentID_label = Label(
            class_student_frame,
            text="StudentId:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold")
        )
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # student name *********************
        studentName_label = Label(
            class_student_frame,
            text="Student Name:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold")
        )
        studentName_entry.grid(row=0, column=3, padx=10, sticky=W)

        # class div ************************
        student_div_label = Label(
            class_student_frame,
            text="Division:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        student_div_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold")
        )
        student_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # gender  *********************
        student_gender_label = Label(
            class_student_frame,
            text="Gender",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        student_gender_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold")
        )
        student_gender_entry.grid(row=1, column=3, padx=10, sticky=W)

        # dob ************************
        student_dob_label = Label(
            class_student_frame,
            text="DOB:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_dob_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        student_dob_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold")
        )
        student_dob_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # gender  *********************
        student_email_label = Label(
            class_student_frame,
            text="Email:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        student_email_entry = ttk.Entry(
            class_student_frame, width=20, font=("times new roman", 13, "bold")
        )
        student_email_entry.grid(row=2, column=3, padx=10, sticky=W)

        # radio button ************************
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, text="Take a Photo Sample", value="Yes"
        )
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame, text="Do not  a Photo Sample", value="Yes"
        )
        radiobtn2.grid(row=6, column=1)

        # button frame
        btn_frame = Frame(
            class_student_frame,
            bd=2,
            relief=RIDGE,
            bg="white",
        )
        btn_frame.place(x=0, y=200, width=715, height=40)

        save_btn = Button(
            btn_frame,
            text="Save",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width="17",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(
            btn_frame,
            text="Update",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width="17",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width="17",
        )
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(
            btn_frame,
            text="Reset",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width="17",
        )
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(
            class_student_frame,
            bd=2,
            relief=RIDGE,
            bg="white",
        )
        btn_frame1.place(x=0, y=235, width=715, height=40)

        take_photo_btn = Button(
            btn_frame1,
            text="take photo sample",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width="17",
        )
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(
            btn_frame1,
            text="update photo sample",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width="17",
        )
        update_photo_btn.grid(row=0, column=1)
        #
        #
        #
        # right frame
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Students Details",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=780, y=10, width=660, height=580)

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


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
