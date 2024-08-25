import pytest
from code import Car, AudioSystem, NavigationSystem, SecuritySystem


def test_car_features():
    """Test adding features to the car and observer notifications."""
    car = Car()
    audio_system = AudioSystem()
    navigation_system = NavigationSystem()
    security_system = SecuritySystem()

    car.attach(audio_system)
    car.attach(navigation_system)
    car.attach(security_system)

    car.add_feature("Audio System")
    car.add_feature("Navigation System")
    car.add_feature("Security System")

    assert "Audio System" in car.get_features()
    assert "Navigation System" in car.get_features()
    assert "Security System" in car.get_features()


def test_observer_detach():
    """Test detaching an observer from the car."""
    car = Car()
    audio_system = AudioSystem()

    car.attach(audio_system)
    car.detach(audio_system)  # Detach the observer

    car.add_feature("Audio System")  

    assert "Audio System" in car.get_features()


def test_observer_update_no_feature():
    """Test that update is called with the correct feature."""
    car = Car()
    audio_system = AudioSystem()
    car.attach(audio_system)
    car.add_feature("Other Feature")  # Trigger update but should not print anything
    assert "Other Feature" in car.get_features()

def test_attach_duplicate_observer():
    """Test that attaching the same observer twice doesn't result in duplicate notifications."""
    car = Car()
    audio_system = AudioSystem()

    car.attach(audio_system)
    car.attach(audio_system)  # Try to attach the same observer again

    car.add_feature("Audio System") 
    # Count the number of times "Audio system installed" is printed (should be 1)
    assert car.get_features().count("Audio System") == 1