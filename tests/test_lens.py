import pytest
import numpy as np
from lens_sensor_simulator.Lens import Lens


def test_lens_height_property():
    """
    Tests that the height property is set to None by default
    """
    lens = Lens()
    assert lens.height is None


def test_lens_width_property():
    """
    Tests that the width property is set to None by default
    """
    lens = Lens()
    assert lens.width is None


def test_lens_height_setter():
    """
    Tests that the height property can be set to an integer
    """
    lens = Lens()
    lens.height = 10
    assert lens.height == 10




def test_lens_width_setter():
    """
    Tests that the width property can be set to an integer
    """
    lens = Lens()
    lens.width = 20
    assert lens.width == 20




def test_process_correct():
    """
    Tests that the process method correctly processes the input image when dimensions are set
    """
    lens = Lens(height=10, width=20)
    lens.set_dimensions(height=10, width=20)
    image = np.zeros((10, 20))
    output = lens.process(image)
    assert np.array_equal(image, output) == True