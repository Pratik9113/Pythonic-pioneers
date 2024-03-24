import pandas as pd
csv_file_path = 'Attendance.csv'
df = pd.read_csv(csv_file_path, header=None, names=['Name', 'Division', 'Roll', 'Date','Time','Subject'])
csv_output_path = 'Attendance_output.csv'
df.to_csv(csv_output_path, index=False)
print(f"CSV created successfully: {csv_output_path}")