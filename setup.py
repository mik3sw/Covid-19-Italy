from setuptools import find_packages, setup

setup(
    name='covid19italy',
    packages=find_packages(include=['covid19italy']),
    version='1.0.0',
    description='Covid-19 italy report',
    author='Mik3sw',
    license='MIT',
    install_requires=['requests']
)