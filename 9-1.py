class Restaurant():
    def __init__(self, restaurant_name, 
                cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant is " + self.restaurant_name + 
        " and the cuisine is " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant('Saffron', 'Butter Chicken')
print("The restaurant is " + restaurant.restaurant_name
+ " and the cuisine is " + restaurant.cuisine_type + ".")

restaurant.describe_restaurant()
restaurant.open_restaurant()