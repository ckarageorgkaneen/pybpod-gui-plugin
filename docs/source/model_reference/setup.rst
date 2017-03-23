*****
Setup
*****

.. contents:: Contents
    :local:

Overview
========

The setup (or subject) holds subject information. The setup UI enables to edit setup information from model (pycontrol-api) and execute operations such as *upload task* or *run task*.

Screenshots
===========

Details section
    This section contains setup properties and available operations.

    .. image:: /_images/setup_details.png

Tree node
    Each setup instance will appear as a tree node below the corresponding experiment parent node.

    .. image:: /_images/setup_treenode.png

Implementation
==============

::

    Setup = type(
        'Setup',
        tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.setup.Setup') + [SetupUIBusy]),
        {}
    )


.. inheritance-diagram:: pybpodgui_plugin.models.setup.setup_uibusy
    :parts: 1

Window fields
-------------

.. automodule:: pybpodgui_plugin.models.setup.setup_window
    :members:
    :show-inheritance:
    :private-members:

Board Communication
-------------------

.. automodule:: pybpodgui_plugin.models.setup.setup_com
    :members:
    :show-inheritance:
    :private-members:

Tree management
---------------

.. automodule:: pybpodgui_plugin.models.setup.setup_treenode
    :members:
    :show-inheritance:
    :private-members:

Dock window
-----------

.. automodule:: pybpodgui_plugin.models.setup.setup_dockwindow
    :members:
    :show-inheritance:
    :private-members:

UI Refreshment
--------------

.. automodule:: pybpodgui_plugin.models.setup.setup_uibusy
    :members:
    :show-inheritance:
    :private-members:
