# # import pandas as pd

# # # Sample data
# # data = ["Laukik,D10C,41.jpeg", "John,D10B,22.jpeg", "Jane,D11A,31.jpeg"]

# # # Extract information from the data
# # processed_data = [item.split(",") for item in data]
# # names, divisions, roll_numbers = zip(*processed_data)

# # # Create a DataFrame
# # df = pd.DataFrame({
# #     'Name': names,
# #     'Division': divisions,
# #     'Roll Number': roll_numbers,
# # })

# # # Save the DataFrame to a CSV file
# # df.to_csv('output.csv', index=False)

# # print("Data has been processed and saved to 'output.csv'")



# # import cv2
# # import numpy as np
# # import os
# # import pandas as pd
# # from datetime import datetime
# # import time
# # import threading
# # image_directory = r"C:\Users\91799\Desktop\face reco using firefox\data"
# # image_files = [f for f in os.listdir(image_directory) if f.lower().endswith('.jpeg')]
# # data = []
# # classNames = []
# # for image_file in image_files:
# #     name, division, roll_number = image_file.split(',')[0].split('.')
# #     data.append([name, division, roll_number])
# #     classNames.append(name)
# # df = pd.DataFrame(data, columns=['Name', 'Division', 'Roll Number'])
# # df.to_csv('output.csv', index=False)
# # def markAttendanceWithDelay(name):
# #     markAttendance(name)
# #     threading.Thread(target=lambda: time.sleep(30)).start()


# import cv2
# import numpy as np
# import os
# import pandas as pd
# from datetime import datetime
# import time
# import threading

# # Directory containing the image files
# image_directory = r"C:\Users\91799\Desktop\face reco using firefox\data"
# image_files = [f for f in os.listdir(image_directory) if f.lower().endswith('.jpeg')]
# data = []
# classNames = []
# for image_file in image_files:
#     name, division, roll_number = image_file.split(',')[0].split('.')
#     data.append([name, division, roll_number])
#     classNames.append(name)
# df = pd.DataFrame(data, columns=['Name', 'Division', 'Roll Number'])
# df.to_csv('output.csv', index=False)

import pandas as pd
from tkinter import Tk, Label, Entry, Button, StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, Frame
class AttendanceVisualization:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x720+200+45")
        self.root.title("Attendance Visualization")

        self.root.configure(bg="black")

        # Create a frame as a background for your widgets
        bg_frame = Frame(root, bg="black")  # Set background color for the frame
        bg_frame.pack(expand=True, fill="both")

        # Label for entering student name
        self.search_label = Label(bg_frame, text="Enter Student Name:", bg="#000000", fg="#ffffff" ,font=("Helvetica", 16) )
        self.search_label.pack(pady=10)

        # Entry widget for student name
        self.search_var = StringVar()
        self.search_entry = Entry(bg_frame, textvariable=self.search_var,font=("Helvetica", 10))
        self.search_entry.pack(pady=10)

        # Button for visualizing attendance
        self.visualize_button = Button(bg_frame, text="Visualize Attendance", command=self.visualize, bg="#4caf50", fg="#ffffff",font=("Helvetica", 14))
        self.visualize_button.pack(pady=10)

        # Label to display defaulter percentage
        self.defaulter_label = Label(bg_frame, text="", bg="#ffffff", fg="#ff0000",font=("Helvetica", 14))
        self.defaulter_label.pack(pady=10)

        # Label to display lecture information
        self.lecture_label = Label(bg_frame, text="", bg="#ffffff", fg="#0000ff")
        self.lecture_label.pack(pady=10)
        
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Load dataset
        try:
            self.data_set = pd.read_csv("Attendance_output.csv")
        except Exception as e:
            print(f"Error loading dataset: {e}")
            self.data_set = pd.DataFrame()  # Initialize an empty DataFrame to avoid further issues

    def visualize(self):
        student_name = self.search_var.get()

        # Check if the name is entered
        if not student_name:
            return 

        # Clear previous plot if it exists
        for widget in self.root.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()

        try:
            # Filter data for the specified student
            student_data = self.data_set[self.data_set['Name'] == student_name]

            # Group data by date and count the number of lectures attended
            daily_attendance = student_data.groupby('Date').size().reset_index(name='Lectures_Attended')

            # Calculate attendance percentage
            total_lectures = 120
            lectures_attended = daily_attendance['Lectures_Attended'].sum()
            attendance_percentage = (lectures_attended / total_lectures) * 100

            # Update labels
            self.lecture_label.config(
                text=f"Total Attendance for {student_name}: {lectures_attended}/{total_lectures}")
            self.defaulter_label.config(
                text=f"Attendance Percentage for {student_name}: {attendance_percentage:.2f}%")

            # Plot the attendance
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(daily_attendance['Date'], daily_attendance['Lectures_Attended'], color='blue')
            ax.set_title(f'Lecture Attendance for {student_name}')
            ax.set_xlabel('Date')
            ax.set_ylabel('Number of Lectures Attended')
            ax.tick_params(axis='x', rotation=45)

            # Display the plot on Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()

        except Exception as e:
            print(f"An error occurred: {e}")

    def on_closing(self):
        # This method will be called when the window is closed
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = AttendanceVisualization(root)
    root.mainloop()
