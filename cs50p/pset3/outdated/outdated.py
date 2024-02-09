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

def main():
    while True:
        try:
            date = input("Date: ").split()
            check_month(date[0])
            check_day(date[1].rstrip(','))
            check_year(date[2])
            print(f"{check_year(date[2])}-{check_month(date[0])}-{check_day(date[1].rstrip(','))}")
        except (KeyError, ValueError):
            pass


def check_month(month):
    if month.isdigit() and month <= 12:
        return month
    elif month.isalpha() and month in months:
        return months.index(month.title())
    else:
        raise KeyError


def check_day(day):
    if day >= 1 and day <= 31:
        return day
    else:
        raise ValueError


def check_year(year):
    if len(year) < 4:
        raise ValueError
    else:
        return year


main()
