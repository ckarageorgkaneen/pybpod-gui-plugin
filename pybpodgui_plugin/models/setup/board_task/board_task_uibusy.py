# !/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

from pysettings import conf

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtGui import QIcon
else:
	from PyQt4.QtGui import QIcon

from pybpodgui_plugin.api.models.setup import Setup
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

		if self.setup.status == Setup.STATUS_BOARD_LOCKED:

			self._sync_btn.enabled = False

		elif self.setup.status not in [Setup.STATUS_READY, Setup.STATUS_BOARD_LOCKED]:

			self._sync_btn.enabled = False
			self._vars.enabled = False
			self._states.enabled = False
			self._events.enabled = False
			self._load_btn.enabled = False

		else:

			self._sync_btn.enabled = True
			self._vars.enabled = True
			self._states.enabled = True
			self._events.enabled = True
			self._load_btn.enabled = True
