# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# from tkinter import Tk, Label, Entry, Button, StringVar
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# class AttendanceVisualization:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1120x720")
#         self.root.title("Attendance Visualization")

#         # Search bar and button
#         self.search_label = Label(root, text="Enter Student Name:")
#         self.search_label.pack(pady=10)

#         self.search_var = StringVar()
#         self.search_entry = Entry(root, textvariable=self.search_var)
#         self.search_entry.pack(pady=10)

#         self.visualize_button = Button(root, text="Visualize Attendance", command=self.visualize)
#         self.visualize_button.pack(pady=10)

#         # Label to display defaulter percentage
#         self.defaulter_label = Label(root, text="")
#         self.defaulter_label.pack(pady=10)
        
#         self.lecture_label = Label(root, text="")
#         self.lecture_label.pack(pady=10)

#         root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
#     def visualize(self):
#         student_name = self.search_var.get()

#         # Check if the name is entered
#         if not student_name:
#             return

#         # Clear previous plot if it exists
#         for widget in self.root.winfo_children():
#             if isinstance(widget, FigureCanvasTkAgg):
#                 widget.get_tk_widget().destroy()

#         # Filter data for the specified student
#         student_data = data_set[data_set['Name'] == student_name]

#         # Group data by date and count the number of lectures attended
#         daily_attendance = student_data.groupby('Date').size().reset_index(name='Lectures_Attended')

#         # Calculate defaulter percentage
#         total_lectures = 100 
#         lectures_attended = daily_attendance['Lectures_Attended'].sum()
#         Attendance = ((lectures_attended) / total_lectures) * 100

#         # Update the defaulter label
#         self.lecture_label.config(text=f"Total Attendance in a month  {student_name}: {lectures_attended:.2f}%")
#         self.defaulter_label.config(text=f"Defaulter Percentage for {student_name}: {Attendance:.2f}%")

#         # Plot the attendance
#         fig, ax = plt.subplots(figsize=(10, 6))
#         ax.bar(daily_attendance['Date'], daily_attendance['Lectures_Attended'], color='blue')
#         ax.set_title(f'Lecture Attendance for {student_name}')
#         ax.set_xlabel('Date')
#         ax.set_ylabel('Number of Lectures Attended')
#         ax.tick_params(axis='x', rotation=45)

#         # Display the plot on Tkinter window
#         canvas = FigureCanvasTkAgg(fig, master=self.root)
#         canvas_widget = canvas.get_tk_widget()
#         canvas_widget.pack()

#     def on_closing(self):
#         # This method will be called when the window is closed
#         self.root.destroy()

# # Assuming your dataset is already loaded into data_set variable
# data_set = pd.read_csv("C:\\Users\\91799\\Desktop\\Pythonic-pioneers\\Attendance_output.csv")

# if __name__ == "__main__":
#     root = Tk()
#     obj = AttendanceVisualization(root)
#     root.mainloop()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from tkinter import Tk, Label, Entry, Button, StringVar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AttendanceVisualization:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1120x720")
        self.root.title("Attendance Visualization")

        # Search bar and button
        self.search_label = Label(root, text="Enter Student Name:")
        self.search_label.pack(pady=10)

        self.search_var = StringVar()
        self.search_entry = Entry(root, textvariable=self.search_var)
        self.search_entry.pack(pady=10)

        self.visualize_button = Button(root, text="Visualize Attendance", command=self.visualize)
        self.visualize_button.pack(pady=10)

        # Label to display defaulter percentage
        self.defaulter_label = Label(root, text="")
        self.defaulter_label.pack(pady=10)

        self.lecture_label = Label(root, text="")
        self.lecture_label.pack(pady=10)

        root.protocol("WM_DELETE_WINDOW", self.on_closing)

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
            student_data = data_set[data_set['Name'] == student_name]

            # Group data by date and count the number of lectures attended
            daily_attendance = student_data.groupby('Date').size().reset_index(name='Lectures_Attended')

            # Calculate defaulter percentage
            total_lectures = 100
            lectures_attended = daily_attendance['Lectures_Attended'].sum()
            Attendance = ((lectures_attended) / total_lectures) * 100

            # Update the defaulter label
            self.lecture_label.config(
                text=f"Total Attendance in a month  {student_name}: {lectures_attended:.2f}%")
            self.defaulter_label.config(
                text=f"Defaulter Percentage for {student_name}: {Attendance:.2f}%")

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

# Assuming your dataset is already loaded into data_set variable
try:
    data_set = pd.read_csv("C:\\Users\\91799\\Desktop\\Pythonic-pioneers\\Attendance_output.csv")
except Exception as e:
    print(f"Error loading dataset: {e}")
    data_set = pd.DataFrame()  # Initialize an empty DataFrame to avoid further issues

if __name__ == "__main__":
    root = Tk()
    obj = AttendanceVisualization(root)
    root.mainloop()
