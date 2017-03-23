# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pybpodgui_plugin.com.messaging.board_message import BoardMessage


class EventFired(BoardMessage):
	"""Message from board that represents an event fired"""

	MESSAGE_TYPE_ALIAS = 'event_fired'

	def __init__(self, event_name, event_timestamp, event_id):
		self.board_timestamp = event_timestamp
		self.event_id = event_id
		self.event_name = event_name

		super(EventFired, self).__init__(content="{0}: {1}".format(event_name, event_timestamp),
		                                 format_string="{0}: {1}".format(event_name, event_timestamp))

	@property
	def event_name(self):
		""" Event name """
		return self._event_name

	@event_name.setter
	def event_name(self, value):
		"""
		event name setter
		:param value: event name
		:type value: string
		"""
		self._event_name = value

	@property
	def event_id(self):
		""" Event id """
		return self._event_id

	@event_id.setter
	def event_id(self, value):
		"""
		event id setter
		:param value: event id
		:type value: string
		"""
		self._event_id = value
