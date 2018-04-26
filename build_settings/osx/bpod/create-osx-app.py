"""
Create a stand-alone Mac OS X app using py2app
To be used like this:

(from the pybpod-gui-plugin folder)
$: pyenv activate pybpod-gui-py3.5.3 # do this if you use pyenv virtualenv
$: pip install -r requirements-dev-YOURNAME.txt 

(from this file folder)
$: python create-osx-app.py py2app   (to build the app)
$: hdiutil create dist/$PROJECT_NAME.dmg -srcfolder dist/$PROJECT_NAME.app/


WARN: DO NOT FORGET TO UPDATE VERSION BEFORE RUNNING THIS SCRIPT!!!!

IF YOU NEED MATPLOTLIB, YOU MAY NEED THE LATEST VERSION OF py2app
"SyntaxError: 'yield' inside async function"
https://github.com/pyinstaller/pyinstaller/commit/48d5554ae74c2759d1fc099d4b2546288cad59fb
https://github.com/pyinstaller/pyinstaller/issues/2434
Solution:
pip install py2app

"""

import os
from setuptools import setup
from shutil import copyfile
import pybpodgui_plugin as app_package

MAIN_SCRIPT_PATH = ['../../../pybpodgui_plugin/__main__.py']
DATA_FILES = []
PACKAGES = ['PyQt5', 'pyforms_generic_editor', 'pyforms', 'pybranch', 'pyforms', 'loggingbootstrap', 'pybpodapi',
            'pybpodgui_plugin', 'pge_welcome_plugin', 'pybpodgui_plugin_timeline', 'pybpodgui_plugin_session_history']
INCLUDES = []
EXCLUDES = ['pyforms_generic_editor_user_settings']

APP_VERSION = app_package.__version__

EXECUTABLE_NAME = "PyBpodGUI-v{version}".format(version=APP_VERSION)

OPTIONS = {
	'argv_emulation': True,
	'compressed': False,
	'optimize': 0,
	'packages': PACKAGES,
	'includes': INCLUDES,
	'excludes': EXCLUDES,
	'iconfile': 'cf_icon_512x512.icns',
	'strip': True,  # strip debug and local symbols from output (default is True for compatibility)
	'plist': {
		'CFBundleName': EXECUTABLE_NAME,
		'CFBundleDisplayName': EXECUTABLE_NAME,
		'CFBundleGetInfoString': "CF Scientific Software Platform",
		'CFBundleIdentifier': "org.champalimaud.swp.pybpod",
		'CFBundleVersion': APP_VERSION,
		'CFBundleShortVersionString': APP_VERSION,
		'NSHumanReadableCopyright': u"Copyright (C) 2007 Free Software Foundation, Inc."
	}
}

setup(
	name=EXECUTABLE_NAME,
	app=MAIN_SCRIPT_PATH,
	options={'py2app': OPTIONS},
	setup_requires=['py2app'],
)

settings_dest_path = 'dist/' + EXECUTABLE_NAME + '.app/Contents/Resources/lib/python3.5/user_settings.py'
copyfile('simple_user_settings.py', settings_dest_path)
