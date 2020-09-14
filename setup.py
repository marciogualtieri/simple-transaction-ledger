#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

version = '1.0.0'


def parse_requirements():
    with open('requirements.txt', 'r') as f:
        return [r for r in f.read().splitlines() if not r.startswith('git')]


# The README.md will be used as the content for the PyPi package details page on the Python Package Index.
with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='simple-transaction-ledger',
    version='1.0.0',
    description='Simple Transaction Ledger',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Marcio Gualtieri',
    author_email='marcio.gualtieri@gmail.com',
    url='https://github.com/marciogualtieri/simple-transaction-ledger',
    license='MIT',
    python_requires='>=3.6,<4',
    install_requires=parse_requirements(),
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
