# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging, time
import traceback
from serial.serialutil import SerialException

from PyQt4 import QtGui

from pysettings import conf

from bpodgui_plugin.api.models.setup import Setup
from bpodgui_plugin.api.models.board.board_operations import BoardOperations

from bpodgui_plugin.com.async.qt_async_pyboard import QtAsyncPyboard
from bpodgui_plugin.models.board.board_window import BoardWindow

logger = logging.getLogger(__name__)


class BoardCom(QtAsyncPyboard, BoardWindow):
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

	def install_framework(self, framework_path=None, devices_path=None):
		"""
		Bases: :meth:`pycontrolapi.model.board.board_com.ComBoard.install_framework`

		Start installing framework on board by invoking API

		:param str framework_path: path to framework
		:param str devices_path: path to devices
		:return: True if no problems occur, False otherwise.
		"""
		try:
			super(BoardCom, self).install_framework(framework_path, devices_path)
		except SerialException:
			QtGui.QMessageBox.critical(self, "Error when trying to install the framework", traceback.format_exc())
			self.status = self.STATUS_READY
			return False
		except FileNotFoundError as err:
			QtGui.QMessageBox.critical(self, "Could not find framework. Is it specified?", str(err))
			self.status = self.STATUS_READY
			return False
		except Exception as err:
			QtGui.QMessageBox.critical(self, "Unknown error found", str(err))
			self.status = self.STATUS_READY
			return False

		return True

	def install_framework_handler_evt(self, e, result):
		"""
		Bases: :meth:`pycontrolapi.model.board.board_com.ComBoard.install_framework_handler_evt`

		Call API corresponding method and handle "install framework" action errors on UI.
		"""
		try:
			super(BoardCom, self).install_framework_handler_evt(e, result)
		except Exception as err:
			self.status = self.STATUS_READY
			QtGui.QMessageBox.critical(self, "Error", str(err))

	def upload_task(self, board_task):
		"""
		Bases: :meth:`pycontrolapi.model.board.board_com.ComBoard.upload_task`

		Start uploading task on board by invoking API

		:param str board_task: board and task object
		:return: True if no problems occur, False otherwise.
		"""
		try:
			super(BoardCom, self).upload_task(board_task)
		except SerialException:
			QtGui.QMessageBox.critical(self, "Error when trying to install the task", traceback.format_exc())
			board_task.setup.status = Setup.STATUS_READY
			self.status = BoardCom.STATUS_READY
			return False
		return True

	def upload_task_handler_evt(self, e, result):
		"""
		Bases: :meth:`pycontrolapi.model.board.board_com.ComBoard.upload_task_handler_evt`

		Call API corresponding method and handle "upload task" action errors on UI.
		"""
		try:
			super(BoardCom, self).upload_task_handler_evt(e, result)
		except Exception as err:
			QtGui.QMessageBox.critical(self, "Error", str(err))
			board_task = e.extra_args[1]

	def sync_variables(self, board_task, func_group_id=None):
		"""
		Bases: :meth:`pycontrolapi.model.board.board_com.ComBoard.sync_variables`

		Start syncing variables on board by invoking API

		:param str board_task: board and task object
		:param int func_group_id:
		:return: True if no problems occur, False otherwise.
		"""
		super(BoardCom, self).sync_variables(board_task, func_group_id=func_group_id)

	def sync_variables_handler_evt(self, e, result):
		"""
		Bases: :meth:`pycontrolapi.model.board.board_com.ComBoard.sync_variables_handler_evt`

		Call API corresponding method and handle "sync variables" action errors on UI.
		"""
		try:
			super(BoardCom, self).sync_variables_handler_evt(e, result)
		except Exception as err:
			QtGui.QMessageBox.critical(self, "Error", str(err))

	def run_task(self, session, board_task):
		"""
		Bases: :meth:`pycontrolapi.model.board.board_com.ComBoard.run_task`

		Start running task on board by invoking API

		:param session:
		:param board_task: board and task object
		:return: True if no problems occur, False otherwise.
		"""
		if len(board_task.events) == 0 or len(board_task.states) == 0:
			QtGui.QMessageBox.about(self, "Task events or states missing",
			                        "No states or events where found in the task.")
			return None

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

			if e.extra_args[0] == BoardOperations.RUNTASK_PRINT_STATES: self.project.update_ui()

		except Exception as err:
			session = e.extra_args[1]
			session.setup.stop_task()

			logger.error(traceback.format_exc())
			QtGui.QMessageBox.critical(self, "Error", str(err))
