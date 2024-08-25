import pytest
from code import BasicCar,AudioSystem,NavigationSystem,SecuritySystem

def test_basic_car():
    car = BasicCar()
    assert car.description() == "Basic Car"
    assert car.cost() == 10000

def test_car_with_audio_system():
    car = AudioSystem(BasicCar())
    assert car.description() == "Basic Car + Audio System"
    assert car.cost() == 11500

def test_car_with_navigation_system():
    car = NavigationSystem(BasicCar())
    assert car.description() == "Basic Car + Navigation System"
    assert car.cost() == 12500

def test_car_with_security_system():
    car = SecuritySystem(BasicCar())
    assert car.description() == "Basic Car + Security System"
    assert car.cost() == 12000

def test_car_with_audio_and_navigation_systems():
    car = NavigationSystem(AudioSystem(BasicCar()))
    assert car.description() == "Basic Car + Audio System + Navigation System"
    assert car.cost() == 14000

def test_car_with_all_features():
    car = SecuritySystem(NavigationSystem(AudioSystem(BasicCar())))
    assert car.description() == "Basic Car + Audio System + Navigation System + Security System"
    assert car.cost() == 16000
