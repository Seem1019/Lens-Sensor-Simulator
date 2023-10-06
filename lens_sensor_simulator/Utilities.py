import numpy as np
from lens_sensor_simulator.Sensor import Sensor
from functools import wraps

def mymean():
    """Generate a random image, process it through a Sensor object, and return the mean of the image.

    Returns:
        float: The mean value of the processed image.
    """
    random_image = np.random.rand(10, 10)
    sensor = Sensor(gain=2)
    processed_image = sensor.process(random_image)
    return np.mean(processed_image)

def ignore_args(func):
    """Decorator to ignore arguments passed to a function.

    Args:
        func (callable): The function whose arguments should be ignored.

    Returns:
        callable: A new function that ignores any arguments passed to it.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func()
    return wrapper

mymean_ignored_args = ignore_args(mymean)