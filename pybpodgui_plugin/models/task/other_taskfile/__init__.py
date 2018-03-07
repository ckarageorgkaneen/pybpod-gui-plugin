# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pyforms import conf

from pybpodgui_plugin.models.task.other_taskfile.other_taskfile_dockwindow import OtherTaskTaskDockWindow

OtherTaskFile = type(
    'OtherTaskFile',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.task.other_taskfile.OtherTaskFile') + [OtherTaskTaskDockWindow]),
    {}
)
