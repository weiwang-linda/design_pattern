######################################################
# pizza_store_packagechanges.py
# 
# 将变化的部分和不变的部分分离出来，进行封装，从而实现对改变关闭。
# 变化的部分是创建对象，将其移到orderPizza函数之外，移到另一个对象中。由新对象专职创建对象。新对象就是工厂。
######################################################

from pizza_store_manytype import Pizza, CheesePizza, GreekPizza, PepperoniPizza

class SimplePizzaFactory():
	def __init__(self):
		self.pi = None

	def createPizza(self, type):
		## 从orderPizza()方法中移过来的代码。
		if type == "cheese":
			self.pi = CheesePizza()
		elif type == "greek":
			self.pi = GreekPizza()
		elif type == "pepperoni":
			self.pi = PepperoniPizza()
		# elif type == "clam":
		# 	self.pi = ClamPizza()
		# elif type == "veggie":
		# 	self.pi = VeggiePizza()
		return self.pi


class PizzaStore():
	def __init__(self, factory):
		self.factory = factory

	def orderPizza(self, type):
		pi = self.factory.createPizza(type)

		pi.prepare()
		pi.bake()
		pi.cut()
		pi.box()


if __name__ == '__main__':
	fc = SimplePizzaFactory()
	ps = PizzaStore(fc)
	ps.orderPizza("cheese")
	ps.orderPizza("greek")