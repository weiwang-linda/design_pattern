#######################################
# singleton_basic_2.py
# 在类的 __new__ 方法中判断
#######################################

class Singleton:
	__uniqueInstance = None

	def __new__(cls, *args, **kwargs):
		if Singleton.__uniqueInstance is None:
			Singleton.__uniqueInstance = object.__new__(cls, *args, **kwargs)
		return Singleton.__uniqueInstance


if __name__ == '__main__':
	a = Singleton()
	b = Singleton()
	assert id(a) == id(b)