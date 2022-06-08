def build_car(manufacturer, model, **car_info):
       """Build a dictionary containing everything we know about a car."""
       profile = {}
       profile['manufacturer_name'] = manufacturer
       profile['model_name'] = model
       for key, value in car_info.items():
              profile[key] = value
       return profile

car_profile = build_car('Ford', 'Ecosport', seating='5', fuel='diesel', price='Rs 8,20,000')
print(car_profile)
