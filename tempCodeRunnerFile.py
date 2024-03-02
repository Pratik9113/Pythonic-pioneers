import pandas as pd
import xlsxwriter
# Read CSV file
csv_file_path = 'Attendance.csv'
df = pd.read_csv(csv_file_path, header=None, names=['Name', 'Division', 'Roll', 'Time'])

# Create a new Excel file
excel_file_path = 'Attendance.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    # Write the DataFrame to the Excel file
    df.to_excel(writer, index=False, sheet_name='Attendance')

    # Access the XlsxWriter workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['Attendance']

    # Get the dimensions of the DataFrame
    num_rows, num_cols = df.shape

    # Create a list of column headers to use in add_table()
    column_settings = [{'header': column} for column in df.columns]

    # Add the Excel table structure. Pandas will add the data
    worksheet.add_table(0, 0, num_rows, num_cols - 1, {'columns': column_settings})

    # Adjust the column width for better readability
    for i, col in enumerate(df.columns):
        max_len = df[col].astype(str).str.len().max()
        max_len = max_len if max_len > len(col) else len(col)
        worksheet.set_column(i, i, max_len + 2)

print(f"Spreadsheet created successfully: {excel_file_path}")
