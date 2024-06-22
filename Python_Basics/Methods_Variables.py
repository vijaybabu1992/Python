# Instance method

# class Student:
# 	school_name='ZP High School'

# 	def __init__(self, name, rollno):
# 		self.name = name        # instance variables
# 		self.rollno = rollno    # instance variables
	
# 	def getstudentinfo(self):
# 		print('student name:',self.name)
# 		print('student rollno:',self.rollno)



# class method

# class Test:
# 	@classmethod
# 	def m1(cls):
# 		print(id(cls))

# print(id(Test))
# Test.m1()

#----------------------------------

'''
--Inside method if we are using only static variables and if we are not using any instance variables, 
then that method is no way related to particular object and it is class level method.
Such type of methods we have to declare as class methods.

--We have to declare class method with @classmethod decorator.
-- The first argument to the class method is always cls, which is reference variable to class object.
-- For every class one special object wil be created by PVM to maintain class level information, 
	which is nothing but class level object.cls is the reference variable pointing to the object.

''' 


# General utility method --> Static Method

# @staticmethod
# def getsum(a,b):
# 	return a+b


'''
Inside a method if we are not using any instance variable or static variable, 
such type of methods are general utility methods and these methods we have to declare as static methods.

Static methods should be declared by using @staticmethod decorator.

'''


#---------------------------------------------------


class Student:
	school_name='ZP High School'

	def __init__(self, name, rollno):
		self.name = name        # instance variables
		self.rollno = rollno    # instance variables
	
	def getstudentinfo(self):
		print('student name:',self.name)
		print('student rollno:',self.rollno)

	@classmethod
	def getschoolname(cls):
		print('School Name:', cls.school_name)

	@staticmethod
	def getsum(a,b):
		sum = a+b
		return sum

#------------------------------------------------------

		
