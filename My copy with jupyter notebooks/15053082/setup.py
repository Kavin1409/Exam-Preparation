
from setuptools import setup, find_packages

setup(
    name="alchemist",
    version="0.0.3",
    author="Kavin Arunasalam",
    packages=find_packages(exclude=['*test']),
    install_requires=['argparse','PyYAML'],
    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:process'
        ]})