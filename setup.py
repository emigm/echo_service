'''HTTP echo service package setup'''
import os

from setuptools import setup
from setuptools import find_packages


PWD = os.path.dirname(os.path.realpath(__file__))


setup(
    name='echo_service',
    version='1.0.0',
    packages=find_packages(PWD, exclude=[]),
    install_requires=[
        'mock',
        'pip',
        'blist',
        'pycurl',
        'strict_rfc3339',
        'tornado',
    ],
    entry_points={
        'console_scripts': [
            'echo_service = echo_service.service.run:main',
        ],
    },
)
