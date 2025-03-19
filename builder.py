from abc import ABC, abstractmethod

class Car:
    def __init__(self, model, engine, wheels, color, sunroof):
        self._model = model
        self._engine = engine
        self._wheels = wheels
        self._color = color
        self._sunroof = sunroof

    def __str__(self):
        return f'Car(model={self._model}, engine = {self._engine}, wheels={self._wheels}, color={self._color}, sunroog={self._sunroof})'

class CarFactory:
    def __init__(self, model, engine):
        self._model = model
        self._engine = engine
        self._wheels = None
        self._color = 'Black'
        self._sunroof = None

    def set_wheels(self, num_wheels):
        self._wheels = num_wheels
        return self # return the builder itself for method chaining

    def set_color(self, new_color):
        self._color = new_color
        return self

    def set_sunroof(self, sunroof_type):
        self._sunroof = sunroof_type
        return self

    def build(self):
        return Car(self._model, self._engine, self._wheels, self._color, self._sunroof)

#Usage
car_builder = CarFactory('Golf', 'V8')
my_car = car_builder.set_wheels(4).set_color('Blue').set_sunroof(False).build()
print(my_car)

#Build a pizza
class Pizza:
    def __init__(self, size, crust, toppings, sauce):
        self._size = size
        self._crust = crust
        self._toppings = toppings
        self._sauce = sauce

    def __str__(self):
        return f'Pizza(size={self._size}, crust={self._crust}, toppings={self._toppings}, sauce={self._sauce}).'

class PizzaFactory:
    def __init__(self):
        self._size = 'Medium'
        self._crust = 'Thin'
        self._toppings = []
        self._sauce = 'Tomato'

    def set_size(self, size):
        self._size = size
        return self

    def set_crust(self, crust):
        self._crust = crust
        return self

    def set_toppings(self, toppings):
        self._toppings = toppings
        return self

    def set_sauce(self, sauce):
        self._sauce = sauce
        return self

    def build(self):
        return Pizza(self._size, self._crust, self._toppings, self._sauce)

#Usage
pizza_builder = PizzaFactory()
my_pizza = (pizza_builder.set_size('large')
            .set_crust('Stuffed')
            .set_toppings(['Mushroom','Chicken','Pineaple'])
            .build())

print(my_pizza)


#Burger Builder
class Burger:
    def __init__(self):
        self._bun = None
        self._patty = None
        self._cheese = None

    def set_bun(self, bun_type):
        self._bun = bun_type


    def set_patty(self, patty_style):
        self._patty = patty_style


    def set_cheese(self, cheese_tyle):
        self._cheese = cheese_tyle

class BurgerBuilder:
    def __init__(self):
        self._burger = Burger()

    def add_buns(self,bun_style):
        self._burger.set_bun(bun_style)
        return self

    def add_patty(self, patty_style):
        self._burger.set_patty(patty_style)
        return self

    def add_cheese(self, cheese_style):
        self._burger.set_cheese(cheese_style)
        return self

    def build(self):
        return self._burger

burger_builder = BurgerBuilder()
my_burger = (burger_builder.add_buns('sesame')
             .add_patty('beef')
             .add_cheese('swiss cheese')
             .build())
