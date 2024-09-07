from available_cars import cars_available

print("Welcome to the Car Rental Shop! This are the available cars:")

for car in cars_available:
    print(f"{car['id']}. {car['name']} - ${car['price']}")

response = int(input("Please select your preferred car: "))

selected_car = cars_available
booked_days = input(f"You have selected the  {selected_car[response]['name']}. How many days would you like to rent it? ")
total_price = selected_car[response]['price'] * int(booked_days)

confirmation = input(f"Your total cost will be ${total_price}, Do you want to proceed? (Y/N) ")


if confirmation.lower() == 'y':
    cars_available.pop(response)
    print("Thank you for booking your car. Enjoy your trip!")
    print(f"Remaining cars: {len(cars_available)}")
    for car in cars_available:
        print(f"{car['id']}. {car['name']} - ${car['price']}")
else:
    print("Your booking has been cancelled.")

