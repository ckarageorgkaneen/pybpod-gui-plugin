.. pybpodapi documentation master file, created by
   sphinx-quickstart on Wed Jan 18 09:35:10 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

**************************************
Welcome to PyBpod's documentation!
**************************************

.. note::

   All examples and Bpod's state machine and communication logic were based on the original version made available by `Josh Sanders (Sanworks) <https://github.com/sanworks>`_.

Download PyBpod
===============

The latest Windows and Mac OS binaries are available at the `downloads page <https://bitbucket.org/fchampalimaud/pybpod-gui-plugin/downloads/>`_.


What is PyBpod?
===================

.. image:: /_images/bpod_gui_sample.png
   :scale: 100 %

**PyBpod** is a GUI application that enables interaction with the latest `Bpod device <https://sanworks.io/shop/viewproduct?productID=1011>`_ version.

This project is maintained by a team of SW developers at the `Champalimaud Foundation <http://research.fchampalimaud.org>`_. Please find more information on section :ref:`Project Info <project-info-label>`.

What is Bpod?
-------------

.. image:: /_images/pybpodapi-logo.png
   :scale: 100 %


**Bpod** is a system from `Sanworks <https://sanworks.io/index.php>`_ for precise measurement of small animal behavior.
It is a family of open source hardware devices which includes also software and firmware to control these devices. The software was originally developed in Matlab providing retro-compatibility with the `BControl <http://brodywiki.princeton.edu/bcontrol/index.php/Main_Page>`_ system.

.. seealso::

    Bpod device: https://sanworks.io/shop/viewproduct?productID=1011

    Bpod on Github: https://github.com/sanworks/Bpod

    Bpod Wiki: https://sites.google.com/site/bpoddocumentation/

    BControl project: http://brodywiki.princeton.edu/bcontrol/index.php/Main_Page/


Why a Python port?
------------------
Python is one of the most popular programming languages today `[1] <https://pypl.github.io/PYPL.html>`_. This is special true for the science research community because it is an open language, easy to learn, with a strong support community and with a lot of libraries available.

Questions?
==========
If you have any questions or want to report a problem with this library please fill a issue `here <https://bitbucket.org/fchampalimaud/pybpod-api/issues>`_.

.. high level toc tree

.. toctree::
   :hidden:
   :maxdepth: 2
   :includehidden:
   :caption: Getting started

   Introduction <self>
   getting_started/installing
   getting_started/basic_usage
   getting_started/writing_protocols

.. toctree::
   :hidden:
   :maxdepth: 2
   :includehidden:
   :caption: Contributing

   contributing/contributing
   contributing/developing_plugins

.. toctree::
   :hidden:
   :maxdepth: 4
   :includehidden:
   :caption: API reference

   api_reference/pybpodgui_plugin/index
   api_reference/diagrams

.. toctree::
   :hidden:
   :maxdepth: 4
   :includehidden:
   :caption: About

   about/about

.. toctree::
   :hidden:
   :maxdepth: 2
   :includehidden:
   :caption: Contents

   contents

