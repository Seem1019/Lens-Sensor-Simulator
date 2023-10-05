from abc import ABC, abstractmethod
import numpy as np


class BaseProcessor(ABC):
    """Base class for image processors.

    Attributes:
        enable (bool): Whether the processor is enabled.
    """

    def __init__(self, enable=True):
        """Initialize BaseProcessor.

        Args:
            enable (bool): Whether the processor is enabled.
        """
        self._enable = enable

    @property
    def enable(self):
        """bool: Get or set the enable status."""
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value

    @abstractmethod
    def process(self, image):
        """Process the input 2D numpy data and return output 2D numpy data.

        Args:
            image (np.ndarray): The input 2D numpy array.

        Returns:
            np.ndarray: The output 2D numpy array.
        """
        pass

# Advanced Python Features
# TODO: Implement Lens decorator for Sensors
# TODO: Allow the Sensor to be used as an iterator of 10 elements
# TODO: Implement the 'mymean' function
