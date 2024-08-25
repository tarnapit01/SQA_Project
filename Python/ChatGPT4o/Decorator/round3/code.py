from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def description(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass
class BasicCar(Car):
    def description(self):
        return "Basic Car"
    
    def cost(self):
        return 10000
class CarDecorator(Car):
    def __init__(self, car: Car):
        self._car = car
    
    def description(self):
        return self._car.description()
    
    def cost(self):
        return self._car.cost()
class AudioSystem(CarDecorator):
    def description(self):
        return self._car.description() + " + Audio System"
    
    def cost(self):
        return self._car.cost() + 1500

class NavigationSystem(CarDecorator):
    def description(self):
        return self._car.description() + " + Navigation System"
    
    def cost(self):
        return self._car.cost() + 2500

class SecuritySystem(CarDecorator):
    def description(self):
        return self._car.description() + " + Security System"
    
    def cost(self):
        return self._car.cost() + 2000
