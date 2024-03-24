from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face import FaceRecognitionApp
# from face_recognition import Face_Recognition
from Visualize_day_wise_attandence import AttendanceVisualization
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x720+200+45")
        self.root.title("face recognition system")

        # left image of sign in....
        # img = Image.open("image path0")
        # img = img.resize((height, width), Image.ANTIALIAS)
        # self.photoimg = ImageTk.PhotoImage(img)
        # f_lbl = Label(self.root, image=self.photoimg)
        # f_lbl.place(width ,height)

        # background page
        imgbg1 = Image.open(r"./bg.png")
        imgbg1 = imgbg1.resize(
            (1080, 720), Image.BILINEAR
        )  # Change to your desired filter
        self.photoimg1 = ImageTk.PhotoImage(imgbg1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(width=1080, height=720)

        # title

        # option
        # Button 1
        # student details
        img4 = Image.open(r"C:\Users\91799\Desktop\Pythonic-pioneers\ImagesFace\studentDetails.png")
        img4 = img4.resize((300, 300), Image.BILINEAR)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(
            bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2"
        )
        b1.place(width=300, height=300, x=40, y=40)

        b1_1 = Button(
            bg_img, text="student details", command=self.student_details, cursor="hand2"
        )
        b1_1.place(x=40, y=295, width=300, height=40)


        img5 = Image.open(r"C:\Users\91799\Desktop\Pythonic-pioneers\ImagesFace\facerecog.png")
        img5 = img5.resize((300, 300), Image.BILINEAR)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(
            bg_img, image=self.photoimg5, command=self.face_recog, cursor="hand2"
        )
        b2.place(width=300, height=300, x=390, y=40)

        b1_2 = Button(bg_img, text="face_recognition (PRESS Q to exit)", command=self.face_recog, cursor="hand2")
        b1_2.place(x=390, y=295, width=300, height=40)

        # Button 3
        img6 = Image.open(r"C:\Users\91799\Desktop\Pythonic-pioneers\ImagesFace\Defaulter.png")
        img6 = img6.resize((300, 300), Image.BILINEAR)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(
            bg_img, image=self.photoimg6, command=self.defaulter, cursor="hand2"
        )
        b3.place(width=300, height=300, x=740, y=40)

        b1_3 = Button(
            bg_img, text="Defaulter List", command=self.defaulter, cursor="hand2"
        )
        b1_3.place(x=740, y=295, width=300, height=40)

        # Button 4
        img7 = Image.open(r"C:\Users\91799\Desktop\Pythonic-pioneers\ImagesFace\view_photo.png")
        img7 = img7.resize((300, 300), Image.BILINEAR)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img, image=self.photoimg7, command=self.open_img, cursor="hand2")
        b4.place(width=300, height=300, x=40, y=380)

        b1_4 = Button(bg_img, text="view photo", command=self.open_img, cursor="hand2")
        b1_4.place(x=40, y=635, width=300, height=40)

    def open_img(self):
        os.startfile("data")
        
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def face_recog(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognitionApp(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def defaulter(self):
        self.new_window = Toplevel(self.root)
        self.app = AttendanceVisualization(self.new_window)
    # def face_data(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = Face_Recognition(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
