################################
# weatherData_advance.py
#
# Make some modifies.
################################

from abc import ABCMeta, abstractmethod

## Define interface classes
class Subject():
	__metaclass__ = ABCMeta

	@abstractmethod
	def registerObserver(self, observer):
		pass

	@abstractmethod
	def unregisterObserver(self, observer):
		pass

	@abstractmethod
	def notifyObservers(self, observer):
		pass


class Observer():
	__metaclass__ = ABCMeta

	@abstractmethod
	def update(self, temp, humidity, pressure):
		pass


class DisplayElement():
	__metaclass__ = ABCMeta

	@abstractmethod
	def display(self):
		pass


## Derived classes from interface
class WeatherData(Subject):
	def __init__(self):
		self.temp = None
		self.humidity = None
		self.pressure = None
		self.observers = []       ##所有观察者用一个list类型在主题subject类里记录

	def registerObserver(self, observer):
		self.observers.append(observer)

	def unregisterObserver(self, observer):
		self.observers.remove(observer)
		# for obs in self.observers:
		# 	print(obs)

	def notifyObservers(self):
		for ob in self.observers:
			ob.update(self.temp, self.humidity, self.pressure)

	def getTemp(self):
		return self.temp

	def getHumidity(self):
		return self.humidity

	def getPressure(self):
		return self.pressure

	def measurementsChanged(self):
		self.notifyObservers()

	def setMeasurements(self, *data):
		self.temp = data[0]
		self.humidity = data[1]
		self.pressure = data[2]
		self.measurementsChanged()      ## 添加这行使得代码量减少了，避免在函数外调用,充分利用封装特性，界面整洁.

class CurrentConditionsDisplay(Observer, DisplayElement):
	def __init__(self, wd):
		self.temp =None
		self.humidity = None
		self.pressure = None
		self.weatherData = wd          ##保存对subject的引用，为了注册时方便对subject的引用
		wd.registerObserver(self)      ## 初始化时调用注册，使得对象生成就已经注册好了，很好的利用了封装特性，可以减少代码量，外观整洁。

	def display(self):
		## 显示函数把主要的显示算法写出来，而不应该写在其他函数里，用多余的变量引用到此函数。
		print(str(self.temp) + "- " + str(self.humidity) + "- " + str(self.pressure))

	## 三个布告板类的update函数内容一样，可以写入父类利用继承, 但此处特殊在于父类我们使用的是接口
	def update(self, temp, humidity, pressure):
		self.temp = temp
		self.humidity = humidity
		self.pressure = pressure
		self.display()                 ## 不是必须放这里, MVC模式就会有变化

class StaticsDisplay(Observer, DisplayElement):
	def __init__(self, wd):
		self.temp =None
		self.humidity = None
		self.pressure = None
		self.weatherData = wd
		wd.registerObserver(self)

	def display(self):
		print((self.temp + self.humidity + self.pressure)/3)

	def update(self, temp, humidity, pressure):
		self.temp = temp
		self.humidity = humidity
		self.pressure = pressure
		self.display()

class ForecastDisplay(Observer, DisplayElement):
	def __init__(self, wd):
		self.temp =None
		self.humidity = None
		self.pressure = None
		self.weatherData = wd
		wd.registerObserver(self)

	def display(self):
		aver = (self.temp + self.humidity + self.pressure)/3

		if aver < 30:
			print("Today is cloudy!")
		elif aver >= 30:
			print("Today is sunny!")
		else:
			print("Display abnormal!")

	def update(self, temp, humidity, pressure):
		self.temp = temp
		self.humidity = humidity
		self.pressure = pressure
		self.display()


if __name__ == "__main__":
	wd = WeatherData()
	ccd = CurrentConditionsDisplay(wd)
	sd = StaticsDisplay(wd)
	fd = ForecastDisplay(wd)

	wd.setMeasurements(10,20,30)


	print("++++++++++++++++++++++++++")
	wd.unregisterObserver(ccd)
	wd.setMeasurements(20,30,40)