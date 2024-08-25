from abc import ABC, abstractmethod

# Subject (Observable)
class Car:
    def __init__(self):
        self._features = []
        self._state = None

    def add_feature(self, feature):
        self._features.append(feature)

    def remove_feature(self, feature):
        self._features.remove(feature)

    def notify(self):
        for feature in self._features:
            feature.update(self)

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
            print("Audio System: ON")
        elif car.state == "audio_off":
            print("Audio System: OFF")

class NavigationSystem(Feature):
    def update(self, car):
        if car.state == "navigation_on":
            print("Navigation System: ON")
        elif car.state == "navigation_off":
            print("Navigation System: OFF")

class SecuritySystem(Feature):
    def update(self, car):
        if car.state == "security_on":
            print("Security System: ON")
        elif car.state == "security_off":
            print("Security System: OFF")

# Example Usage
if __name__ == "__main__":
    car = Car()

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
    car.state = "navigation_off"
    car.state = "security_off"
