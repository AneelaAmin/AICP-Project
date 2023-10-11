# Constants
DAYS_OF_WEEK= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
DISCOUNT_TIME = 16
DISCOUNT_PERCENTAGE = 0.5
EVENING_CHARGE = 2


# Function to calculate check digit for frequent parking number
def calculate_check_digit(number):
    total = 0
    for i in range(4):
        total += int(number[i]) * (i + 1)
    return total % 11


# Task 1 - Calculating the price to park
def calculate_parking_price(day, arrival_hour, parking_hours, frequent_parking_number):
    if arrival_hour < 8 or arrival_hour >= 24:
        return "No parking allowed between Midnight and 08:00."

    day_index = DAYS_OF_WEEK.index(day)
    base_price = 0

    if arrival_hour < DISCOUNT_TIME:
        base_price = arrival_hour * 2
    else:
        base_price = DISCOUNT_TIME * 2

    total_price = base_price * parking_hours

    if frequent_parking_number:
        check_digit = calculate_check_digit(frequent_parking_number)
        if check_digit == int(frequent_parking_number[-1]):
            if arrival_hour >= DISCOUNT_TIME:
                total_price *= (1 - DISCOUNT_PERCENTAGE)
            else:
                total_price *= 0.9

    return total_price


# Task 2 - Keeping a total of the payments
daily_total = 0


# Task 3 - Making payments fairer
def calculate_fair_parking_price(day, arrival_hour, parking_hours):
    if arrival_hour < DISCOUNT_TIME:
        total_price = arrival_hour * 2
    else:
        total_price = DISCOUNT_TIME * 2

    if arrival_hour < DISCOUNT_TIME and arrival_hour + parking_hours > DISCOUNT_TIME:
        total_price += EVENING_CHARGE

    return total_price * parking_hours


# Main program
day = input("Enter the day of the week: ")
arrival_hour = int(input("Enter the arrival hour (24-hour format): "))
parking_hours = int(input("Enter the number of parking hours: "))
frequent_parking_number = input("Enter frequent parking number (or press Enter to skip): ")

if day in DAYS_OF_WEEK:
    fair_price = calculate_fair_parking_price(day, arrival_hour, parking_hours)
    print(f"The fair price for parking is: {fair_price:.2f}")

    if frequent_parking_number:
        check_digit = calculate_check_digit(frequent_parking_number)
        if check_digit == int(frequent_parking_number[-1]):
            total_price = fair_price * 0.9
        else:
            total_price = fair_price
            print("Invalid frequent parking number. No discount applied.")
    else:
        total_price = fair_price

    print(f"The total price to pay is: {total_price:.2f}")
    daily_total += total_price
    print(f"Daily total: {daily_total:.2f}")
else:
    print("Invalid day input. Please enter a valid day of the week.")
