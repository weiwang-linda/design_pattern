#####################################################
# pizza_ingredient_factory.py
# 
#####################################################

from abc import ABCMeta, abstractmethod
from pizza_ingredient import *

## 皮萨原料家族---抽象工厂
class PizzaIngredientFactory(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.dough = None
		self.sauce = None
		self.cheese = None
		self.veggies = []
		self.pepperoni = None
		self.clam = None

	@abstractmethod
	def createDough(self):
		pass

	@abstractmethod
	def createSauce(self):
		pass

	@abstractmethod
	def createCheese(self):
		pass

	@abstractmethod
	def createVeggies(self):
		pass

	@abstractmethod
	def createPepperoni(self):
		pass

	@abstractmethod
	def createClam(self):
		pass

## 具体的纽约皮萨原料工厂
class NYPizzaIngredientFactory(PizzaIngredientFactory):
	def createDough(self):
		self.dough = ThinCrustDough()

	def createSauce(self):
		self.sauce = MarinaraSauce()

	def createCheese(self):
		self.cheese = ReggianoCheese()

	def createVeggies(self):
		self.veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]

	def createPepperoni(self):
		self.pepperoni = SlicedPepperoni()

	def createClam(self):
		self.clam = FreshClams()

## 具体的芝加哥皮萨原料工厂
class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
	def createDough(self):
		self.dough = ThickCrustDough()

	def createSauce(self):
		self.sauce = PlumTomatoSauce()

	def createCheese(self):
		self.cheese = MozzarellaCheese()

	def createVeggies(self):
		self.veggies = [Spinach(), BlackOlives(), EggPlant()]

	def createPepperoni(self):
		self.pepperoni = SlicedPepperoni()

	def createClam(self):
		self.clam = FrozenClams()