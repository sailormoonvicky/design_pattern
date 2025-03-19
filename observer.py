from abc import ABC, abstractmethod
# Example Use Case: Weather Station
# Imagine we are designing a Weather Station where multiple devices
# (phone apps, websites, and news channels) need to receive real-time updates when the weather changes.

# Abstract Subject (Observable)
class WeatherStation(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observer(self):
        pass

# Abstract Observer
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

# Concrete Subject
class WeatherData(WeatherStation):
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def add_observer(self, observer:Observer):
        self._observers.append(observer)


    def remove_observer(self, observer:Observer):
        self._observers.remove(observer)

    def notify_observer(self):
        for user in self._observers:
            user.update(self._temperature, self._humidity, self._pressure)

    def set_weather(self, temperature, humidity, pressure):
        """ Updates weather data and notifies observers. """
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observer() # Notify all observers of change

# Concrete Observer: Phone App
class PhoneApp(Observer):
    def update(self, temperature, humidity, pressure):
        print(f'[Phone APP] Weather Updated: {temperature}°C, {humidity}% Humidity, {pressure} hPa')

#Concrete Observer: SMS
class SMS(Observer):
    def update(self, temperature, humidity, pressure):
        print(f'[SMS] Weather Updated: {temperature}°C, {humidity}% Humidity, {pressure} hPa')

#Usage
nation_weather = WeatherData()
app_user = PhoneApp()
sms_user = SMS()
nation_weather.add_observer(app_user)
nation_weather.add_observer(sms_user)
print("Weather Update 1:")
nation_weather.set_weather(26,60,1010)
print("\nWeather Update 2:")
nation_weather.set_weather(30,55,1005)
print("\nNews Channel Unsubscribes:")
nation_weather.remove_observer(sms_user)
print("\nWeather Update 3:")
nation_weather.set_weather(28,65,1000)


## Real-World Example: Stock Market Notifications
# traders receive real-time stock price updates.
class Trader(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, stock_price, volume, market_status):
        print(f'[{self._name}] Alert! Stock Price:£{stock_price}, Volume: {volume}, Market: {market_status}')

# Concrete Subject: Stock Market
class StockMarket(WeatherStation):
    def __init__(self):
        self._observer = []
        self._stock_price = None
        self._volume = None
        self._market_status = None

    def add_observer(self, observer):
        self._observer.append(observer)

    def remove_observer(self, observer):
        self._observer.remove(observer)

    def notify_observer(self):
        for user in self._observer:
            user.update(self._stock_price, self._volume, self._market_status)

    def set_stock_info(self, stock_price, volume, market_status):
        self._stock_price = stock_price
        self._volume = volume
        self._market_status = market_status
        self.notify_observer()

london_stock_exchange = StockMarket()

trader1 = Trader("Alice")
trader2 = Trader("Bob")
trader3 = Trader("Cindy")
london_stock_exchange.add_observer(trader1)
london_stock_exchange.add_observer(trader2)
london_stock_exchange.add_observer(trader3)

print("Stock Update 1:")
london_stock_exchange.set_stock_info(150,10000,"Open")

print("\nBob Unsubscribes")
london_stock_exchange.remove_observer(trader2)

print("\nStock Update 2:")
london_stock_exchange.set_stock_info(160, 12000,'Close')
