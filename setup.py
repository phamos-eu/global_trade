# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in global_trade/__init__.py
from global_trade import __version__ as version

setup(
	name='global_trade',
	version=version,
	description='ERPNext App for internation goods trading.',
	author='tüit GmBH',
	author_email='administrator@tueit.de',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
