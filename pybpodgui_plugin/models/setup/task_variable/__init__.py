# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf

from pybpodgui_plugin.models.setup.task_variable.task_variable_window import TaskVariableWindow

TaskVariable = type(
    'TaskVariable',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.setup.task_variable.TaskVariable') + [TaskVariableWindow]),
    {}
)