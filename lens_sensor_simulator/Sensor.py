class Sensor(BaseProcessor):
    """Sensor class for image processing.

    Attributes:
        gain (int): The gain of the sensor.
    """

    def __init__(self, gain):
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
        self._gain = value

    def process(self, image):
        """Multiply the input numpy data by the gain and return it.

        Args:
            image (np.ndarray): The input 2D numpy array.

        Returns:
            np.ndarray: The output 2D numpy array.
        """
        return self._gain * image