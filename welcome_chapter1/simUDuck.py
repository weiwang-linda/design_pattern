##########
# ******** Simulate Ducks game ********
##########
# All kinds of ducks in the game will as swim as quack

#Superclass
class Duck():
	def __init__(this, mode):
		this.mode = mode

	def quack(this):
		print(this.__class__.__name__ + ": Ga Ga Ga")

	def swim(this):
		print(this.__class__.__name__ + ": Swim in a pool")

	def display(this):       #This method can be reload in subclass.
	    pass



#subclass
class MallardDuck(Duck):
    def display(this):      #Green head
        print(this.__class__.__name__ + ": display as " + this.mode)


class RedheadDuck(Duck):
    def display(this):       #Red head
        print(this.__class__.__name__ + ": display as " + this.mode)


if __name__ == '__main__':
    greenduck = MallardDuck("Mallard")
    redduck = RedheadDuck("Redhead")

    greenduck.quack()
    greenduck.swim()
    greenduck.display()

    redduck.quack()
    redduck.swim()
    redduck.display()