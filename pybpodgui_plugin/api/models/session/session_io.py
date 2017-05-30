# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import datetime

from pybpodgui_plugin.api.models.session.session_base import SessionBase
from pybpodgui_plugin.api.exceptions.invalid_session import InvalidSessionError
from pybpodgui_plugin.com.messaging.msg_factory import parse_session_msg


class SessionIO(SessionBase):
	"""

	"""

	def save(self, parent_path):
		"""

		:param parent_path:
		:return:
		"""
		filename = os.path.basename(self.path).replace('.txt', '')
		filepath = os.path.dirname(self.path)

		if filename != self.name or filepath != parent_path:
			new_path = os.path.join(parent_path, self.name + '.txt')
			os.rename(self.path, new_path)
			self.path = new_path

	def load(self, session_path, data):
		"""

		:param session_path:
		:param data:
		:return:
		"""
		self.name = os.path.basename(session_path).replace('.txt', '')

		self.path = session_path

	def load_contents(self, session_path):
		"""
		Parses session history file, line by line and populates the history message on memory.

		:param str session_path: path to session history file
		"""
		with open(session_path, "r") as f:
			for line in f:
				message = parse_session_msg(line)
				if message:
					self.messages_history.append(message)
