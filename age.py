from datetime import date


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    # Check if they haven't had their birthday yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
