from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in analytica_one/__init__.py
from analytica_one import __version__ as version

setup(
	name='analytica_one',
	version=version,
	description='analytica one app',
	author='THE ELECTRONIC COMMERCE & DATA CONSULTANTS',
	author_email='rk@whitehatglobal.org',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
