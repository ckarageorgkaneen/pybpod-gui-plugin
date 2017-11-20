# !/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

from pysettings import conf

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtGui import QIcon
else:
	from PyQt4.QtGui import QIcon

from pybpodgui_api.models.setup import Setup
from pybpodgui_plugin.models.setup.board_task.board_task_window import BoardTaskWindow

logger = logging.getLogger(__name__)


class BoardTaskUIBusy(BoardTaskWindow):
	"""
	TODO
	"""

	def __init__(self, setup):
		super(BoardTaskUIBusy, self).__init__(setup)
		self.__running_icon = QIcon(conf.PLAY_SMALL_ICON)

	def update_ui(self):

		pass