##########
# ******** Simulate Ducks game ********
##########
# Add setter method to change duck's behavier on runtime


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

# Add new fly behavier
class FlyRocketPowered(FlyBehavier):
	def __init__(self):
		print("FlyBehavier-FlyRocketPowered")

	def fly(self):
		print("I'm flying with a rocket!")

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

	# add setter method
	def setFlyBehavier(self, fb):
		self.flyBehavier = fb                #fb is FlyBehavier instance

	def setQuackBehavier(self, qb):
		self.quackBehavier = qb              #qb is QuackBehavier instance

	def swim(self):
		print("Swim in a pool")

	def display(self):
		pass

class MallardDuck(Duck):
	def __init__(self, mode):
		self.mode = mode
		self.flyBehavier = FlyWithWings()        #instance fly behavier class for duck subclass
		self.quackBehavier = Quack()             #instance quack behavier class for duck subclass

	def display(self):
		print(self.__class__.__name__ + ": display as " + self.mode)


# Add a new duck class --- ModelDuck
class ModelDuck(Duck):
	def __init__(self, mode):
		self.mode = mode
		self.flyBehavier = FlyNoWay()
		self.quackBehavier = Quack()

	def display(self):
	    print(self.__class__.__name__ + ": display as " + self.mode)

if __name__ == '__main__':
	mallard = MallardDuck("Mallard")
	model = ModelDuck("Model")

	mallard.display()
	mallard.performFly()
	mallard.performQuack()
	mallard.swim()

	model.display()
	model.performFly()                          #FlyBehavier instance FlyNoWay is set at ModelDuck's __init__()
	model.setFlyBehavier(FlyRocketPowered())    #setter function can change the FlyBehavier on runtime  
	model.performFly()