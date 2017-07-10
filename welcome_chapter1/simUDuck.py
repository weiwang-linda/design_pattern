##########
# ******** Simulate Ducks game ********
##########
# All kinds of ducks in the game will as swim as quack

#Superclass
class Duck():
	def __init__(self, mode):
		self.mode = mode

	def quack(self):
		print(self.__class__.__name__ + ": Ga Ga Ga")

	def swim(self):
		print(self.__class__.__name__ + ": Swim in a pool")

	def display(self):       #self method can be reload in subclass.
	    pass



#subclass
class MallardDuck(Duck):
    def display(self):      #Green head
        print(self.__class__.__name__ + ": display as " + self.mode)


class RedheadDuck(Duck):
    def display(self):       #Red head
        print(self.__class__.__name__ + ": display as " + self.mode)


if __name__ == '__main__':
    greenduck = MallardDuck("Mallard")
    redduck = RedheadDuck("Redhead")

    greenduck.quack()
    greenduck.swim()
    greenduck.display()

    redduck.quack()
    redduck.swim()
    redduck.display()