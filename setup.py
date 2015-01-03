#!/usr/bin/python3

from setuptools import setup, find_packages
import pyMouseTrack
import sys

requires = [
    'Pillow',
    'PyUserInput',
    'pyimgur',
    'pyscreenshot'
]


if sys.version_info[0] == 3:
    requires.append('python3-xlib')
else:
    requires.append('python-xlib')

setup(
    name="pyMouseTrack",
    version=pyMouseTrack.__VERSION__,
    description="Turn mouse movement into pictures.",
    url="https://github.com/tuankiet65/pyMouseTrack",
    author="Ho Tuan Kiet",
    author_email="tuankiet65@gmail.com",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=requires,
    packages=find_packages(exclude=["docs", "test"]),
    entry_points={
        'console_scripts': [
            'pyMouseTrack=pyMouseTrack.main:main'
        ]
    }
)
