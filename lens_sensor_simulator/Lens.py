from lens_sensor_simulator.BaseProcessor import BaseProcessor
class Lens(BaseProcessor):
    """Lens class for image processing.

    Attributes:
        height (int): The height of the lens.
        width (int): The width of the lens.
    """

    def __init__(self, height=None, width=None):
        """Initialize Lens.

        Args:
            height (int): The height of the lens.
            width (int): The width of the lens.
        """
        super().__init__()
        self._height = height
        self._width = width

    @property
    def height(self):
        """int: Get or set the height of the lens."""
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        """int: Get or set the width of the lens."""
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    def set_dimensions(self, height, width):
        """Set the height and width of the lens.

        Args:
            height (int): The height of the lens.
            width (int): The width of the lens.
        """
        self._height = height
        self._width = width

    def process(self, image):
        """Validate the shape of the input numpy data and return it.

        Args:
            image (np.ndarray): The input 2D numpy array.

        Returns:
            np.ndarray: The output 2D numpy array.

        Raises:
            ValueError: If the shape of the input does not match the lens dimensions.
        """
        if image.shape == (self._height, self._width):
            return image
        else:
            raise ValueError('Shape mismatch')