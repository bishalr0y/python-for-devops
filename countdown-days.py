from datetime import date

date_string = input("Enter your date in format of DD-MM-YYYY: ")

date_list = date_string.split("-")
print(date_list[2])
user_date = date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
print(f"User Date: {user_date}")

current_date = date.today()
print(f"Current Date: {current_date}")

days_diff = user_date - current_date
print(f"Days remaining for deadline: {days_diff.days}")
