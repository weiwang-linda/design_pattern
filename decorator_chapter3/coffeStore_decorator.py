##############################################
# coffeStore_decorator.py
# 使用装饰者的方式
##############################################

from abc import ABCMeta, abstractmethod

#所有咖啡的抽象基类，也是所有调料抽象基类的基类.
class Beverage(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.description = "Unknown Beverage"

	def getDescription(self):
		return self.description

	@abstractmethod
	def cost(self):
		pass

#所有装饰者抽象基类
class CondimentDecorator(Beverage):
	__metaclass__ = ABCMeta

	@abstractmethod
	def getDescription(self):
		pass

#实现具体咖啡类，每种咖啡都是一种饮料,都有自己的描述和价格。
class HouseBlend(Beverage):
	def __init__(self):
		self.description = "House Blend Coffee"

	def cost(self):
		return 0.89

class DarkRoast(Beverage):
	def __init__(self):
		self.description = "Dark Roast Coffee"

	def cost(self):
		return 0.99

class Espresso(Beverage):
	def __init__(self):
		self.description = "Espresso Coffee"

	def cost(self):
		return 1.99

class Decaf(Beverage):
	def __init__(self):
		self.description = "Decaf Coffee"

	def cost(self):
		return 1.05


# 实现具体装饰者调料类
class Mocha(CondimentDecorator):
	def __init__(self, bever):
		self.beverage = bever

	def getDescription(self):
		return self.beverage.getDescription() + ", Mocha"

	def cost(self):
		return self.beverage.cost() + 0.20

class Milk(CondimentDecorator):
	def __init__(self, bever):
		self.beverage = bever

	def getDescription(self):
		return self.beverage.getDescription() + ", Milk"

	def cost(self):
		return self.beverage.cost() + 0.30

class Soy(CondimentDecorator):
	def __init__(self, bever):
		self.beverage = bever

	def getDescription(self):
		return self.beverage.getDescription() + ", Soy"

	def cost(self):
		return self.beverage.cost() + 0.40


class Whip(CondimentDecorator):
	def __init__(self, bever):
		self.beverage = bever

	def getDescription(self):
		return self.beverage.getDescription() + ", Whip"

	def cost(self):
		return self.beverage.cost() + 0.50


if __name__ == "__main__":
	be = Espresso()
	print(be.getDescription() + " $" + str(be.cost()))

	be = Mocha(be)
	be = Whip(be)
	be = Mocha(be)

	print(be.getDescription() + " $" + str(be.cost()))