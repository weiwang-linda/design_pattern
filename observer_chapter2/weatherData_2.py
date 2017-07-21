#############################
#weatherData_2.py
#
#Using abstract method
#############################

from abc import ABCMeta, abstractmethod

class Bulletin():
	__metaclass__ = ABCMeta

	def __init__(self):
		self.display = None

	@abstractmethod
	def update(self, temp, humidity, pressure):
		pass

	def show(self):
		print(self.display)

class WeatherData():
	def __init__(self, *data):   # tuple argument usage
		self.temp = data[0]
		self.humidity = data[1]
		self.pressure = data[2]

	def getTemp(self):
		return self.temp

	def getHumidity(self):
		return self.humidity

	def getPressure(self):
		return self.pressure

	def measurementsChanged(self, bulletin):
		self.temp = self.getTemp()
		self.humidity = self.getHumidity()
		self.pressure = self.getPressure()

		bulletin.update(self.temp, self.humidity, self.pressure)   # add any bulletin board is flexible.
		#TODO: 
		# Need to modify for some bulletins don't want to update again
		# Later maybe these bulletins want to update again

class CurrentConditionsDisplay(Bulletin):
	def update(self, temp, humidity, pressure):
		self.display = str(temp) + "- " + str(humidity) + "- " + str(pressure)

class StaticsDisplay(Bulletin):
	def update(self, temp, humidity, pressure):
		self.display = (temp+humidity+pressure)/3

class ForecastDisplay(Bulletin):
	def update(self, temp,humidity,pressure):
		aver = (temp+humidity+pressure)/3

		if aver < 30:
			self.display = 1
		elif aver >= 30:
			self.display = 2

	def show(self):
		if not self.display:
			print("Display abnormal!")
		elif self.display == 1:
			print("Today is cloudy!")
		elif self.display == 2:
			print("Today is sunny!")


if __name__ == "__main__":
	wd = WeatherData(10,20,30)   ## tuple argument usage
	ccd = CurrentConditionsDisplay()
	sd = StaticsDisplay()
	fd = ForecastDisplay()
	wd.measurementsChanged(ccd)
	ccd.show()
	wd.measurementsChanged(sd)
	sd.show()
	wd.measurementsChanged(fd)
	fd.show()