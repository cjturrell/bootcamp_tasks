"""
A program to determine a users total holiday cost.
Includes plane cost, hotel cost and car rental cost.
"""
# Functions ==================================================================

def plane_cost(city_flight):
    """
    The function calculates the cost of a plane ticket based on the 
    destination city.
    :return: the value of the variable "flight_total".
    """
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


def hotel_cost(num_nights, hotel_cost=50):
    """
    The function calculates the total cost of a hotel stay based on the number 
    of nights.
    :return: the total cost of the hotel stay.
    """
    hotel_total = num_nights * hotel_cost
    return hotel_total


def car_rental(rental_days, car_rental_cost=25):
    """
    The function calculates the total cost of renting a car based on the 
    number of rental days.
    :return: The variable `car_total` is being returned.
    """
    car_total = rental_days * car_rental_cost
    return car_total


def holiday_cost(plane_cost, hotel_cost, car_rental):
    """
    The function calculates the total cost of a holiday by adding the costs of
    a plane ticket, hotel stay, and car rental.
    :return: the total cost of the holiday, which is calculated by adding the 
    costs of the plane, hotel, and car rental.
    """
    holiday_total = (plane_cost(city_flight) + 
                    hotel_cost(num_nights, hotel_cost=50) + 
                    car_rental(rental_days, car_rental_cost=25))
    return holiday_total


# Welcome message ============================================================
print("-"*50)
print("Welcome to the holiday cost calculator!")
print("-"*50)


print("City destinations are: \nIreland \nParis \nAmsterdam \nBerlin")
# Ensure user input is valid for flight destination
while True:
    city_flight = (input("Which destination are you flying to"
                         ":\t")).capitalize()
    if city_flight == "Ireland" or city_flight == "Paris" \
        or city_flight == "Amsterdam" or city_flight == "Berlin":
        break
    else:
        print("Destination not recognized")

# Ensure user input is numerical for number of hotel nights
while True:
    num_nights = input("Number of nights at the hotel:\t")
    if num_nights.isnumeric():
        num_nights = int(num_nights)
        break
    else:
        print("Please type a number")

# Ensure user input is numerical for number or car rental days
while True:
    rental_days = input("Number of days to rent a car:\t")
    if rental_days.isnumeric():
        rental_days = int(rental_days)
        break
    else:
        print("Please type a number")

# Display all information in a readable format
print("-"*50)
print(f"Plane to {city_flight}: \t£{"%.2f" % plane_cost(city_flight)}"
      f"\nHotel for {num_nights} nights: \t£{ "%.2f" % hotel_cost(num_nights)}"
      f"\nCar rental for {rental_days} days: "
        f"\t£{"%.2f" % car_rental(rental_days)}"
      f"\n\nHoliday Total: "
        f"£{" %.2f" % holiday_cost(plane_cost, hotel_cost, car_rental)}")
print("-"*50)
