from setuptools import find_packages, setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='covid19italy',
    packages=find_packages(include=['covid19italy']),
    version='1.1.0',
    description='Covid-19 italy report',
    author='Mik3sw',
    license='MIT',
    install_requires=['requests']
)