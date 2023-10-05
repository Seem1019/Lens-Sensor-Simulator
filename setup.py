from setuptools import setup, find_packages

# Read requirements from the 'requirements.txt' file
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='Lens-Sensor-Simulator',
    version='0.2',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'lens_sensor_simulator=lens_sensor_simulator:main',
        ],
    },
)