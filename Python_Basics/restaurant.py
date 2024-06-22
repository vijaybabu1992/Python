'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a
method called describe_restaurant() that prints these two pieces of information, and a
method called open_restaurant() that prints a message indicating that the restaurant is
open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
'''

class Restaurant:

    def __init__(self,name,cuisine_type):
        '''Initialize Restaurant'''
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Describe Restaurant'''
        msg = f'{self.name} Restaurant serves delicious {self.cuisine_type} food'
        print(f'\n{msg}')

    def open_restaurant(self):
        '''Restaurant status'''
        msg = f'{self.name} Restaurant is open to serve {self.cuisine_type} food. Come on in...!'
        print(f'\n {msg}')

''' We are calling the function here'''

restaurant = Restaurant('the food factory','Chinese')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.open_restaurant()
restaurant.describe_restaurant()


''' We are gonna create couple of instances'''

restaurant_01 = Restaurant('pradise','hyderabadi')

print(restaurant_01.name)
print(restaurant_01.cuisine_type)

restaurant_01.describe_restaurant()
restaurant_01.open_restaurant()

