from lens_sensor_simulator.BaseProcessor import BaseProcessor
class Sensor(BaseProcessor):
    """Sensor class for image processing.

    Attributes:
        gain (int): The gain of the sensor.
    """

    def __init__(self, gain=None):
        """Initialize Sensor.

        Args:
            gain (int): The gain of the sensor.
        """
        super().__init__()
        self._gain = gain

    @property
    def gain(self):
        """int: Get or set the gain of the sensor."""
        return self._gain

    @gain.setter
    def gain(self, value):
        if not isinstance(value, int):
            raise ValueError("Gain property must be an integer")
        self._gain = value
    
    def _validate_gain(self):
        if not self.gain:
            raise ValueError("A sensor gain must be defined")


    def process(self, image):
        """Multiply the input numpy data by the gain and return it.

        Args:
            image (np.ndarray): The input 2D numpy array.

        Returns:
            np.ndarray: The output 2D numpy array.
        """
        self._validate_gain()
        self._validate_image(image)
        return self._gain * image