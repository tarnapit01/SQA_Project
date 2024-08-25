# car.py

class Car:
    """Represents a basic car."""

    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.features = []  # Store added features

    def description(self):
        base_description = f"This is a {self.model} car."
        if self.features:
            base_description += " It has: " + ", ".join(self.features) + "."
        return base_description


# decorators.py
def add_feature(feature_name, price):
    """Decorator to add a feature to a car."""

    def decorator(car_function):
        def wrapper(self, *args, **kwargs):
            self.price += price
            self.features.append(feature_name)
            return car_function(self, *args, **kwargs)

        return wrapper

    return decorator


class CarFactory:
    """Factory class to create cars with features."""

    @add_feature("audio system", 1000)
    def create_audio_car(self, car):
        return car

    @add_feature("navigation system", 1500)
    def create_nav_car(self, car):
        return car

    @add_feature("security system", 2000)
    def create_security_car(self, car):
        return car