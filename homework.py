attendance = float(input("Enter attendance percentage: "))
internal_score = float(input("Enter internal score: "))

if attendance >= 75 and internal_score >= 40:
    print(" good Eligible for exam")
else:
    if attendance < 75:
        print(" bad Attendance below 75%")
    if internal_score < 40:
        print("Internal score below 40")