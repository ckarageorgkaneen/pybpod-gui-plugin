# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pybpodgui_plugin.com.messaging import BoardMessage


class EventOccurrence(BoardMessage):
	"""
	Message from board that represents state change (an event)

	:ivar str event_name: name of the event
	:ivar int event_id: index of the event
	:ivar float board_timestamp: timestamp associated with this event (from bpod)

	"""

	MESSAGE_TYPE_ALIAS = 'event_occurrence'

	def __init__(self, event_name, event_timestamp, event_id):
		"""

		:param event_name:
		:param event_timestamp:
		:param event_id:
		"""
		self.event_name = event_name
		self.event_id = int(event_id)

		BoardMessage.__init__(self, board_timestamp=event_timestamp,
		                      content="{0} ({1}): {2}".format(event_name, event_id, event_timestamp))

		# TEMPORARY FIX BECAUSE BPOD DOESN'T SEND TIMESTAMPS BEFORE TRIAL ENDS
		self.board_timestamp = self.pc_timestamp

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

	def export(self):
		return "{msg_type}, {pc_timestamp}, {event_id}, {event_name}, {event_timestamp}\n".format(
			msg_type=self.MESSAGE_TYPE_ALIAS,
			pc_timestamp=self._pc_timestamp.isoformat(), event_id=self.event_id,
			event_name=self.event_name, event_timestamp=self.board_timestamp)
