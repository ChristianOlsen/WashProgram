from setuptools import setup, find_packages

setup(
    name='WashIt',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    scripts=['bin/washit'],
    author='Christian Olsen',
    author_email='christian.tkd.olsen@gmail.com',
    url='https://github.com/ChristianOlsen/WashIt'
)
