import calendar
yy = int(input("enter the current year: "))
mm = int(input("enter the current month in numbers: "))
if mm > 12:
    print("sir pls enter a valid month")
else:
    print(calendar.month(yy, mm))