# !/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from pyforms_generic_editor.com.messaging.history_message import HistoryMessage


class BoardMessage(HistoryMessage):
	"""
	Represents a message output from the board

	:ivar datetime board_timestamp: board timestamp

	"""

	MESSAGE_TYPE_ALIAS = 'board_message'

	def __init__(self, board_timestamp, content, format_string=None):
		self.board_timestamp = board_timestamp

		HistoryMessage.__init__(self, content=content, format_string=format_string)

	@property
	def board_timestamp(self):
		return self._board_timestamp

	@board_timestamp.setter
	def board_timestamp(self, value):
		self._board_timestamp = value
