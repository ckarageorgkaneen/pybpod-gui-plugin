# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import datetime
import logging

from pyforms_generic_editor.com.messaging.board_message import BoardMessage
from pybpodgui_plugin.com.messaging.msg_factory import parse_board_msg

logger = logging.getLogger(__name__)


class SessionBase(object):
	"""
	Represents a board running session
	"""

	def __init__(self, setup):
		setup += self
		self.setup = setup
		self.name = "{0}".format(datetime.datetime.now().strftime('%d%m%Y_%H%M%S'))
		self.path = os.path.join(self.setup.path, "{0}.txt".format(self.name))
		self.setup_name = setup.name
		self.board_name = setup.board.name if setup.board else None
		self.task_name = setup.task.name if setup.task else None
		self.board_serial_port = setup.board.serial_port if setup.board else None
		self.started = datetime.datetime.now()
		self.ended = None
		self.messages_history = []

	##########################################################################
	####### PROPERTIES #######################################################
	##########################################################################

	def remove(self):
		pass

	def log_msg(self, msg, file_obj):
		parsed_messages = parse_board_msg(msg)

		for m in parsed_messages:
			if issubclass(type(m), BoardMessage):
				file_obj.write(str(m))
				self.messages_history.append(m)

	@property
	def setup(self):
		return self._setup

	@setup.setter
	def setup(self, value):
		self._setup = value

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, value):
		self._path = value

	@property
	def setup_name(self):
		return self._setup_name

	@setup_name.setter
	def setup_name(self, value):
		self._setup_name = value

	@property
	def board_name(self):
		return self._board_name

	@board_name.setter
	def board_name(self, value):
		self._board_name = value

	@property
	def task_name(self):
		return self._task_name

	@task_name.setter
	def task_name(self, value):
		self._task_name = value

	@property
	def board_serial_port(self):
		return self._board_serial_port

	@board_serial_port.setter
	def board_serial_port(self, value):
		self._board_serial_port = value

	@property
	def started(self):
		return self._started

	@started.setter
	def started(self, value):
		self._started = value

	@property
	def ended(self):
		return self._ended

	@ended.setter
	def ended(self, value):
		self._ended = value

	@property
	def messages_history(self):
		return self._messages_history

	@messages_history.setter
	def messages_history(self, value):
		self._messages_history = value

	@property
	def project(self):
		return self.setup.project

	@property
	def task(self):
		return self.setup.task
