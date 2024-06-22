'''
9-3. Users: Make a class called User. Create two attributes called first_name and
last_name, and then create several other attributes that are typically stored in a user
profile. Make a method called describe_user() that prints a summary of the user’s
information. Make another method called greet_user() that prints a personalized
greeting to the user.
Create several instances representing different users, and call both methods for each
user.
'''

class User:

    def __init__(self,first_name,last_name,address,pincode):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.pincode = pincode

    def describe_user(self, age):
        ''' describing user detils'''
        print(f'first_name: {(self.first_name).upper()}\n last_name: {self.last_name}\n address: {self.address} \n pincode: {self.pincode}')

        return  f"{self.first_name}'s age is {age}"

    def greet_user(self):
        '''Greet the user'''
        return f"Hello Mr.{self.first_name} {self.last_name} ............!"


#--------------------------------------------------------------------
# Calling the class

user1 = User('Vijay','Babu','Chirala',523157)

print(user1.describe_user(31))

print(user1.greet_user())

print('\n\n')
user2 = User('Srinu','D','kakinada',523155)

print(user2.greet_user())
print(user2.describe_user(16))
