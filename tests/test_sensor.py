import pytest
import numpy as np
from lens_sensor_simulator.Sensor import Sensor


def test_sensor_gain_property():
    """
    Tests that the gain property is set to None by default
    """
    sensor = Sensor()
    assert sensor.gain is None


def test_sensor_gain_setter():
    """
    Tests that the gain property can be set to an integer
    """
    sensor = Sensor()
    sensor.gain = 2
    assert sensor.gain == 2


def test_sensor_gain_setter_invalid_value():
    """
    Tests that setting an invalid gain value raises a ValueError
    """
    sensor = Sensor()
    with pytest.raises(ValueError):
        sensor.gain = '2'


def test_process_invalid_input():
    """
    Tests that the process method raises a ValueError if the input is not a numpy array
    """
    sensor = Sensor()
    with pytest.raises(ValueError):
        sensor.process([10, 20])


def test_process_no_gain():
    """
    Tests that the process method raises a ValueError if no gain is defined
    """
    sensor = Sensor()
    with pytest.raises(ValueError) as excinfo:
        sensor.process(np.zeros((1, 10)))
    assert 'A sensor gain must be defined' in str(excinfo.value)


def test_process_correct():
    """
    Tests that the process method correctly applies the gain to the input image
    """
    sensor = Sensor()
    gain = 2
    sensor.gain = gain
    image = np.ones((10, 20))
    output = sensor.process(image)
    assert np.array_equal(output, image * gain) == True