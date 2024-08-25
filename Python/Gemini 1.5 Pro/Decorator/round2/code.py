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
    """Decorator factory to add a feature to a car."""

    def decorator(car_class):
        class FeatureAddedCar(car_class):
            def __init__(self, model, base_price):
                super().__init__(model, base_price)
                self.price += price
                self.features.append(feature_name)

        return FeatureAddedCar

    return decorator


@add_feature("audio system", 1000)
class AudioCar(Car):
    pass


@add_feature("navigation system", 1500)
class NavCar(Car):
    pass


@add_feature("security system", 2000)
class SecurityCar(Car):
    pass