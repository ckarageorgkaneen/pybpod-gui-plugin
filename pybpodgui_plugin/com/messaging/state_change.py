# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pyforms_generic_editor.com.messaging.board_message import BoardMessage


class StateChange(BoardMessage):
	"""Message from board that represents state change"""

	MESSAGE_TYPE_ALIAS = 'state_change'

	def __init__(self, event_name, event_timestamp, event_id):
		"""

		:param event_name:
		:param event_timestamp:
		:param event_id:
		"""
		self.event_id = event_id
		self.event_name = event_name

		BoardMessage.__init__(self, board_timestamp=event_timestamp,
		                      content="{0}: {1}".format(event_name, event_timestamp))

	@property
	def event_name(self):
		return self._event_name

	@event_name.setter
	def event_name(self, value):
		self._event_name = value

	@property
	def event_id(self):
		return self._event_id

	@event_id.setter
	def event_id(self, value):
		self._event_id = value
