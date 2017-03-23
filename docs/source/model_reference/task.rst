*****
Task
*****

.. contents:: Contents
    :local:

Overview
========

A task defines the state machine code. The task UI enables to edit task fields from model (pycontrol-api) and execute operations such as edit task code.

Screenshots
===========

Details section
    This section contains task properties and available operations.

    .. image:: /_images/task_details.png

Tree node
    Each task instance will appear as tree node below the "Tasks" parent node.

    .. image:: /_images/task_treenode.png

Task Code Editor
    Edit state machine code using a code editor with syntax highlighting.

    .. image:: /_images/task_code_editor.png

Implementation
==============

::

    Task = type(
        'Task',
        tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.task.Task') + [TaskDockWindow]),
        {}
    )



.. inheritance-diagram:: pybpodgui_plugin.models.task.task_dockwindow
    :parts: 1

Window fields
-------------

.. automodule:: pybpodgui_plugin.models.task.task_window
    :members:
    :show-inheritance:
    :private-members:

Tree management
---------------

.. automodule:: pybpodgui_plugin.models.task.task_treenode
    :members:
    :show-inheritance:
    :private-members:

Dock window
-----------

.. automodule:: pybpodgui_plugin.models.task.task_dockwindow
    :members:
    :show-inheritance:
    :private-members: