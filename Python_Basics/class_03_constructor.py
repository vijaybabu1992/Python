# class Test:
#     def __init__(self):
#         print('constructor') # to declare and initialize instance variables
#
#
# t1 = Test()
# t2 = Test()
# t3 = Test()

# #----------------------------------------
#
# class Student:
#     def __init__(self,name,rollno,marks):
#         '''
#         Creating instance variable and performing initialization -- constructor
#         We should take min one argument compulsory in constructor which is 'self' and max no limit
#         '''
#
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#
# s1 = Student('bunny',100,900)
# s2 = Student('sunny',101,950)
# print(s1.name,s2.name)


#----------------------------------------

# class Test:
#     '''Constructor is always optional it's not mandatory'''
#
#     def m1(self):
#         print('method')
#
# t1 = Test
# t1.m1('hi')

#---------------------------
#
# class Test:
#     def __init__(self):
#         print('constructor Execution')
#
# t = Test()
# t.__init__()
# t.__init__()

#------------------------
# Over loading Methods
#--------------------------
# class Test:
#     def __init__(self):
#         print('no_arg_constructor')
#
#     def __init__(self, x):
#         print('One-arg constructor')   # It always considers the last argument, while giving the same constructor multiple times
#
# ##t1 = Test()
# t2 = Test(3)


'''
1. Constructor is a special method in python
2. The name of the constructor is always: __init__
3. We are not required to call constructor explicitly. Whenever we are creating an object,
automatically constructor will be executed.
4. Per object constructor will be executed only once.
5. The main purpose of constructor is to declare and initialize instance variables.
6. Constructor can take atleast one argument.(self)
7. Within the class constructor is optional, If we are not writing constructor, they python will provide default constructor.
8. Based on our requirement we can call constructor explicitly, then it will executed just like a normal method.
9. Overloading concept is not applicable for constructors within the same class. If we are trying to define multiple
constructors, only last constructor will be considered.
'''
