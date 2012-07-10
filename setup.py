#!/usr/bin/env python

from setuptools import setup

setup(
    name='numberlike',
    version='0.1.0',
    description='Types for overloaded numbers',
    long_description=(
        'Includes semantic version number type,'
        ' and some checksums'),
    author='Anders Eurenius',
    author_email='aes@nerdshack.com',
    license='bsd',
    # url='http://www.python.org/sigs/distutils-sig/',
    packages=['numberlike'],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent'])
