import pytest
from io import StringIO
import sys

from code import MyCar, AudioSystem, NavigationSystem, SecuritySystem

@pytest.fixture
def car():
    return MyCar()

@pytest.fixture
def audio_system():
    return AudioSystem()

@pytest.fixture
def navigation_system():
    return NavigationSystem()

@pytest.fixture
def security_system():
    return SecuritySystem()

def test_audio_system_on(car, audio_system, capsys):
    car.add_feature(audio_system)
    car.state = "audio_on"
    captured = capsys.readouterr()
    assert "Audio System is now ON." in captured.out

def test_audio_system_off(car, audio_system, capsys):
    car.add_feature(audio_system)
    car.state = "audio_off"
    captured = capsys.readouterr()
    assert "Audio System is now OFF." in captured.out

def test_navigation_system_on(car, navigation_system, capsys):
    car.add_feature(navigation_system)
    car.state = "navigation_on"
    captured = capsys.readouterr()
    assert "Navigation System is now ON." in captured.out

def test_navigation_system_off(car, navigation_system, capsys):
    car.add_feature(navigation_system)
    car.state = "navigation_off"
    captured = capsys.readouterr()
    assert "Navigation System is now OFF." in captured.out

def test_security_system_on(car, security_system, capsys):
    car.add_feature(security_system)
    car.state = "security_on"
    captured = capsys.readouterr()
    assert "Security System is now ON." in captured.out

def test_security_system_off(car, security_system, capsys):
    car.add_feature(security_system)
    car.state = "security_off"
    captured = capsys.readouterr()
    assert "Security System is now OFF." in captured.out
