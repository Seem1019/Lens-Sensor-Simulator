# Camera Simulator Project

## Overview
This project is a Python-based Lens and Sensor simulator. It serves as a technical test to demonstrate advanced Python skills, object-oriented programming (OOP), and software design patterns.

## Features
- Abstract Base Class for image processors
- Lens class for image shape validation
- Sensor class for image manipulation

## Features Implemented

### Sensor Class

- The `Sensor` class multiplies an input image (2D numpy array) by a gain factor.
- The gain factor can be set and retrieved using the `gain` property.

### Lens Class

- The `Lens` class validates the shape of the input image against the lens dimensions (height and width).
- The dimensions can be set and retrieved using the `height` and `width` properties.

### Concurrency

- Used `ThreadPoolExecutor` from Python's `concurrent.futures` library to create a pool of 5 workers.
- The workers execute the `mymean_ignored_args` function 100 times in parallel.

### Utilities

- Created a `mymean` function that generates a random image, processes it through a `Sensor` object, and returns the mean of the image.
- Created a decorator `ignore_args` to allow functions to ignore any arguments passed to them.

## Documentation

- The project is documented using Sphinx. You can generate the documentation by running `sphinx-build -b html . ./_build` in the `docs` directory.

## Testing

- Tests can be run using Docker. Follow the steps below to run the tests:

    ```bash
    docker build -t camera-simulator-test .
    docker run camera-simulator-test
    ```

## Relevant Comments

- The `ignore_args` decorator is useful for using the `mymean` function with `ThreadPoolExecutor.map`, which expects a function to take an argument.
- The `Sensor` and `Lens` classes inherit from a `BaseProcessor` class, promoting code reusability.
- The project is structured to be easily extendable for adding more features like different types of sensors or lenses.

## How to Run

1. Install the package using pip:

    ```bash
    pip install -e .
    ```

2. Run the main script:

    ```bash
    pysensor
    ```

