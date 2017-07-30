######################################
# pizza_store_notype.py
# 在此例中皮萨不分种类
######################################

import time

class Pizza(object):
	def __init__(self, size=9):
		self.size = size

	def prepare(self, flour=False, vegetables=False):
		if not flour:
			print("Pizza is lack of flour, need to be prepared!")
			exit(1)
		elif not vegetables:
			print("Pizza is lack of vegetables, need to be prepared!")
			exit(1)
		else:
			print("All things are ready, begin to do pizza!")


	#  /* fire = 100degree; time = 10min */
	def bake(self, fire, duration):
		for minute in range(duration):
			time.sleep(10)
			print("Bake {0} min...".format(minute+1))

		print("Pizza is baked with {0} degree {1} min. ".format(fire, duration))

	#/* num = 6 piece */
	def cut(self, num):
		print("Pizza is cut with {0} pieces. ".format(num))


	def box(self):
		print("Pizza is boxed already!")


if __name__ == '__main__':
	pi = Pizza(12)       ## 当皮萨分种类后，每次生成皮萨实例，就会生成很多皮萨对象。

	pi.prepare(True, True)
	pi.bake(200, 15)
	pi.cut(10)
	pi.box()