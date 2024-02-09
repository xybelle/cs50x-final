months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("Date: ").split()
    check_month(date[0])
    check_day[date[1]]

def check_month(month):
    if month.isdigit and month !> 12:
        return month
    elif month.isalpha and month in months:
        return months.index(month)
    else:
        raise KeyError

def check_day(day):
    if day >= 1 and day <= 31:
        return day
    else:
        raise Value
