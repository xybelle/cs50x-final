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
            date = input("Date: ").strip()
            mdy = validate_date(date)

            m = check_month(mdy[0])
            d = check_day(mdy[1])
            y = check_year(mdy[2])
            print(f"{y}-{m:02}-{d:02}")
            break
        except (KeyError, ValueError):
            pass


def check_month(month):
    if month.isdigit() and int(month) <= 12:
        return int(month)
    elif month.isalpha() and month.title() in months:
        return months.index(month.title()) + 1
    else:
        raise KeyError


def check_day(day):
    if int(day) >= 1 and int(day) <= 31:
        return int(day)
    else:
        raise ValueError


def check_year(year):
    if len(year) < 4:
        raise ValueError
    else:
        return year


def validate_date(mdy):
    if ' ' in mdy and ',' in mdy:
        return mdy.split()
    elif '/' in mdy and not mdy.isalnum():
        print(mdy)
        return mdy.split('/')
    else:
        raise ValueError


main()
