from abc import ABC, abstractmethod

# Subject (Observable)
class Car(ABC):
    def __init__(self):
        self._observers = []

    def add_feature(self, observer):
        self._observers.append(observer)

    def remove_feature(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

# Concrete Subject
class MyCar(Car):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify()

# Observer
class Feature(ABC):
    @abstractmethod
    def update(self, car):
        pass

# Concrete Observers
class AudioSystem(Feature):
    def update(self, car):
        if car.state == "audio_on":
            print("Audio System is now ON.")
        elif car.state == "audio_off":
            print("Audio System is now OFF.")

class NavigationSystem(Feature):
    def update(self, car):
        if car.state == "navigation_on":
            print("Navigation System is now ON.")
        elif car.state == "navigation_off":
            print("Navigation System is now OFF.")

class SecuritySystem(Feature):
    def update(self, car):
        if car.state == "security_on":
            print("Security System is now ON.")
        elif car.state == "security_off":
            print("Security System is now OFF.")

# Client code to demonstrate the pattern
if __name__ == "__main__":
    car = MyCar()

    audio = AudioSystem()
    navigation = NavigationSystem()
    security = SecuritySystem()

    car.add_feature(audio)
    car.add_feature(navigation)
    car.add_feature(security)

    car.state = "audio_on"
    car.state = "navigation_on"
    car.state = "security_on"

    car.state = "audio_off"
    car.state = "security_off"
