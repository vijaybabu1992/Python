class Student:
    '''This class developed by vijay'''
    def __init__(self):
        self.name = 'vijay'
        self.roll_no = 101
        self.course = 'BTech'

    def talk(self):
        print('Hello Everyone, My Name is: ', self.name)
        print('My Roll No is: ', self.roll_no)
        print('My course is: ', self.course)


# reference_variable = Classname()
s1 = Student()

print(s1.course)
print(s1.roll_no)
print(s1.name)
print('\n')
print(s1.talk())

# Part_02 --------------------------------------------------------------------

class Student:
    '''This class developed by vijay'''
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def talk(self):
        print('Hello Everyone,\nMy Name is: ', self.name)
        print('My Roll No is: ', self.roll_no)
        print('My course is: ', self.course)


# reference_variable = Classname()
# s1 = Student('pratap',102, 'Btech-Mech')
#
# print(s1.course)
# print(s1.roll_no)
# print(s1.name)
# print('\n')
# s1.talk()
#
# print('-'*100,'\n')
# s2 = Student('srinu',103,'Btech-ECE')
# print(s2.roll_no)
# print(s2.name)
# print(s2.course)
# print('-'*100,'\n')
# s2.talk()
