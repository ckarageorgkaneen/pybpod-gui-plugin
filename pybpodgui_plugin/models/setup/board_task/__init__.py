# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf

from pybpodgui_plugin.models.setup.board_task.board_task_uibusy import BoardTaskUIBusy

BoardTask = type(
	'BoardTask',
	tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.setup.board_task.BoardTask') + [BoardTaskUIBusy]),
	{}
)
