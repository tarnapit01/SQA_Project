class Car:
    def __init__(self, model):
        self.model = model

    def start(self):
        print(f"Starting {self.model} car")

    def stop(self):
        print(f"Stopping {self.model} car")

    def drive(self):
        print(f"Driving {self.model} car")


def audio_system(func):
    def wrapper(self, *args, **kwargs):
        print("Turning on the audio system")
        func(self, *args, **kwargs)
        print("Turning off the audio system")
    return wrapper


def navigation_system(func):
    def wrapper(self, *args, **kwargs):
        print("Navigating to destination")
        func(self, *args, **kwargs)
        print("Navigation completed")
    return wrapper


def security_system(func):
    def wrapper(self, *args, **kwargs):
        print("Activating security system")
        func(self, *args, **kwargs)
        print("Deactivating security system")
    return wrapper


@audio_system
@navigation_system
@security_system
class EnhancedCar(Car):
    pass