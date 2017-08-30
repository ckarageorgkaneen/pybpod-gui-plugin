# !/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import logging
import os
import uuid

from pysettings import conf

from pybpodgui_plugin.com.async.async_bpod import AsyncBpod

from pybpodgui_plugin.api.models.board.board_io import BoardIO
from pybpodgui_plugin.api.models.board.board_operations import BoardOperations
from pybpodgui_plugin.com.messaging.msg_factory import parse_board_msg
from pybpodgui_plugin.api.models.setup.board_task import BoardTask  # used for type checking

from pybpodgui_plugin.api.exceptions.board_error import BoardError
from pybpodgui_plugin.api.exceptions.pycontrol_error import PycontrolError

logger = logging.getLogger(__name__)


class BoardCom(AsyncBpod, BoardIO):
	#### SETUP STATUS ####
	STATUS_READY = 0
	STATUS_INSTALLING_FRAMEWORK = 1  # The board is busy installing the framework
	STATUS_INSTALLING_TASK = 2  # The board is busy installing a task
	STATUS_SYNCING_VARS = 3  # The board is busy syncing variables
	STATUS_RUNNING_TASK = 4  # The board is busy running a task

	INSTALL_FRAMEWORK_TAG = 'Install framework'
	UPLOAD_TASK_TAG = 'Upload task'
	SYNC_VARIABLES_TAG = 'Sync variables'
	RUN_TASK_TAG = 'Run task'

	CONSOLE_COMMENT_LEVEL1_TAG = '#1'
	CONSOLE_COMMENT_LEVEL2_TAG = '#2'
	CONSOLE_ERROR_TAG = '!'

	def __init__(self, project):
		BoardIO.__init__(self, project)
		AsyncBpod.__init__(self)
		self.status = BoardCom.STATUS_READY

	##########################################################################
	####### PROPERTIES #######################################################
	##########################################################################

	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, value):
		self._status = value

	##########################################################################
	####### FUNCTIONS ########################################################
	##########################################################################

	def log_msg_error(self, msg):
		tag_msg = '{0} {1}'.format(self.CONSOLE_ERROR_TAG, msg)  # adds sign to indicate message type
		self.log_msg(tag_msg)

	def log_msg_level1(self, msg):
		tag_msg = '{0} {1}'.format(self.CONSOLE_COMMENT_LEVEL1_TAG, msg)  # adds sign to indicate message type
		self.log_msg(tag_msg)

	def log_msg_level2(self, msg):
		tag_msg = '{0} {1}'.format(self.CONSOLE_COMMENT_LEVEL2_TAG, msg)  # adds sign to indicate message type
		self.log_msg(tag_msg)

	def log_msg(self, msg):
		parsed_messages = parse_board_msg(msg)

		for m in parsed_messages:
			logger.debug("Logging message: %s", m)
			self.log_messages.append(m)
		# logger.debug(msg)

	def log_session_history(self, msg):
		"""
		Log session history on file and on memory
		We could read the file while writing at the same time
		but this would be a more complex approach
		:param session:
		:param board_task:
		:param msg:
		:return:
		"""
		self._running_session.log_msg(msg)

	def unique_id(self, handler_evt=None):
		if handler_evt is None: handler_evt = self.unique_id_handler_evt
		super(BoardCom, self).unique_id(handler_evt)

	def unique_id_handler_evt(self, e, result):
		self.log_msg('I Board {0} ID: {1}'.format(self.name, result))

	def run_task(self, session, board_task, workspace_path):

		self.log_msg_level1("Running protocol now")

		func_group_id = uuid.uuid4()

		self._session_log_file = open(session.path, 'w+', newline='\n', buffering=1) 

		self._running_task = board_task.task
		self._running_session = session

		session.open()

		AsyncBpod.run_protocol(self,
		                       board_task.board.serial_port, board_task.task.name, board_task.task.path, workspace_path,
		                       handler_evt=self.run_task_handler_evt,
		                       extra_args=(BoardOperations.RUN_PROTOCOL,),
		                       group=func_group_id
		                       )

	def run_task_handler_evt(self, e, result):
		called_operation = e.extra_args[0]

		try:
			if called_operation == BoardOperations.RUN_PROTOCOL:
				if isinstance(result, Exception):
					self.log_msg_error(str(result))
					raise Exception("Unable to run protocol. Please check console for more info.")
				elif result is not None:
					self.log_msg(result)
					self.log_session_history(result)

			if e.last_call:
				self._running_session.close() 
				self._running_task = None
				self._running_session = None
		except Exception as err:
			self._running_session.close() 
			self._running_task = None
			self._running_session = None
			raise err
