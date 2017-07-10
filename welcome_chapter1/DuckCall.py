##########
# ******** Device Duck Call ********
##########
# Cannot reherit from Duck class
# Can simulate duck quack
# Cannot fly


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


class DuckCall(FlyBehavier, QuackBehavier):
	def __init__(self, mode):
		self.mode = mode
		self.flyBehavier = FlyNoWay()        #instance fly behavier class for duck subclass
		self.quackBehavier = Quack()             #instance quack behavier class for duck subclass

	def performFly(self):
		self.flyBehavier.fly()

	def performQuack(self):
		self.quackBehavier.quack()

	def display(self):
		print(self.__class__.__name__ + ": display as " + self.mode)


if __name__ == '__main__':
	duckcall = DuckCall("DuckCall")

	duckcall.display()
	duckcall.performFly()
	duckcall.performQuack()