import datetime
import calendar

# Get today's date and store it in the variable
_year = datetime.date.today().year
_date = datetime.date.today().day
_month = datetime.date.today().month
# gets the weekday in integer.( where monday = 0 and sunday = 6)
_day = datetime.date.today().weekday()
myDate = datetime.date(_year, _month, _date)

yearLimit = _year + 10
Occurrence = 0


# method to print the Date and Day
def printdate(_mydate):
    print("Date: ", _mydate)
    print("Day: ", calendar.day_name[_mydate.weekday()])
    print()


# method that validates that the date actually exist in the calendar.
def validate(year, month, date):
    try:
        datetime.datetime(int(year), int(month), int(date))
    except ValueError:
        return False
    return True


# Method that counts the occurrence of how many times that date and day matches.
def CountTodaysOccurance(year, date, month, day):
    global Occurrence
    # loop only runs for 10 years
    while year < yearLimit:
        # resets the month variable to 1 after it reaches 12
        while month < 13:
            if validate(year, month, date):
                checkDate = datetime.date(year, month, date)
                if day == checkDate.weekday():
                    printdate(checkDate)
                    Occurrence += 1
            month += 1
        month = 1
        year += 1


# method calls
printdate(myDate)
CountTodaysOccurance(_year, _date, _month, _day)
print("It will occur ", Occurrence, " times in 10 years")
input("Program Finished Running")