'''
99-4: Number Served
Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class. Print the number of customers the restaurant has served,
and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers that have been served.
Call this method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment the number of customers who've been served.
Call this method with any number you like that could represent how many customers were served in, say, a day of business.
'''

class Restaurant:

    def __init__(self,name,cuisine_type):
        '''Initialize Restaurant'''
        self.name = name.title()
        self.cuisine_type = cuisine_type
        #self.number_served = 0

    def describe_restaurant(self):
        '''Describe Restaurant'''
        msg = f'{self.name} Restaurant serves delicious {self.cuisine_type} food'
        print(f'\n{msg}')

    def open_restaurant(self):
        '''Restaurant status'''
        msg = f'{self.name} Restaurant is open to serve {self.cuisine_type} food. Come on in...!'
        print(f'\n {msg}')

    def no_of_serv(self,number_served):
        '''Number of people the restaurant served'''
        self.number_served = number_served
        #print('The no of people served is ',number_served)
        return f'The no of people served till now {self.number_served}'

''' We are calling the function here'''

# restaurant = Restaurant('the food factory','Chinese')
#
# print(restaurant.name)
# print(restaurant.cuisine_type)
#
# restaurant.open_restaurant()
# restaurant.describe_restaurant()
#
# restaurant.no_of_serv(10)
# print(f'No of people its served is {restaurant.number_served}')

''' We are gonna create couple of instances'''

# restaurant_01 = Restaurant('pradise','hyderabadi')
#
# print(restaurant_01.name)
# print(restaurant_01.cuisine_type)
#
# restaurant_01.describe_restaurant()
# restaurant_01.open_restaurant()

restaurant_02 = Restaurant('Udipi','South India')

print(restaurant_02.no_of_serv(5))

#print(f'testing with self {restaurant_02.number_served}')
