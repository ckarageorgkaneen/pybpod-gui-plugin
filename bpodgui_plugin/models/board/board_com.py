# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging, time
import traceback
from serial.serialutil import SerialException

from PyQt4 import QtGui

from pysettings import conf

from bpodgui_plugin.api.models.setup import Setup
from bpodgui_plugin.api.models.board.board_operations import BoardOperations

from bpodgui_plugin.com.async.qt_async_bpod import QtAsyncBpod
from bpodgui_plugin.models.board.board_window import BoardWindow

logger = logging.getLogger(__name__)


class BoardCom(QtAsyncBpod, BoardWindow):
	"""
	Board communication logic. Define here actions that can be triggered on board.

	.. seealso::
		This class heavy relies on the corresponding API module.

		:py:class:`pycontrolapi.model.board.board_com.ComBoard`

	**Methods**

	"""

	def __init__(self, project=None):
		BoardWindow.__init__(self, project)

	##########################################################################
	####### FUNCTIONS ########################################################
	##########################################################################

	def run_task(self, session, board_task):
		"""
		Bases: :meth:`pycontrolapi.model.board.board_com.ComBoard.run_task`

		Start running task on board by invoking API

		:param session:
		:param board_task: board and task object
		:return: True if no problems occur, False otherwise.
		"""
		flag = None
		self._enable_btn_flag = True
		self._tmp_setup = session.setup
		try:
			flag = super(BoardCom, self).run_task(session, board_task)
		except Exception:
			board_task.setup.status = Setup.STATUS_READY
			self.status = self.STATUS_READY
			raise
		return flag

	def run_task_handler_evt(self, e, result):
		"""
		Bases: :meth:`pycontrolapi.model.board.board_com.ComBoard.run_task_handler_evt`

		Call API corresponding method and handle "run task" action errors on UI.
		"""
		try:
			super(BoardCom, self).run_task_handler_evt(e, result)

			called_operation = e.extra_args[0]

			if called_operation == BoardOperations.RUN_PROTOCOL:
				self.project.update_ui()

		except Exception as err:
			self._running_session.setup.stop_task()

			self._running_session = None
			self._running_task = None

			logger.error(traceback.format_exc())
			QtGui.QMessageBox.critical(self, "Error", str(err))
