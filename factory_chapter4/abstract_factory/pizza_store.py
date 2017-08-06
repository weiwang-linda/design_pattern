#########################################
# pizza_store.py
#
#########################################

from abc import ABCMeta, abstractmethod
from pizza_basic import *
from pizza_ingredient_factory import *

class PizzaStore(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.pi = None

	@abstractmethod
	def createPizza(self, type):
		pass

	def orderPizza(self, type):
		self.pi = self.createPizza(type)

		self.pi.prepare()
		self.pi.bake()
		self.pi.cut()
		self.pi.box()

class NYPizzaStore(PizzaStore):
	def __init__(self):
		super(NYPizzaStore, self).__init__()
		self.factory = NYPizzaIngredientFactory()

	def createPizza(self, type):
		if type == "cheese":
			return CheesePizza(self.factory)
		elif type == "veggie":
			return VeggiePizza(self.factory)
		elif type == "clam":
			return ClamPizza(self.factory)
		elif type == "pepperoni":
			return PepperoniPizza(self.factory)

class ChicagoPizzaStore(PizzaStore):
	def __init__(self):
		super(ChicagoPizzaStore, self).__init__()
		self.factory = ChicagoPizzaIngredientFactory()

	def createPizza(self, type):
		if type == "cheese":
			return CheesePizza(self.factory)
		elif type == "veggie":
			return VeggiePizza(self.factory)
		elif type == "clam":
			return ClamPizza(self.factory)
		elif type == "pepperoni":
			return PepperoniPizza(self.factory)


if __name__ == '__main__':
	nyps = NYPizzaStore()
	nyps.orderPizza("cheese")

	ccps = ChicagoPizzaStore()
	ccps.orderPizza("clam")