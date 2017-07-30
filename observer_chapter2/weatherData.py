################################
# weatherData.py
#
# Using Object-Observer desgin pattern
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
		self.observers = []      ##所有观察者用一个list类型在主题subject类里记录

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

class CurrentConditionsDisplay(Observer, DisplayElement):
	def __init__(self):
		self.show = None

	def display(self):
		print(self.show)

	def update(self, temp, humidity, pressure):
		self.show = str(temp) + "- " + str(humidity) + "- " + str(pressure)

class StaticsDisplay(Observer, DisplayElement):
	def __init__(self):
		self.show = None

	def display(self):
		print(self.show)

	def update(self, temp, humidity, pressure):
		self.show = (temp+humidity+pressure)/3

class ForecastDisplay(Observer, DisplayElement):
	def __init__(self):
		self.show = None

	def display(self):
		if not self.show:
			print("Display abnormal!")
		elif self.show == 1:
			print("Today is cloudy!")
		elif self.show == 2:
			print("Today is sunny!")

	def update(self, temp, humidity, pressure):
		aver = (temp+humidity+pressure)/3

		if aver < 30:
			self.show = 1
		elif aver >= 30:
			self.show = 2


if __name__ == "__main__":
	wd = WeatherData()
	ccd = CurrentConditionsDisplay()
	wd.registerObserver(ccd)
	sd = StaticsDisplay()
	wd.registerObserver(sd)
	fd = ForecastDisplay()
	wd.registerObserver(fd)

	wd.setMeasurements(10,20,30)
	wd.measurementsChanged()              ## this can be in WeatherData.setMeasurements() to decrease code lines
	ccd.display()
	sd.display()
	fd.display()

	print("++++++++++++++++++++++++++")
	wd.unregisterObserver(ccd)
	wd.setMeasurements(20,30,40)
	wd.measurementsChanged()
	ccd.display()
	sd.display()
	fd.display()