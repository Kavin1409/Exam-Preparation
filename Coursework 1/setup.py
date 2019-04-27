
from setuptools import setup, find_packages

setup(
    name="alchemist",
    version="0.0.3",
    author="Kavin Arunasalam",
    packages=find_packages(exclude=['*tests']),
    install_requires=['argparse','pyyaml'],
    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:process'
        ]})