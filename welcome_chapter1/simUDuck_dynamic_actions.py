##########
# ******** Simulate Ducks game ********
##########
# Using absctract basic class to implay interface of program, so make the Duck actions are dynamic changed while runtime.


# 2 abstract base classes:
# one is fly behavier class
# another is quack behavier class
from abc import ABCMeta, abstractmethod

class FlyBehavier():
	__metaclass__ = ABCMeta

	@abstractmethod
	def fly(self):
		pass                  #abstract

class QuackBehavier():
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self):
    	pass                  #abstract

# 6 reherit classes
class FlyWithWings(FlyBehavier):
	def __init__(self):
		print("FlyBehavier-FlyWithWings")

	def fly(self):                 #give actual code for abstract method reherit from abstract class
		print("I am flying!...")

class FlyNoWay(FlyBehavier):
	def __init__(self):
		print("FlyBehavier-FlyNoWay")

	def fly(self):
		print("I can not fly!...")

class Quack(QuackBehavier):
	def __init__(self):
		print("QuackBehavier-Quack")

	def quack(self):
		print("Quack")

class Squeak(QuackBehavier):
	def __init__(self):
		print("QuackBehavier-Squeak")
	    
	def quack(self):
		print("Squeak")

class MuteQuack(QuackBehavier):
	def __init__(self):
		print("QuackBehavier-MuteQuack")

	def quack(self):
		print("MuteQuack")

# base class Duck, reherit from 2 abstract base classes
class Duck(FlyBehavier,QuackBehavier):
	def __init__(self):
		self.flyBehavier = None
		self.quackBehavier = None

	def performFly(self):
		self.flyBehavier.fly()               #delegate var for fly behavier

	def performQuack(self):
		self.quackBehavier.quack()           #delegate var for quack behavier

	def swim(self):
		print(self.__class__.__name__ + ": Swim in a pool")

	def display(self):
		pass

class MallardDuck(Duck):
	def __init__(self, mode):
		self.mode = mode
		self.flyBehavier = FlyWithWings()        #instance fly behavier class for duck subclass
		self.quackBehavier = Quack()             #instance quack behavier class for duck subclass

	def display(self):
		print(self.__class__.__name__ + ": display as " + self.mode)

class RedheadDuck(Duck):
	def __init__(self, mode):
		self.mode = mode
		self.flyBehavier = FlyWithWings()
		self.quackBehavier = Quack()

	def display(self):
		print(self.__class__.__name__ + ": display as " + self.mode)


class RubberDuck(Duck):
	def __init__(self, mode):
		self.mode = mode
		self.flyBehavier = FlyNoWay()
		self.quackBehavier = Squeak()

	def display(self):       #Rubber
		print(self.__class__.__name__ + ": display as " + self.mode)


class DecoyDuck(Duck):
	def __init__(self, mode):
		self.mode = mode
		self.flyBehavier = FlyNoWay()
		self.quackBehavier = MuteQuack()

	def display(self):       #Decoy, wooden
	    print(self.__class__.__name__ + ": display as " + self.mode)

if __name__ == '__main__':
	mallard = MallardDuck("Mallard")
	red = RedheadDuck("Redhead")
	rubber = RubberDuck("Rubber")
	decoy = DecoyDuck("Decoy")

	mallard.display()
	mallard.performFly()
	mallard.performQuack()
	mallard.swim()

	red.display()
	red.performFly()
	red.performQuack()
	red.swim()

	rubber.display()
	rubber.performFly()
	rubber.performQuack()
	rubber.swim()

	decoy.display()
	decoy.performFly()
	decoy.performQuack()
	decoy.swim()