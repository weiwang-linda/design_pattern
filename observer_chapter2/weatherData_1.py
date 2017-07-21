#####################
#weatherData_1.py
#
# Using customer method
#####################

class WeatherData():
	def __init__(self, temp, humidity, pressure):
		self.temp = temp
		self.humidity = humidity
		self.pressure = pressure

	def getTemp(self):
		return self.temp

	def getHumidity(self):
		return self.humidity

	def getPressure(self):
		return self.pressure

	# notify the changed measurements
	def measurementsChanged(self, currentConditionsDisplay, staticsDisplay, forecastDisplay):
		self.temp = self.getTemp()
		self.humidity = self.getHumidity()
		self.pressure = self.getPressure()

		currentConditionsDisplay.update(self.temp, self.humidity, self.pressure)
		staticsDisplay.update(self.temp, self.humidity, self.pressure)
		forecastDisplay.update(self.temp, self.humidity, self.pressure)
		#TODO: need to modify, change to interface mode
		#If a new bulletin board is added by user, need to add it's update() here. So it is not flexible code.

class CurrentConditionsDisplay():
	def __init__(self):
		self.display = None

	def update(self, temp, humidity, pressure):
		self.display = str(temp) + "- " + str(humidity) + "- " + str(pressure)

	def show(self):
		print(self.display)

class StaticsDisplay():
	def __init__(self):
		self.display = None

	def update(self, temp, humidity, pressure):
		self.display = (temp+humidity+pressure)/3

	def show(self):
		print(self.display)

class ForecastDisplay():
	def __init__(self):
		self.display = None

	def update(self, temp, humidity, pressure):
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


if __name__ == '__main__':
	wd = WeatherData(30, 20, 40)
	print(str(wd.getTemp()) + " degree")

	wd2 = WeatherData(10,20,30)
	ccd = CurrentConditionsDisplay()
	sd = StaticsDisplay()
	fd = ForecastDisplay()
	wd2.measurementsChanged(ccd,sd,fd)
	ccd.show()
	sd.show()
	fd.show()
