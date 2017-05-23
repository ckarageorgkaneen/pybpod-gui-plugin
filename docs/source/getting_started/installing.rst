.. pybpodapi documentation master file, created by
   sphinx-quickstart on Wed Jan 18 09:35:10 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _installing-label:

**********
Installing
**********

.. note::
   This page describes pybpod libraries installation from source. If you just want to try **PyBpod** you can find Windows and Mac OS binaries available at the `downloads page <https://bitbucket.org/fchampalimaud/pybpod-gui-plugin/downloads/>`_.


Installing PyBpod-GUI and PyBpod-API from sources
=================================================

1. Download projects
--------------------
Run the following commands inside the folder where you want to install the source code. A new folder will be automatically created for each project.

::

    # PyBpod API
    git clone https://bitbucket.org/fchampalimaud/pybpod-api.git

    # PyBpod GUI plugin
    git clone https://bitbucket.org/fchampalimaud/pybpod-gui-plugin.git



2. Install requirements
-----------------------
For each project you should now install the requirements.

::

    # Inside pybpod-api folder
    pip install -r requirements-dev.txt --upgrade

    # Inside pybpod-gui-plugin folder
    pip install -r requirements-dev.txt --upgrade


3. Set up user settings
-----------------------
Inside the pybpod-gui-plugin folder, locate the file *user_settings.py.template*. **Duplicate this file** and name it to *user_settings.py*.

4. Run it!
----------

::

    # Inside pybpod-gui-plugin folder
    python3 -m pybpodgui_plugin

