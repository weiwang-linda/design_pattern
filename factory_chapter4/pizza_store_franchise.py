###########################################
# pizza_store_franchise.py
# 1. 扩大经营规模，创办皮萨加盟店，为保证质量希望加盟店使用总店的PizzaStore代码。
# 2. 加盟店受地点和口味影响，需要提供不同口味的皮萨。比如纽约风味皮萨，芝加哥风味皮萨。可以将皮萨工厂分类为制作不同风味皮萨的工厂。
# 3. 多一些质量控制，建立一个框架：加盟店和创建皮萨捆绑一起但又保持一定的弹性，比如烘培方法，是否切片，包装盒厂商。
# 解决方案：将创建皮萨抽象方法放入皮萨总店，具体实现在皮萨店的加盟店实现。即不再按皮萨工厂分类pizza，而是按皮萨店分类pizza了。
###########################################

from abc import ABCMeta, abstractmethod
from time import sleep
from pizza_basic import NYStyleCheesePizza, NYStylePepperoniPizza, ChicagoStyleCheesePizza, ChicagoStylePepperoniPizza

# /* Main pizza store */
class PizzaStore(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.pi = None

	@abstractmethod
	def createPizza(self, type):       ## 定义为抽象函数，在子类中具体实现，使得制作皮萨和订购皮萨过程解耦。
		pass                           ## 不同种类的皮萨制作过程不一样，但所有皮萨订购过程一样

	def orderPizza(self, type):
		self.pi = self.createPizza(type)
		self.pi.prepare()
		self.pi.bake()
		self.pi.cut()
		self.pi.box()

# /* Franchise pizza store */
class NYStylePizzaStore(PizzaStore):
	def createPizza(self, type):
		if type == "cheese":
			pi = NYStyleCheesePizza()
		elif type == "pepperoni":
			pi = NYStylePepperoniPizza()
		return pi

class ChicagoStylePizzaStore(PizzaStore):
	def createPizza(self, type):
		if type == "cheese":
			pi = ChicagoStyleCheesePizza()
		elif type == "pepperoni":
			pi = ChicagoStylePepperoniPizza()
		return pi


if __name__ == '__main__':

	## 客户决定皮萨的风味和类型,想要某种风味皮萨，需要到该风味的皮萨店订购。

	# /* 先找到某种风味的皮萨加盟店,然后订购某种类型皮萨. */
	nyps = NYStylePizzaStore()
	nyps.orderPizza("cheese")

	csps = ChicagoStylePizzaStore()
	csps.orderPizza("pepperoni")