class Animal:

    def is_mammal(self):
        return None

    
class Duck(Animal):

    def quack(self):
        print('quack')

    def is_mammal(self):
        return False
    



my_duck = Duck()
my_duck.quack()