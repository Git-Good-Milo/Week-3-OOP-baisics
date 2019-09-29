from animal_class import *
class Reptile(Animal):  # Inheritance
                        # It will run all the same methods as Animal
                        # Because that is all it knows
    # We can add our own  __init__ using def __init__.
    def __init__(self, name, teeth, looking_pretty, number_of_hearts, camo, eyes = 2):
        # Runs the __init__ in the parent class. In this case animal_calss
        super().__init__(name, teeth, looking_pretty, eyes)
        self.number_h = number_of_hearts
        self.camoflage = camo
        # The above metho overides the previous init method. However, the super call the previous init method so our object does have all of the           previous characteristices
        # AND THEN!!! We add more characterisitics
    # You can overide Methods from the parent class. This is called Polymorphisium
    def eat(self, food = 'bugs'):
        return 'OMG THESE things are soooo delicious! WHat are they called? ' + food

    # Adding a new method to this class ( Ploymorphing)
    def seek_heat(self, cool, mega, swag):
        return 'My gosh this is a bit chilly wot wot! Said the posh Reptile. I need to find some warmth old boy!' + cool + mega + ': ' + swag