"""
A program to determine a users total holiday cost.
Includes plane cost, hotel cost and car rental cost.
"""

def plane_cost():
    if city_flight == "Ireland":
        flight_total = 50
    elif city_flight == "Paris":
        flight_total = 55
    elif city_flight == "Amsterdam":
        flight_total = 40
    elif city_flight == "Berlin":
        flight_total = 60
    else:
        print("Destination not recognized")
    return flight_total

def hotel_cost():
    hotel_total = num_nights * 50
    return hotel_total

def car_rental():
    car_total = rental_days * 25
    return car_total

def holiday_cost():
    holiday_total = plane_cost() + hotel_cost() + car_rental()
    return holiday_total

print("-"*50)
print("Welcome to the holiday cost calculator!")
print("-"*50)

print("City destinations are: \nIreland \nParis \nAmsterdam \nBerlin")
while True:
    city_flight = (input("Which destination are you flying to:\t")).capitalize()
    if city_flight == "Ireland" or city_flight == "Paris" \
        or city_flight == "Amsterdam" or city_flight == "Berlin":
        break
    else:
        print("Destination not recognized")

while True:
    num_nights = input("Number of nights at the hotel:\t")
    if num_nights.isnumeric():
        num_nights = int(num_nights)
        break
    else:
        print("Please type a number")

while True:
    rental_days = input("Number of days to rent a car:\t")
    if rental_days.isnumeric():
        rental_days = int(rental_days)
        break
    else:
        print("Please type a number")

print("-"*50)
print(f"Plane to {city_flight}: \t£{"%.2f"%plane_cost()}\
      \nHotel for {num_nights} nights: \t£{"%.2f"%hotel_cost()}\
      \nCar rental for {rental_days} days: \t£{"%.2f"%car_rental()}\
      \nHoliday Total: £{"%.2f"%holiday_cost()}")
print("-"*50)
