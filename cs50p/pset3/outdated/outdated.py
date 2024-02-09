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
    validate(date[0])

def validate(month)
    if month not in months:
        raise KeyError
    return
