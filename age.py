from datetime import date

a = int(input("enter the year:"))
b = int(input("enter the month:"))
c = int(input("enter the day:"))


def ansar():
    today = date.today()
    # Correct syntax: date(year, month, day)
    bday = date(a, b, c)

    print("Today:", today)
    print("Birthday:", bday)
    day = (today-bday)
    years = day.days // 365
    print(years)


ansar()
