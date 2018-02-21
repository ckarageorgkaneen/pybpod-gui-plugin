# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import traceback, sys

from pyforms import conf

from pybpodgui_api.models.setup import Setup

from pybpodgui_plugin.com.async.qt_async_bpod import QtAsyncBpod
from pybpodgui_plugin.models.board.board_window import BoardWindow

logger = logging.getLogger(__name__)


class BoardCom(QtAsyncBpod, BoardWindow):
	"""
	Board communication logic. Define here actions that can be triggered on board.

	.. seealso::
		This class heavy relies on the corresponding API module.

		:py:class:`pybpodgui_api.models.board.board_com.BoardCom`

	**Methods**

	"""

	def __init__(self, project=None):
		BoardWindow.__init__(self, project)

	##########################################################################
	####### FUNCTIONS ########################################################
	##########################################################################

	def run_task(self, session, board_task, workspace_path, detached=False):
		"""
		Bases: :meth:`pybpodgui_api.models.board.board_com.BoardCom.run_task`

		Start running task on board by invoking API

		:param session:
		:param board_task: board and task object
		:return: True if no problems occur, False otherwise.
		"""
		flag = None
		self._enable_btn_flag = True
		self._tmp_setup = session.setup
		try:
			flag = super(BoardCom, self).run_task(session, board_task, workspace_path, detached)
		except Exception:
			board_task.setup.status = Setup.STATUS_READY
			self.status = self.STATUS_READY
			raise
		return flag

	def run_task_handler_evt(self, e, result):
		"""
		Bases: :meth:`pybpodgui_api.models.board.board_com.BoardCom.run_task_handler_evt`

		Call API corresponding method and handle "run task" action errors on UI.
		"""
		try:
			super(BoardCom, self).run_task_handler_evt(e, result)

			called_operation = e.extra_args[0]

			if called_operation == BoardCom.STATUS_RUNNING_TASK:
				self.project.update_ui()

		except Exception as err:
			if self._running_session:
				self._running_session.setup.stop_task()

			self._running_session = None
			self._running_task 	  = None

			logger.error(traceback.format_exc())
			self.alert(self, str(err), "Error")
