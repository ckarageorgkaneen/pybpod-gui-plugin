.. pybpodapi documentation master file, created by
   sphinx-quickstart on Wed Jan 18 09:35:10 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _installing-label:

**********
Installing
**********

.. note::
   This page describes **PyBpod** installation from source. If you just want to try **PyBpodGUI** you can find Windows and Mac OS binaries available at the `downloads page <https://bitbucket.org/fchampalimaud/pybpod-gui-plugin/downloads/>`_.


PyBpod GUI Plugin
=================

**PyBpod** works as plugin for a generic GUI framework, called **PyformsGenericEditor**. Thus, you will need to download this project source code.

Installing Python3
==================

You can follow the SWP `Python Installation <http://swp-docs.readthedocs.io/en/latest/python-installation/index.html>`_ tutorial.

.. warning::
   This project requires Python 3! Python2 is not supported.

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

    pip3 install -r requirements.txt --upgrade # installs dependencies (including qt5 and qscintilla2)

..    pip3 install . # installs this project

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
      'pybpodgui_plugin',
      'pybpodgui_plugin_timeline',
      'session_log_plugin',
   ]

   DEFAULT_PROJECT_PATH = None # optionally define here the path to an already existent project to open automatically


Running GUI
===========

On the project root folder (where *'setup.py'* is located) run the following commands:

::

    python3 -m pyforms_generic_editor
