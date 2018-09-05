#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

version = ''
with open('pybpodgui_plugin/__init__.py', 'r') as fd: version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                                                                      fd.read(), re.MULTILINE).group(1)
if not version: raise RuntimeError('Cannot find version information')

requirements = [
	'pyforms>=1.0.0',
	'pyforms=1.0.beta',
	'pyforms_generic_editor>=1.1.0',
	'pyserial>= 3.1.1',
	'logging-bootstrap>=1.0.0',
]

setup(
	name='pybpod-gui-plugin',
	version=version,
	description="""pybpod-gui-plugin is a behavioral experiments control system written in Python 3.5 for Bpod""",
	author=['Carlos Mão de Ferro', 'Ricardo Ribeiro'],
	author_email='cajomferro@gmail.com',
	license='Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>',
	url='https://bitbucket.org/fchampalimaud/pycontrolgui',

	include_package_data=True,
	packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'deploy', 'reports']),

	# install_requires=requirements,

	entry_points={
		'gui_scripts': [
			'start-pybpod=pybpodgui_plugin.__main__:start',
		],
	}
)
