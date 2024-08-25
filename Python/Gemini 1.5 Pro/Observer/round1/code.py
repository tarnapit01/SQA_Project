from abc import ABC, abstractmethod


class Car:
    """
    The Subject (Car) maintains a list of its dependents, called observers,
    and notifies them automatically of any state changes, usually by calling
    one of their methods.
    """

    def __init__(self):
        self._observers = []
        self._features = []

    def attach(self, observer):
        """Attach an observer to the car."""
        self._observers.append(observer)

    def detach(self, observer):
        """Detach an observer from the car."""
        self._observers.remove(observer)

    def notify(self):
        """Notify all observers about an update."""
        for observer in self._observers:
            observer.update(self)

    def add_feature(self, feature):
        """Add a new feature to the car."""
        self._features.append(feature)
        print(f"Car: Added feature: {feature}")
        self.notify()

    def get_features(self):
        """Get the list of features in the car."""
        return self._features


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject):
        """Receive update from subject."""
        pass


class AudioSystem(Observer):
    """
    Concrete Observers react to the updates issued by the Subject they had been
    attached to.
    """

    def update(self, subject):
        """React to the car update."""
        if "Audio System" in subject.get_features():
            print("AudioSystem: Reacting to car update: Audio system installed.")


class NavigationSystem(Observer):
    """
    Concrete Observers react to the updates issued by the Subject they had been
    attached to.
    """

    def update(self, subject):
        """React to the car update."""
        if "Navigation System" in subject.get_features():
            print("NavigationSystem: Reacting to car update: Navigation system installed.")


class SecuritySystem(Observer):
    """
    Concrete Observers react to the updates issued by the Subject they had been
    attached to.
    """

    def update(self, subject):
        """React to the car update."""
        if "Security System" in subject.get_features():
            print("SecuritySystem: Reacting to car update: Security system installed.")