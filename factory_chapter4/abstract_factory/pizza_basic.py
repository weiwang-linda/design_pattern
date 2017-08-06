############################################
# pizza_basic.py
# 
############################################

from abc import ABCMeta, abstractmethod

class Pizza(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.name = None
		self.dough = None
		self.sauce = None
		self.veggies = []
		self.cheese = None
		self.pepperoni = None
		self.clam = None

	@abstractmethod
	def prepare(self):
		pass

	def bake(self):
		print("Bake for 25 minutes at 350")

	def cut(self):
		print("Cutting the pizza into diagonal slices")

	def box(self):
		print("Place pizza in offical PizzaStore box")

class CheesePizza(Pizza):

	def __init__(self, ingredientFactory):
		super(CheesePizza, self).__init__()
		self.factory = ingredientFactory

	def prepare(self):
		print("Preparing cheese pizza ")
		self.dough = self.factory.createDough()
		self.sauce = self.factory.createSauce()
		self.cheese = self.factory.createCheese()

class ClamPizza(Pizza):

	def __init__(self, ingredientFactory):
		super(ClamPizza, self).__init__()
		self.factory = ingredientFactory

	def prepare(self):
		print("Preparing cheese pizza ")
		self.dough = self.factory.createDough()
		self.sauce = self.factory.createSauce()
		self.cheese = self.factory.createCheese()
		self.clam = self.factory.createClam()