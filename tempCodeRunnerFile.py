y()
    #                 print(f"{name} marked for attendance on {date.today()}.")
    def markAttendance(self, name):
        with open("Attendance.csv", "r+") as f:
            myDataList = f.readlines()
            nameList = [line.split(",")[0] for line in myDataList]
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime("%Y-%m-%d,%H:%M:%S")
                day = current_date.day
                subject = ""