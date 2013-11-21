from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-custom_theme',
	version=version,
	description="Codeando Mexico custom theme",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Braulio Chavez',
	author_email='braulio@codeandomexico.org',
	url='datos.codeandomexico.org',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.custom_theme'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.custom_theme:PluginClass
	""",
)
