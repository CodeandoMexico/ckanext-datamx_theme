from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(
	name='ckanext-datamx',
	version=version,
	description="Datamx theme",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Codeando Mexico',
	author_email='equipo@codeandomexico.org',
	url='datamx.io',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.datamx'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
        ckanext-datamx=ckanext.datamx.plugin:DatamxThemePlugin
        datamx_controller = ckanext.datamx.controller:DatamxController
	""",
)
