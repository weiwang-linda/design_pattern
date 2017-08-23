############################################
# singleton_basic_3.py
# 根据书上的java代码改写
############################################

class Singleton(object):
	__uniqueInstance = None

	def __create(cls, *args, **kwargs):
		return object.__new__(cls, *args, **kwargs)

	@classmethod
	def getInstance(cls, *args, **kwargs):
		if cls.__uniqueInstance is None:
			cls.__uniqueInstance = cls.__create(cls, *args, **kwargs)
		return cls.__uniqueInstance


if __name__ == '__main__':
	a = Singleton.getInstance()
	b = Singleton.getInstance()
	print(id(a),id(b))
	assert id(a) == id(b)