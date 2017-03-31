.. pybpodapi documentation master file, created by
   sphinx-quickstart on Wed Jan 18 09:35:10 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _installing-label:

**********
Installing
**********

PyBpod GUI Plugin
=================

**PyBpod** works as plugin for a generic GUI framework, called PyformsGenericEditor. Thus, you will need to install 2 projects first:

   * PyQt4
   * Pyforms Generic Editor

.. warning::
   This project uses Python 3!

Installing PyQt4
================

Mac OS
------

You can follow the SWP `PyQt4 Installation with QScintilla <http://swp-docs.readthedocs.io/en/latest/pyqt-installation/index.html#on-mac-os>`_ tutorial.

.. seealso::
   [Install python and its tools using Homebrew] (http://brew.sh)

   [Scientific Python on Mac OS X 10.9+ with homebrew | Jörn's Blog](https://joernhees.de/blog/2014/02/25/scientific-python-on-mac-os-x-10-9-with-homebrew/)

   [Installing scientific Python on Mac OS X | Lowin Data Company](http://www.lowindata.com/2013/installing-scientific-python-on-mac-os-x/)

Windows
-------

One easy way is to install `WinPython <http://winpython.github.io>`_. This way you do not mess with other Python installations on the system.

You can download the latest version compatible with PyQt4 here: https://sourceforge.net/projects/winpython/files/WinPython_3.5/3.5.2.3/WinPython-64bit-3.5.2.3.exe/download

Ubuntu
------

Will be added soon!

Installing Pyforms Generic Editor
=================================

Option A. Clone project from Bitbucket:
---------------------------------------

::

    git clone https://bitbucket.org/fchampalimaud/pyforms-generic-editor.git


Option B. Download zip
----------------------

https://bitbucket.org/fchampalimaud/pyforms-generic-editor/get/master.zip

Install files
-------------

On the project root folder (where *'setup.py'* is located) run the following commands:

::

    pip3 install -r requirements.txt --upgrade # installs dependencies
    pip3 install . # installs this project

Configuring PyBpod Plugin
=========================

On the project root folder (where *'setup.py'* is located) create a new file named "pyforms_generic_editor_user_settings.py". Then, copy the following content:

::

   # !/usr/bin/python3
   # -*- coding: utf-8 -*-

   SETTINGS_PRIORITY = 0


   ############ PYFORMS GENERIC EDITOR SETTINGS ############

   GENERIC_EDITOR_WINDOW_GEOMETRY = 100, 100, 1200, 800

   GENERIC_EDITOR_TITLE = "PyBpod GUI"

   # OPTIONAL FOR MAC OS
   PYFORMS_MAINWINDOW_MARGIN = 0
   PYFORMS_STYLESHEET = ''
   PYFORMS_STYLESHEET_DARWIN = ''

   GENERIC_EDITOR_PLUGINS_LIST = [
       'pybpodgui_plugin_timeline',
       'pybpodgui_plugin',
       'session_log_plugin',
   ]

   DEFAULT_PROJECT_PATH = None # optionally define here the path to an already existent project to open automatically

