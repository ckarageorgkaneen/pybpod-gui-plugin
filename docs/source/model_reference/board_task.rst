*********
BoardTask
*********

.. contents:: Contents
    :local:

Overview
========

The BoardTask aggregates information from a board, a task and a setup (a.k.a. subject).

Screenshots
===========

Setup configuration
    Visualize board and task information and sync variables.

    .. image:: /_images/setup_configuration.png

Implementation
==============

::

    BoardTask = type(
        'BoardTask',
        tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.setup.board_task.BoardTask') + [BoardTaskUIBusy]),
        {}
    )


.. inheritance-diagram:: pybpodgui_plugin.models.setup.board_task.board_task_uibusy
    :parts: 1

Window fields
-------------

.. automodule:: pybpodgui_plugin.models.setup.board_task.board_task_window
    :members:
    :show-inheritance:
    :private-members:


UI Refreshment
--------------

.. automodule:: pybpodgui_plugin.models.setup.board_task.board_task_uibusy
    :members:
    :show-inheritance:
    :private-members:
