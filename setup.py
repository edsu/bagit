#!/usr/bin/env python

from setuptools import setup

setup(
    name="bagit",
    version="2.0.0",
    url="https://github.com/edsu/bagit/",
    author="Ed Summers",
    author_email="ehs@pobox.com",
    packages=["bagit"],
    description="Create and validate BagIt packages",
    long_description="bagit is a Python library and command line utility for working with BagIt style packages.",
    entry_points={"console_scripts": ["bagit = bagit.cli:main"]},
    install_requires=['fs'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
