##########################################
# pizza_basic.py
# 定义所有的pizza类, 包括基类，不同风味的皮萨。
##########################################

#/* pizza基类 */
class Pizza(object):
	"""All of the pizza has name, dough, sauce and toppings.
	All of the pizza has 4 processes: prepare, bake, cut, box."""

	def __init__(self):
		self.name = None        ## pizza的名字
		self.dough = None       ## pizza的面团类型
		self.sauce = None       ## pizza的酱料类型
		self.toppings = []      ## pizza的一套佐料

	def prepare(self):
		print("Preparing " + self.name)
		print("Tossing dough...")
		print("Adding sauce...")
		print("Adding toppings: ")
		for item in self.toppings:
			print(" " + item)

	def bake(self):
		print("Baking for 25 minutes at 350.")

	def cut(self):
		print("Cutting the pizza into diagonal slices")

	def box(self):
		print("Place pizza in offical PizzaStore box")

#/* Pizza子类 */
class CheesePizza(Pizza):
	def __init__(self):
		self.name = "Cheese Pizza"
		self.dough = "Common Dough"
		self.sauce = "Marinara Sauce"
		self.toppings = ["Cabbage","Cheese"]

class GreekPizza(Pizza):
	def __init__(self):
		self.name = "Greek Pizza"
		self.dough = "Common Dough"
		self.sauce = "Greek Sauce"
		self.toppings = ["Tommato","Greek"]

class PepperoniPizza(Pizza):
	def __init__(self):
		self.name = "Pepper on I Pizza"
		self.dough = "Common Dough"
		self.sauce = "Pepper Sauce"
		self.toppings = ["Tommato","Cabbage","Pepper"]

class NYStyleCheesePizza(Pizza):
	def __init__(self):
		self.name = "NY Style sauce and Cheese Pizza"
		self.dough = "Thin Crust Dough"
		self.sauce = "Marinara Sauce"
		self.toppings = ["Cabbage","Grated","Reggiano","Cheese"]

class NYStylePepperoniPizza(Pizza):
	def __init__(self):
		self.name = "NY Style sauce and Pepper Pizza"
		self.dough = "Thin Crust Dough"
		self.sauce = "Marinara Sauce"
		self.toppings = ["Tommato","Cabbage","Pepper","Grated","Reggiano"]

class ChicagoStyleCheesePizza(Pizza):
	def __init__(self):
		self.name = "Chicago Style Deep Dish Cheese Pizza"
		self.dough = "Extra Thick Crust Dough"
		self.sauce = "Plum Tomato Sauce"
		self.toppings = ["Cabbage","Shredded","Mozzarella","Cheese"]

	def cut(self):
		print("Cutting the pizza into square slices")

class ChicagoStylePepperoniPizza(Pizza):
	def __init__(self):
		self.name = "Chicago Style Deep Dish Pepper Pizza"
		self.dough = "Extra Thick Crust Dough"
		self.sauce = "Plum Tomato Sauce"
		self.toppings = ["Tommato","Cabbage","Pepper","Shredded","Mozzarella"]
