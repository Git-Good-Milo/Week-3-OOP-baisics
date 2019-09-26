class Animal():

    # Charateristics
    def __init__(self, name, teeth, looking_pretty, eyes = 2): # runs only once when you initilise an object
        self.name = name
        self.number_eyes = eyes
        self.number_of_teeth = teeth
        self.alive = True
        self.colour = looking_pretty
        self.age = 0


    # Methods -  functions that can only be used on this classes instance

    # Behaviours - functions that belong to a class.
    def eat(self, food):
        return 'NOM NOM NOM NOM' + ' ' + food

    def sleep(self):
        return 'ZZZZZZZZZZZ zzz zz zzzzz'

    def hunt(self, tasty_things):
        return 'ATTTAAAAACKKK This is sparta!!!' + ' ' + tasty_things

    def potty(self):
        return 'aghghaghghaghaghgahgahghg ahhhhhhhhhh (big BIG splash)'

    def play(self):
        return 'I can have fun by myself!'

# Lets create an object of class Animal
    # Also known as initialising an object
# my_animal = Animal() #this is where i created an instance of class Animal
# print(my_animal)
# print(type(my_animal))