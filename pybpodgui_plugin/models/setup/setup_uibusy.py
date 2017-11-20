# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pysettings import conf

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtGui import QIcon
else:
	from PyQt4.QtGui import QIcon

from pybpodgui_api.models.setup import Setup
from pybpodgui_plugin.models.setup.setup_com import SetupCom

logger = logging.getLogger(__name__)


class SetupUIBusy(SetupCom):
	"""
	Extends setup with UI refreshment logic.

	.. seealso::
		UI buttons: :py:class:`pybpodgui_plugin.models.setup.setup_window.SetupWindow`.

	**Methods**

	"""

	def update_ui(self):
		"""
		Update UI button states and labels and tree icons when board communication is active.
		"""
		if not hasattr(self, 'node'): return

		logger.debug('Setup [{0}] status: {1}'.format(self.name, self.status))

		if self.status == Setup.STATUS_READY:

			self.node.setIcon(0, QIcon(conf.BOX_SMALL_ICON))

			self._run_task_btn.label = 'Run'

			if self.board:
				self.enable_all_task_buttons()
			else:
				self.disable_all_task_buttons()

			self._board.enabled = True

		elif self.status == Setup.STATUS_BOARD_LOCKED:

			self.node.setIcon(0, QIcon(conf.BUSY_SMALL_ICON))
			self.disable_all_task_buttons()
			self._board.enabled = False

		elif self.status == Setup.STATUS_INSTALLING_TASK:

			self.node.setIcon(0, QIcon(conf.PLAY_SMALL_ICON))
			self.disable_all_task_buttons()
			self._board.enabled = False

		elif self.status == Setup.STATUS_SYNCING_VARS:

			self.node.setIcon(0, QIcon(conf.PLAY_SMALL_ICON))
			self.disable_all_task_buttons()
			self._board.enabled = False

		elif self.status == Setup.STATUS_RUNNING_TASK:

			self.node.setIcon(0, QIcon(conf.PLAY_SMALL_ICON))
			self.disable_all_task_buttons()
			self._board.enabled = False

		elif self.status == Setup.STATUS_RUNNING_TASK_HANDLER:

			self.node.setIcon(0, QIcon(conf.PLAY_SMALL_ICON))
			self._run_task_btn.label = 'Stop'
			self._run_task_btn.enabled = True

		elif self.status == Setup.STATUS_RUNNING_TASK_ABOUT_2_STOP:

			self.node.setIcon(0, QIcon(conf.PLAY_SMALL_ICON))
			self._run_task_btn.enabled = False
			self._run_task_btn.label = 'Stop'

		self.board_task.update_ui()
		if self.last_session: self.last_session.update_ui()

	def enable_all_task_buttons(self):
		"""
		Enable UI buttons for upload task, configure task and run task
		"""
		self._run_task_btn.enabled = True

	def disable_all_task_buttons(self):
		"""
		Disable UI buttons for upload task, configure task and run task
		"""
		self._run_task_btn.enabled = False
