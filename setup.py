from setuptools import setup, find_packages

# Read requirements from the 'requirements.txt' file
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='camera-simulator',
    version='0.3',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'camera-simulator=lens_sensor_simulator:main',
        ],
    },
)