###################################################################################
# coffestore_size_decorator.py
# 新需求：
# 	1. 在菜单上加上咖啡的容量大小，供顾客选择小杯（tall）、中杯（grande）、大杯（venti）
# 	2. 任何咖啡都必须具备容量大小，也希望调料根据咖啡容量收费。
###################################################################################


from abc import ABCMeta, abstractmethod

class Beverage(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.description = "Unknown Beverage"
		self.size = "grande"

	def getDescription(self):
		return self.description

	def getSize(self):
		return self.size

	def setSize(self, se):
		self.size = se

	@abstractmethod
	def cost(self):
		pass

class CondimentDecorator(Beverage):
	__metaclass__ = ABCMeta

	@abstractmethod
	def getDescription(self):
		pass

class SizeDecorator(Beverage):
	__metaclass__ = ABCMeta

	@abstractmethod
	def getDescription(self):
		pass

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

	def getSize(self):
		return self.beverage.getSize()

	def cost(self):
		cost = self.beverage.cost()
		if self.getSize() == 'tall':
			return cost + 0.10
		elif self.getSize() == 'grande':
			return cost + 0.15
		elif self.getSize() == 'venti':
			return cost + 0.20

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

	be.setSize('venti')
	be = Soy(be)
	print(be.getDescription() + " $" + str(be.cost()))