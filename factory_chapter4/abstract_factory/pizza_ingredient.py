####################################################
# pizza_ingredient.py
# 
####################################################

class Dough(object):
	def __init__(self):
		print("Dough")

class ThinCrustDough(Dough):
	def __init__(self):
		print("ThinCrustDough")

class ThickCrustDough(Dough):
	def __init__(self):
		print("ThickCrustDough")


class Sauce(object):
	def __init__(self):
		print("Sauce")

class MarinaraSauce(Sauce):
	def __init__(self):
		print("MarinaraSauce")

class PlumTomatoSauce(Sauce):
	def __init__(self):
		print("PlumTomatoSauce")


class Cheese(object):
	def __init__(self):
		print("Cheese")

class ReggianoCheese(Cheese):
	def __init__(self):
		print("ReggianoCheese")

class MozzarellaCheese(Cheese):
	def __init__(self):
		print("MozzarellaCheese")


class Clams(object):
	def __init__(self):
		print("Clams")

class FreshClams(Clams):
	def __init__(self):
		print("FreshClams")

class FrozenClams(Clams):
	def __init__(self):
		print("FrozenClams")


class SlicedPepperoni(object):
	def __init__(self):
		print("SlicedPepperoni")