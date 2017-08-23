##################################
# singleton_basic_1.py
# 存储在类属性中，通过类方法去获取。
##################################

class Singleton(object):
	__uniqueInstance = None

	@classmethod
	def getInstance(cls, *args, **kwargs):
		if cls.__uniqueInstance is None:
			cls.__uniqueInstance = cls(*args, **kwargs)
		return cls.__uniqueInstance


if __name__ == '__main__':
	a = Singleton.getInstance()
	b = Singleton.getInstance()
	assert id(a) == id(b)