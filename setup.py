from setuptools import find_packages, setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='covid19it',
    packages=find_packages(include=['covid19it']),
    version='1.2.0',
    description='Covid-19 italy report',
    author='Mik3sw',
    license='MIT',
    install_requires=['requests'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/mik3sw/Covid-19-Italy'
)