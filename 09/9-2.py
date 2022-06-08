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

restaurant1 = Restaurant('Saffron', 'Butter Chicken')
restaurant2 = Restaurant('BM dhaba', 'Chicken dry fry')
restaurant3 = Restaurant('Pakghor', 'Chicken chowmein')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()