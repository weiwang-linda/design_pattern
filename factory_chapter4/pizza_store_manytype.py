#################################################
# pizza_store_manytype.py
# 
# 当皮萨店有更多种类皮萨时，需要根据类型制造出皮萨。
#################################################

import time

from abc import ABCMeta, abstractmethod
from pizza_basic import CheesePizza, GreekPizza, PepperoniPizza


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