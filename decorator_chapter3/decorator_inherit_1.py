##########################################
#decorator_inherit_1.py
# 使用继承: 4种咖啡继承自抽象基类饮料类
# 出现问题：当咖啡加入各种调料后，需要维护的类的数量几何数增加。当咖啡或调料价格变化使，需要维护修改的价格太多，软件设计缺乏弹性.
##########################################


class Beverage():

	def __init__(self):
		self.description = "unknown beverage"

	def getDescription(self):
		return self.description

	def cost(self):
		return 0

class HouseBlend(Beverage):
	def __init__(self, desc, price):
		self.description = desc
		self.price = price

	def cost(self):
		return self.price

class DarkRoast(Beverage):
	def __init__(self, desc, price):
		self.description = desc
		self.price = price

	def cost(self):
		return self.price

class Decaf(Beverage):
	def __init__(self, desc, price):
		self.description = desc
		self.price = price

	def cost(self):
		return self.price

class Espresso(Beverage):
	def __init__(self, desc, price):
		self.description = desc
		self.price = price

	def cost(self):
		return self.price



if __name__ == '__main__':
	hb = HouseBlend("House Blend!", 10)
	dr = DarkRoast("Dark Roast!", 20)
	decaf = Decaf("Decaf", 30)
	esp = Espresso("Espresso", 40)

	for item in [hb, dr, decaf, esp]:
		print(item.__class__.__name__ + " is: " + item.getDescription())
		print(item.__class__.__name__ + " price is: " + str(item.cost()))