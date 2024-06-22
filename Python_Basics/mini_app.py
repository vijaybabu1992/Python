# class Movie:
#     '''This is a class developed by vijay for Movie'''
#
#     def __init__(self,x,y,z):
#         '''x, y, z -- temporary variables to hold the arguments -- local variables
#         -- recommended to use same values(title, hero, heroine) for local variables x,y,z'''
#         self.title = x
#         self.hero = y
#         self.heroine = z
#
#
# movie = Movie('Bahubali','prabas','anuska')
#
# print(movie.title)

#--------------------------------------------------
class Movie:
    '''This is a class developed by vijay for Movie'''

    def __init__(self,title, hero, heroine):
        '''x, y, z -- temporary variables to hold the arguments -- local variables
        -- recommended to use same values(title, hero, heroine) for local variables x,y,z'''
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print('Movie Name: ', self.title)
        print('Hero Name: ', self.hero)
        print('Heroine Name: ', self.heroine)


list_movies = []

while True:
    title = input('Enter Movie Name:')
    hero = input('Enter Hero Name:')
    heroine = input('Enter Heroine Name:')
    m = Movie(title,hero,heroine)
    list_movies.append(m)
    print('Movie added Successfully')
    option = input('Do you want to add one more Movie(YES/NO): ')
    if option.upper() == 'YES':
        continue
    elif option.upper() == 'NO':
        break
    else:
        print('Please Enter Yes or No')
        option = input('Do you want to add one more Movie(YES/NO): ')

print('All Movies Information.......\n')
print('-'*100)
for movie in list_movies:
    movie.info()
    print('-'*100)

