# class Test:
#     '''This class developed by vijay'''
#     def __init__(self):
#         ## __init__ is a constructor
#         # self is a reference variable, which is always falling into current object
#
#         pass
#
#
# k = Test()
# #print(k)
# print(id(k))

#--------------------------------------------
# class Test:
#     '''This class developed by vijay'''
#
#     def __init__(self):
#         print('Address of Object pointed by self: ',id(self))
#
#
# k = Test()
# # print(k)
# print('Address of object pointed by k',id(k))

#---------------------------------------------------------------

# class Test:
#     def __init__(self):
#         print('constructor')
#
#     def fun1(self,x):
#         print('x value',x)
#
# k = Test()
# k.fun1(5)

#------------------------------------------------------------
# class Student:
#     def __init__(self, name, rollno, marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#
#     def talk(self):
#         print('Hello Everyone: \n\tI am ',self.name)
#         print('\tMy Rollno: ',self.rollno)
#         print('\tMy Total Marks: ',self.marks)
#
# s1 = Student('Nani','10001','550')
# s1.talk()

#----------------------------------------------------

class Student:
    def __init__(delf, name, rollno, marks):
        delf.name = name
        delf.rollno = rollno
        delf.marks = marks

    def talk(celf):
        print('Hello Everyone: \n\tI am ',celf.name)
        print('\tMy Rollno: ',celf.rollno)
        print('\tMy Total Marks: ',celf.marks)

s1 = Student('sunny','10001','550')
s1.talk()