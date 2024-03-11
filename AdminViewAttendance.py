# import pandas as pd

# # Sample data
# data = ["Laukik,D10C,41.jpeg", "John,D10B,22.jpeg", "Jane,D11A,31.jpeg"]

# # Extract information from the data
# processed_data = [item.split(",") for item in data]
# names, divisions, roll_numbers = zip(*processed_data)

# # Create a DataFrame
# df = pd.DataFrame({
#     'Name': names,
#     'Division': divisions,
#     'Roll Number': roll_numbers,
# })

# # Save the DataFrame to a CSV file
# df.to_csv('output.csv', index=False)

# print("Data has been processed and saved to 'output.csv'")



# import cv2
# import numpy as np
# import os
# import pandas as pd
# from datetime import datetime
# import time
# import threading
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
# def markAttendanceWithDelay(name):
#     markAttendance(name)
#     threading.Thread(target=lambda: time.sleep(30)).start()


import cv2
import numpy as np
import os
import pandas as pd
from datetime import datetime
import time
import threading

# Directory containing the image files
image_directory = r"C:\Users\91799\Desktop\face reco using firefox\data"

# Get a list of all files in the directory
image_files = [f for f in os.listdir(image_directory) if f.lower().endswith('.jpeg')]

# Initialize variables to store data
data = []
classNames = []

# Process each image file
for image_file in image_files:
    # Extract information from the filename
    name, division, roll_number = image_file.split(',')[0].split('.')

    # Append data to the list
    data.append([name, division, roll_number])
    classNames.append(name)

# Convert data list to a Pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Division', 'Roll Number'])
    
# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

# ... (rest of the code remains unchanged)

# Function to mark attendance with delay
# def markAttendanceWithDelay(name):
#     markAttendance(name)
#     pass
#     threading.Thread(target=lambda: time.sleep(30)).start()

# ... (rest of the code remains unchanged)
