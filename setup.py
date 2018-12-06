#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

setup(
    name="bagit",
    version="2.0.0",
    url="https://libraryofcongress.github.io/bagit-python/",
    author="Ed Summers",
    author_email="ehs@pobox.com",
    py_modules=["bagit"],
    description="Create and validate BagIt packages",
    long_description="bagit is a Python library and command line utility for working with BagIt style packages.",
    entry_points={"console_scripts": ["bagit = bagit.cli:main"]},
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        "License :: Public Domain",
        "Intended Audience :: Developers",
        "Topic :: Communications :: File Sharing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Filesystems",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
