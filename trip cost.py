def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if "tokyo" == city:
        return 205
    elif "kyoto" == city:
        return 250
    elif "osaka" == city:
        return 300
    elif "hiroshima" == city:
        return 320
    elif "nagasaki" == city:
        return 350
def rental_car_cost(days):
    if days>=7:
        return 40*days - 50
    elif days>=3:
        return 40*days - 20
    else:
        return 40*days
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print("cost of rental car: ", rental_car_cost(6))
print("cost of plane ride (u prob booked economy): ", plane_ride_cost("tokyo"))
print("cost of hotel room: ", hotel_cost(7))
print("total cost of trip: ", trip_cost("tokyo",7,500))
print(trip_cost("kyoto",6,500))