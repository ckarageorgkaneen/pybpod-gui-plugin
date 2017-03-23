**********
Experiment
**********

.. contents:: Contents
    :local:

Overview
========

Every experiment runs inside a board. The board UI enables to edit board information on model (pycontrol-api) and execute operations such as *install framework*, visualize board messages and edit framework code.

Screenshots
===========

Details section
    This section contains experiment properties and available operations.

    .. image:: /_images/experiment_details.png

Tree node
    Each experiment instance will appear as tree node below the "Experiments" parent node.

    .. image:: /_images/experiment_treenode.png


Implementation
==============

::

    Experiment = type(
        'Experiment',
        tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.experiment.Experiment') + [ExperimentUIBusy]),
        {}
    )


.. inheritance-diagram:: pybpodgui_plugin.models.experiment.experiment_uibusy
    :parts: 1

Window fields
-------------

.. automodule:: pybpodgui_plugin.models.experiment.experiment_window
    :members:
    :show-inheritance:
    :private-members:

Tree management
---------------

.. automodule:: pybpodgui_plugin.models.experiment.experiment_treenode
    :members:
    :show-inheritance:
    :private-members:

Dock window
-----------

.. automodule:: pybpodgui_plugin.models.experiment.experiment_dockwindow
    :members:
    :show-inheritance:
    :private-members:

UI refreshment
--------------

.. automodule:: pybpodgui_plugin.models.experiment.experiment_uibusy
    :members:
    :show-inheritance:
    :private-members:

