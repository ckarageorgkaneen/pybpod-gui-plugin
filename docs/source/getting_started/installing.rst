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

===========================
Installing from source code
===========================

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
Next, move inside the pybpod-gui-plugin folder and run the following command:

::

    # Inside pybpod-gui-plugin folder
    pip3 install -r requirements-dev.txt --upgrade


.. warning::
   This project requires Python 3! Python2 is not supported.


3. Set up user settings
-----------------------
Inside the pybpod-gui-plugin folder, locate the file :py:class:`user_settings.py.template`. **Duplicate this file** and name it :py:class:`user_settings.py`.

::

   cp user_settings.py.template user_settings.py # For UNIX


4. Run it!
----------

::

    # Inside pybpod-gui-plugin folder
    python3 -m pybpodgui_plugin


.. seealso::
   `Python Installation tutorial <http://swp-docs.readthedocs.io/en/latest/python-installation/index.html>`_ |
   `Using pyenv for python management <http://swp-docs.readthedocs.io/en/latest/python-installation/pyenv.html>`_

================
Try the examples
================

For a complete set of examples, download the `project sample <https://bitbucket.org/fchampalimaud/pybpod-gui-plugin/downloads/simple_project_bpod.zip>`_.
Then, unzip and open this project on the GUI.