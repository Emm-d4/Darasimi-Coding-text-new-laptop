import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print("\nHere is your calendar:\n")
print(calendar.month(year, month))
