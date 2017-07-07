##########
# ******** Simulate Ducks game ********
##########
# Using interface to make some ducks can fly or some ducks can quack.

#Superclass
class Duck():
    def __init__(this, mode):
    	this.mode = mode

    def swim(this):
        print(this.__class__.__name__ + ": Swim in a pool")

    def display(this):       #This method can be reload in subclass.
        pass

#interface
class Flyable():
    def fly(this):
        print(this.__class__.__name__ + ": fly in the sky")


class Quackable():
    def quack(this):
        print(this.__class__.__name__ + ": Ga Ga Ga")


#subclass
class MallardDuck(Duck,Flyable,Quackable):
    def display(this):       #Green head
        print(this.__class__.__name__ + ": display as " + this.mode)


class RedheadDuck(Duck,Flyable,Quackable):
    def display(this):       #Red head
        print(this.__class__.__name__ + ": display as " + this.mode)


class RubberDuck(Duck,Quackable):
    def quack(this):         #squeak
	    print(this.__class__.__name__ + ": Zi Zi Zi")
    def display(this):       #Rubber
        print(this.__class__.__name__ + ": display as " + this.mode)


class DecoyDuck(Duck):
	def display(this):       #Decoy, wooden
	    print(this.__class__.__name__ + ": display as " + this.mode)



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