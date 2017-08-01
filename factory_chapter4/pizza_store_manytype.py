#################################################
# pizza_store_manytype.py
# 
# 当皮萨店有更多种类皮萨时，需要根据类型制造出皮萨。
#################################################

import time

from abc import ABCMeta, abstractmethod

class Pizza(object):
	__metaclass__ = ABCMeta

	## 所有类型皮萨都必须实现Pizza接口.
	@abstractmethod
	def __init__(self):
		pass

	def prepare(self):
		print(self.__class__.__name__ + " is prepared well!")

	def bake(self):
		print(self.__class__.__name__ + " is baked well!")

	def cut(self):
		print(self.__class__.__name__ + " is cut!")

	def box(self):
		print(self.__class__.__name__ + " is boxed already!")

class CheesePizza(Pizza):
	def __init__(self):
		super(CheesePizza, self).__init__()
		self.cheese = 0.5

class GreekPizza(Pizza):
	def __init__(self):
		super(GreekPizza, self).__init__()


class PepperoniPizza(Pizza):
	def __init__(self):
		super(PepperoniPizza, self).__init__()
		self.pepper = 0.1


if __name__ == '__main__':

	def orderPizza(type):
		## 这里是变化的部分，皮萨店菜单改变，这里一定会一改再改。
		if type == "cheese":
			pi = CheesePizza()
		elif type == "greek":
			pi = GreekPizza()
		elif type == "pepperoni":
			pi = PepperoniPizza()

		## 以下是不想改变的地方
		pi.prepare()
		pi.bake()
		pi.cut()
		pi.box()

	orderPizza("cheese")
	orderPizza("greek")
	orderPizza("pepperoni")