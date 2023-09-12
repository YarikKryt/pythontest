def date(day, month, year):
    max30daysList= {4,6,9,1} # list of dates that have 30 days max
    #Checking for all exceptions:
    if day <= 0 or day >= 32:
        print("Error: invalid day, write a correct day")
    elif month <= 0 or month >= 13:
        print("Error: invalid month, write a correct day")
    elif type(year) != int:
        print("Error: invalid year, write an integer")
    elif month == 2 and day > 29:
        print("Error: February can't have more than 29 days")
    elif month in max30daysList and day > 30:
        print("Error: this month can't have more than 30 days")
    elif year % 4 != 0 and month == 2 and day == 29:
        print("Error: February can't have more than 28 days in", year, "this is not a leap year")
    else: 
        print(f"{day}/{month}/{year}")
        print(f"{year}-{month}-{day}")
        if day == 1 and month != 1:
            month = month - 1
            day = 31
            print ("Date subtract 1 day = " , f"{day}/{month}/{year}")
        elif day == 1 and month == 1:
            month = 12
            day = 31
            year = year - 1
            print ("Date subtract 1 day = " , f"{day}/{month}/{year}")
        else:
            day = day - 1
            print("Date subtract 1 day = ", f"{day}/{month}/{year}")

date(1,2,2024)





