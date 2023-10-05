from setuptools import setup, find_packages

setup(
    name='Lens-Sensor-Simulator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.26.0',
    ],
    entry_points={
        'console_scripts': [
            'lens_sensor_simulator=lens_sensor_simulator:main',
        ],
    },
)