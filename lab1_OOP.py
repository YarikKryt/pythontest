def date(day, month, year):
    if day <= 0 or day >= 32:
        print("Error: invalid day, write a correct day")
    if month <= 0 or month >= 13:
        print("Error: invalid month, write a correct day")
    if type(year) != int:
        print("Error: invalid year, write an integer")
    else:
        print(f"{day}/{month}/{year}")
        print(f"{year}-{month}-{day}")
        if day == 1 and month != 1:
            month = month - 1
            day = 31
            print ("Дата мінус 1 день = " , f"{day}/{month}/{year}")
        if day == 1 and month == 1:
            month = 12
            day = 31
            year = year - 1
            print ("Дата мінус 1 день = " , f"{day}/{month}/{year}")
        else:
            day = day - 1
            print("Дата мінус 1 день = ", f"{day}/{month}/{year}")

date(31,2,2015)