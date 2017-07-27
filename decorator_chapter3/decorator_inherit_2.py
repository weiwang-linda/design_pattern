############################################
#decorator_inherit_2.py
# 使用继承：给4种咖啡加入不同的调料。
# 解决问题：解决了第一个问题，只需要5个类就覆盖了之前方法的几何基数增加的类。
# 出现问题: 但当调料价格变化会使我们更改现有的代码。新调料出现，须更改Beverage类代码。新的饮料继承了不合适的方法。双倍调料如何解决。
############################################


# ********** base class : Beverage *********** #
class Beverage(object):

	def __init__(self):
		self.description = 'Unknown Beverage'
		self.milk = False
		self.soy = False
		self.mocha = False
		self.whip = False

	def getDescription(self):
		return self.description

	def cost(self):
		condimentCost = 0.0
		if(self.hasMilk()):
			condimentCost += 0.6
		if(self.hasSoy()):
			condimentCost += 0.7
		if(self.hasMocha()):
			condimentCost += 0.8
		if(self.hasWhip()):
			condimentCost += 0.9
		return condimentCost

	def hasMilk(self):
		return self.milk

	def setMilk(self, val):
		self.milk = val

	def hasSoy(self):
		return self.soy

	def setSoy(self, val):
		self.soy = val

	def hasMocha(self):
		return self.mocha

	def setMocha(self, val):
		self.mocha = val

	def hasWhip(self):
		return self.whip

	def setWhip(self, val):
		self.whip = val

# **************** Derived class: 4 cafes ******************* #
class HouseBlend(Beverage):
	def __init__(self, desc):
		super(HouseBlend, self).__init__()        # 注意super的用法，在新式类中，遵循MRO
		self.description = desc

	def cost(self):
		return 10 + super(HouseBlend,self).cost()

class DarkRoast(Beverage):
	def __init__(self, desc):
		super(DarkRoast, self).__init__()
		self.description = desc

	def cost(self):
		return 20 + super(DarkRoast,self).cost()

class Decaf(Beverage):
	def __init__(self, desc):
		super(Decaf, self).__init__()
		self.description = desc

	def cost(self):
		return 20 + super(Decaf,self).cost()

class Espresso(Beverage):
	def __init__(self, desc):
		super(Espresso, self).__init__()
		self.description = desc

	def cost(self):
		return 20 + super(Espresso,self).cost()


if __name__ == '__main__':
	hb = HouseBlend("HouseBlend")
	hb.setMilk(True)
	dr = DarkRoast("DarkRoast")
	dr.setWhip(True)
	dr.setMilk(True)
	df = Decaf("Decaf")
	df.setMocha(True)
	ep = Espresso("Espresso")
	ep.setSoy(True)

	for item in [hb, dr, df, ep]:
		print(item.__class__.__name__ + " is: " + item.getDescription())
		print(item.__class__.__name__ + " price is: " + str(item.cost()))