from datetime import date


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    # Check if they haven't had their birthday yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


# 1. Receive inputs from the user
print("--- Age Calculator ---")
year = int(input("Enter your birth year (e.g., 1995): "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))

# 2. Convert inputs into a date object
user_birthday = date(year, month, day)

# 3. Calculate and display the age
user_age = calculate_age(user_birthday)
print(f"\nYou are {user_age} years old!")
