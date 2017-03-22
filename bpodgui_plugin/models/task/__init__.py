# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf

from bpodgui_plugin.models.task.task_dockwindow import TaskDockWindow

Task = type(
	'Task',
	tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.task.Task') + [TaskDockWindow]),
	{}
)