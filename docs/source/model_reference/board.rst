*****
Board
*****

.. contents:: Contents
    :local:

Overview
========

Every experiment runs inside a board. The board UI enables to edit board information on model (pycontrol-api) and execute operations such as *install framework*, visualize board messages and edit framework code.

Screenshots
===========

Details section
    This section contains board properties and available operations.

    .. image:: /_images/board_details.png

Tree node
    Each board instance will appear as tree node below the "Boards" parent node.

    .. image:: /_images/board_treenode.png

Board Console
    Visualize board messages that come from the serial port.

    .. image:: /_images/board_console.png

Implementation
==============

::

    Board = type(
        'Board',
        tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.board.Board') + [BoardUIBusy]),
        {}
    )


.. inheritance-diagram:: pybpodgui_plugin.models.board.board_uibusy
    :parts: 1

Window fields
-------------

.. automodule:: pybpodgui_plugin.models.board.board_window
    :members:
    :show-inheritance:
    :private-members:

Board Communication
-------------------

.. automodule:: pybpodgui_plugin.models.board.board_com
    :members:
    :show-inheritance:
    :private-members:


Tree management
---------------

.. automodule:: pybpodgui_plugin.models.board.board_treenode
    :members:
    :show-inheritance:
    :private-members:

Dock window
-----------

.. automodule:: pybpodgui_plugin.models.board.board_dockwindow
    :members:
    :show-inheritance:
    :private-members:

UI Refreshment
--------------

.. automodule:: pybpodgui_plugin.models.board.board_uibusy
    :members:
    :show-inheritance:
    :private-members:
