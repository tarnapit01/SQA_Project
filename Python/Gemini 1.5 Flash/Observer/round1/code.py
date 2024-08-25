class Subject:
    """Represents the car, which is the subject of observation."""

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """Attach an observer to the car."""
        self._observers.append(observer)

    def detach(self, observer):
        """Detach an observer from the car."""
        self._observers.remove(observer)

    def notify(self, event):
        """Notify all observers about the event."""
        for observer in self._observers:
            observer.update(event)


class Observer:
    """Abstract base class for observers."""

    def update(self, event):
        """Receive notification about an event."""
        raise NotImplementedError


class AudioSystem(Observer):
    """Represents an audio system as an observer."""

    def update(self, event):
        """Respond to car events related to audio."""
        if event == "start":
            print("Audio system: Playing welcome tune.")
        elif event == "stop":
            print("Audio system: Turning off.")


class NavigationSystem(Observer):
    """Represents a navigation system as an observer."""

    def update(self, event):
        """Respond to car events related to navigation."""
        if event == "start":
            print("Navigation system: Starting navigation.")
        elif event == "destination":
            print("Navigation system: Setting new destination.")


class SecuritySystem(Observer):
    """Represents a security system as an observer."""

    def update(self, event):
        """Respond to car events related to security."""
        if event == "start":
            print("Security system: Disarming.")
        elif event == "stop":
            print("Security system: Arming.")


# Example usage:
if __name__ == "__main__":
    car = Subject()

    audio_system = AudioSystem()
    navigation_system = NavigationSystem()
    security_system = SecuritySystem()

    car.attach(audio_system)
    car.attach(navigation_system)
    car.attach(security_system)

    print("Starting the car...")
    car.notify("start")

    print("Setting a destination...")
    car.notify("destination")

    print("Stopping the car...")
    car.notify("stop")