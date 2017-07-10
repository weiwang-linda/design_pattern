##########
# ******** Simulate Ducks game ********
##########
# Using interface to make some ducks can fly or some ducks can quack.

#Superclass
class Duck():
    def __init__(self, mode):
    	self.mode = mode

    def swim(self):
        print(self.__class__.__name__ + ": Swim in a pool")

    def display(self):       #self method can be reload in subclass.
        pass

#interface
class Flyable():
    def fly(self):
        print(self.__class__.__name__ + ": fly in the sky")


class Quackable():
    def quack(self):
        print(self.__class__.__name__ + ": Ga Ga Ga")


#subclass
class MallardDuck(Duck,Flyable,Quackable):
    def display(self):       #Green head
        print(self.__class__.__name__ + ": display as " + self.mode)


class RedheadDuck(Duck,Flyable,Quackable):
    def display(self):       #Red head
        print(self.__class__.__name__ + ": display as " + self.mode)


class RubberDuck(Duck,Quackable):
    def quack(self):         #squeak
	    print(self.__class__.__name__ + ": Zi Zi Zi")
    def display(self):       #Rubber
        print(self.__class__.__name__ + ": display as " + self.mode)


class DecoyDuck(Duck):
	def display(self):       #Decoy, wooden
	    print(self.__class__.__name__ + ": display as " + self.mode)



if __name__ == '__main__':
    greenduck = MallardDuck("Mallard")
    redduck = RedheadDuck("Redhead")
    rubberduck = RubberDuck("Rubber")
    decoyduck = DecoyDuck("Decoy")

    greenduck.quack()
    greenduck.swim()
    greenduck.display()
    greenduck.fly()

    redduck.quack()
    redduck.swim()
    redduck.display()
    redduck.fly()

    try:
        rubberduck.quack()
        rubberduck.swim()
        rubberduck.display()
        rubberduck.fly()
    except AttributeError as ae:
    	print(ae)
   

    try:
        decoyduck.quack()
    except AttributeError as ae:
    	print(ae)
    decoyduck.swim()
    decoyduck.display()
    try:
        decoyduck.fly()
    except AttributeError as ae:
    	print(ae)