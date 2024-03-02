from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

from teachercheck import AdminView


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x720+0+0")
        self.root.title("student")

        # ------variable -------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_StudentId = StringVar()
        self.var_StudentName = StringVar()
        self.var_Studentdiv = StringVar()
        self.var_Studentgender = StringVar()
        self.var_DOB = StringVar()
        self.var_email = StringVar()
        self.var_radio1 = StringVar()
        self.var_radio2 = StringVar()

        # Background image
        img_path = r"C:\Users\91799\Desktop\pythonprojectmainpratik\bg.png"
        img3 = Image.open(img_path)
        img3 = img3.resize(
            (1080, 720), resample=Image.LANCZOS
        )  # Use LANCZOS for antialiasing
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1080, height=720)

        # Frames
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=40, y=0, width=1000, height=700)

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

        img_path = r"C:\Users\91799\Desktop\pythonprojectmainpratik\bg.png"
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
            textvariable=self.var_dep,
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
            textvariable=self.var_course,
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
            textvariable=self.var_year,
        )
        year_combo["values"] = (
            "Select year",
            "2020",
            "2021",
            "2022",
            "2023",
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
            textvariable=self.var_semester,
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
            class_student_frame,
            width=20,
            textvariable=self.var_StudentId,
            font=("times new roman", 13, "bold"),
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
            class_student_frame,
            textvariable=self.var_StudentName,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        studentName_entry.grid(row=0, column=3, padx=10, sticky=W)

        # class div ************************
        student_div_label = Label(
            class_student_frame,
            text="Division:",
            font=("times new roman", 12, "bold"),
            bg="white",
            # textvariable=self.var_Studentdiv,
        )
        student_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        student_div_entry = ttk.Entry(
            class_student_frame,
            textvariable=self.var_Studentdiv,
            width=20,
            font=("times new roman", 13, "bold"),
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

        # student_gender_entry = ttk.Entry(
        #     class_student_frame,
        #     textvariable=self.var_Studentgender,
        #     width=20,
        #     font=("times new roman", 13, "bold"),
        # )
        # student_gender_entry.grid(row=1, column=3, padx=10, sticky=W)

        gender_combo = ttk.Combobox(
            class_student_frame,
            font=("times new roman", 12, "bold"),
            width=17,
            state="readonly",
            textvariable=self.var_Studentgender,
        )
        gender_combo["values"] = (
            "Male",
            "Female",
            "Others",
        )
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        # dob ************************
        student_dob_label = Label(
            class_student_frame,
            text="DOB:",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        student_dob_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        student_dob_entry = ttk.Entry(
            class_student_frame,
            width=20,
            textvariable=self.var_DOB,
            font=("times new roman", 13, "bold"),
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
            class_student_frame,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        student_email_entry.grid(row=2, column=3, padx=10, sticky=W)

        # radio button ************************
        radiobtn1 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="Take a Photo Sample",
            value="Yes",
        )
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio2,
            text="Do not  a Photo Sample",
            value="No",
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
            command=self.add_data,
            text="Save",
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width="17",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(
            btn_frame,
            command=self.update_data,
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
            command=self.generate_dataset,
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

    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_StudentName.get() == ""
            or self.var_StudentId.get() == ""
        ):
            messagebox.showerror("Error", "All field are mandatory", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Pratik@6878",
                    database="face_recognition",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into studentdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_StudentId.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_StudentName.get(),
                        self.var_Studentdiv.get(),
                        self.var_Studentgender.get(),
                        self.var_DOB.get(),
                        self.var_email.get(),
                    ),
                )
                conn.commit()
                # self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "success", "student details has been added ", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("error", f"due to : {str(es)}", parent=self.root)

    # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Pratik@6878",
            database="face_recognition",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from studentdetails")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.AdminView.student_table.delete(
                self.AdminView.student_table.get_children()
            )
            for i in data:
                self.AdminView.student_table.insert("", END, values=i)
            conn.commit()
        conn.close

    ####################get cursor
    # def get_cursor(self):
    #     cursor_focus  = self.AdminView.student_table.focus()
    #     content =
    ################################################################
    # generate dataset and take a sample

    ############### update data
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_StudentName.get() == ""
            or self.var_StudentId.get() == ""
        ):
            messagebox.showerror("Error", "All field are mandatory", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update",
                    "Do you want to update the student details",
                    parent=self.root,
                )
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Pratik@6878",
                        database="face_recognition",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update studentdetails set dep =%s,course=%s,year=%s,semester =%s,studentname =%s,studentdiv=%s,studentgender=%s,dob=%s,email=%s where studentid = %s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_StudentName.get(),
                            self.var_Studentdiv.get(),
                            self.var_Studentgender.get(),
                            self.var_DOB.get(),
                            self.var_email.get(),
                            self.var_StudentId.get(),
                        ),
                    )
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "success", "Student details successfully updated", parent=self.root
                )
                conn.commit()
                # self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("error", f"due to : {str(es)}", parent=self.root)

    # generate data set an take photo sample
    # def generate_dataset(self):
    #     if (
    #         self.var_dep.get() == "Select Department"
    #         or self.var_StudentName.get() == ""
    #         or self.var_StudentId.get() == ""
    #     ):
    #         messagebox.showerror("Error", "All field are mandatory", parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(
    #                 host="localhost",
    #                 username="root",
    #                 password="Pratik@6878",
    #                 database="face_recognition",
    #             )
    #             my_cursor = conn.cursor()
    #             my_cursor.execute("select* from student")
    #             myresult = my_cursor.fetchall()
    #             id = 0
    #             for x in myresult:
    #                 id += 1
    #             my_cursor.execute(
    #                 "update studentdetails set dep =%s,course=%s,year=%s,semester =%s,studentname =%s,studentdiv=%s,studentgender=%s,dob=%s,email=%s where studentid = %s",
    #                 (
    #                     self.var_dep.get(),
    #                     self.var_course.get(),
    #                     self.var_year.get(),
    #                     self.var_semester.get(),
    #                     self.var_StudentName.get(),
    #                     self.var_Studentdiv.get(),
    #                     self.var_Studentgender.get(),
    #                     self.var_DOB.get(),
    #                     self.var_email.get(),
    #                     self.var_StudentId.get(),
    #                 ),
    #             )
    #             conn.commit()
    #             # self.fetch_data()
    #             conn.close()

    #             # load predeifind data on front page
    #             face_classifier = cv2.CascadeClassifier(
    #                 "haarcascade_frontalface_default.xml"
    #             )

    #             def face_cropped(img):
    #                 # color into grey scale
    #                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #                 faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    #                 # 1.3 scalling factor
    #                 # 5 minimum neighbour = 5

    #                 for x, y, w, h in faces:
    #                     face_cropped = img[y : y + h, x : x + w]
    #                     return face_cropped

    #             cap = cv2.VideoCapture(0)
    #             img_id = 0
    #             while True:
    #                 ret, my_frame = cap.read()
    #                 if face_cropped(my_frame) is not None:
    #                     img_id += 1
    #                 face = cv2.resize(face_cropped(my_frame), (450, 450))
    #                 face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    #                 file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
    #                 cv2.imwrite(file_name_path, face)
    #                 cv2.putText(
    #                     face,
    #                     str(img_id),
    #                     (50, 50),
    #                     cv2.FONT_HERSHEY_COMPLEX,
    #                     2,
    #                     (0, 255, 0),
    #                     2,
    #                 )
    #                 cv2.imshow("Croped Face", face)

    #                 if cv2.waitKey(1) == 13 or int(img_id) == 100:
    #                     break

    #             cap.release()
    #             cv2.destroyAllWindows()
    #             messagebox.showinfo("Result", "Generating data sets completed !!!")

    #         except Exception as es:
    #             messagebox.showerror("error", f"due to : {str(es)}", parent=self.root)

    
    # 1 march - pratik patil updated code algo changed
    # def generate_dataset(self):
    #     # Open the camera
    #     cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera, you can change it if you have multiple cameras

    #     # Capture a single frame
    #     ret, frame = cap.read()

    #     # Check if the frame is captured successfully
    #     if ret:
    #         # Get division and rollno from your database (replace these with your actual logic)
    #         division = "A"
    #         rollno = "123"

    #         # Define the filename based on division and rollno
    #         filename = f"data/{division}_{rollno}_photo.png"

    #         # Save the captured frame as an image
    #         cv2.imwrite(filename, frame)

    #         # Display a success message
    #         messagebox.showinfo("Capture Success", f"Photo captured and saved as {filename}")

    #     # Release the camera
    #     cap.release()
    #     cv2.destroyAllWindows()
    
    # def generate_dataset(self):
    # # Fetch division and rollno from the database based on student ID
    #     student_id = self.var_StudentId.get()
    #     studentname,division, rollno = self.fetch_division_and_rollno_from_database(student_id)

    # # Check if division and rollno are fetched successfully
    #     if studentname is not None and division is not None and rollno is not None:
    #         # Open the camera
    #         cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera, you can change it if you have multiple cameras

    #         # Capture a single frame
    #         ret, frame = cap.read()

    #         # Check if the frame is captured successfully
    #         if ret:
    #             # Define the filename based on division and rollno
    #             filename = f"data/{studentname},{division},{rollno}.jpeg"

    #             # Save the captured frame as an image
    #             cv2.imwrite(filename, frame)

    #             # Display a success message
    #             messagebox.showinfo("Capture Success", f"Photo captured and saved as {filename}")

    #         # Release the camera
    #         cap.release()
    #         cv2.destroyAllWindows()
    #     else:
    #         # Display an error message if division or rollno is not found
    #         messagebox.showerror("Error", "Failed to fetch division and rollno from the database")
    def generate_dataset(self):
        # Fetch division and rollno from the database based on student ID
        student_id = self.var_StudentId.get()
        studentname, division, rollno = self.fetch_division_and_rollno_from_database(student_id)

        # Check if division and rollno are fetched successfully
        if studentname is not None and division is not None and rollno is not None:
            # Open the camera
            cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera, you can change it if you have multiple cameras

            while True:
                # Capture a single frame
                ret, frame = cap.read()

                # Check if the frame is captured successfully
                if ret:
                    cv2.imshow("Webcam", frame)

                    # Wait for the 'c' key press
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord("c"):
                        # Define the filename based on division and rollno
                        filename = f"data/{studentname},{division},{rollno}.jpeg"

                        # Save the captured frame as an image
                        cv2.imwrite(filename, frame)

                        # Display a success message
                        messagebox.showinfo("Capture Success", f"Photo captured and saved as {filename}")

                        # Release the camera
                        cap.release()
                        cv2.destroyAllWindows()
                        break

                else:
                    # Display an error message if the frame is not captured successfully
                    messagebox.showerror("Error", "Failed to capture frame from the camera")
                    break

        else:
            # Display an error message if division or rollno is not found
            messagebox.showerror("Error", "Failed to fetch division and rollno from the database")
    def fetch_division_and_rollno_from_database(self, student_id):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Pratik@6878",
                database="face_recognition",
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT  studentname,studentdiv,studentid FROM studentdetails WHERE studentid = %s",
                (student_id,),
            )
            result = my_cursor.fetchone()
            conn.close()

            if result:
                return result
            else:
                return None, None , None
        except Exception as es:
            messagebox.showerror("Error", f"Failed to fetch data from the database: {str(es)}")
            return None, None , None 

    # def generate_dataset(self):
    #     if (
    #         self.var_dep.get() == "Select Department"
    #         or self.var_StudentName.get() == ""
    #         or self.var_StudentId.get() == ""
    #     ):
    #         messagebox.showerror("Error", "All fields are mandatory", parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(
    #                 host="localhost",
    #                 username="root",
    #                 password="Pratik@6878",
    #                 database="face_recognition",
    #             )
    #             my_cursor = conn.cursor()
    #             my_cursor.execute("select * from student")
    #             myresult = my_cursor.fetchall()
    #             id = 0
    #             for x in myresult:
    #                 id += 1
    #             my_cursor.execute(
    #                 "update studentdetails set dep =%s,course=%s,year=%s,semester =%s,studentname =%s,studentdiv=%s,studentgender=%s,dob=%s,email=%s where studentid = %s",
    #                 (
    #                     self.var_dep.get(),
    #                     self.var_course.get(),
    #                     self.var_year.get(),
    #                     self.var_semester.get(),
    #                     self.var_StudentName.get(),
    #                     self.var_Studentdiv.get(),
    #                     self.var_Studentgender.get(),
    #                     self.var_DOB.get(),
    #                     self.var_email.get(),
    #                     self.var_StudentId.get(),
    #                 ),
    #             )
    #             conn.commit()
    #             conn.close()

    #             # load predefined data on the front page
    #             face_classifier = cv2.CascadeClassifier(
    #                 "haarcascade_frontalface_default.xml"
    #             )

    #             def face_cropped(img):
    #                 # Convert to grayscale
    #                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #                 faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    #                 for x, y, w, h in faces:
    #                     face_cropped = img[y : y + h, x : x + w]
    #                     return face_cropped

    #             cap = cv2.VideoCapture(0)
    #             img_id = 0
    #             id = self.var_StudentId.get()
    #             while True:
    #                 ret, my_frame = cap.read()
    #                 cropped_face = face_cropped(my_frame)
    #                 if cropped_face is not None:
    #                     img_id += 1
    #                     face = cv2.resize(cropped_face, (450, 450))
    #                     face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    #                     file_name_path = f"data/user.{id}.{img_id}.jpg"
    #                     cv2.imwrite(file_name_path, face)
    #                     cv2.putText(
    #                         face,
    #                         str(img_id),
    #                         (50, 50),
    #                         cv2.FONT_HERSHEY_COMPLEX,
    #                         2,
    #                         (0, 255, 0),
    #                         2,
    #                     )
    #                     cv2.imshow("Cropped Face", face)

    #                 if cv2.waitKey(1) == 13 or int(img_id) == 10:
    #                     break

    #             cap.release()
    #             cv2.destroyAllWindows()
    #             messagebox.showinfo("Result", "Generating data sets completed !!!")

    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
