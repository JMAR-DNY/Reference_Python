#calculates basic traval costs highlighting functions calling other functions

def hotel_cost(nights):
    return 140*nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return "Error"
        
def rental_car_cost(days):
    discount = 0
    cost_per_day = 40
    
    if days >=7:
        discount -=50
    elif days >=3:
        discount -=20
    
    return cost_per_day*days + discount
    
def trip_cost(city, days, spending_money):
    return rental_car_cost(days)+plane_ride_cost(city)+hotel_cost(days)+spending_money

print trip_cost("Los Angeles", 5, 600)
