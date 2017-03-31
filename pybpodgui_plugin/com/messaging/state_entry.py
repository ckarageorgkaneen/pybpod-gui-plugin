# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pybpodgui_plugin.com.messaging import BoardMessage


class StateEntry(BoardMessage):
	""" Message from board that represents a state entry"""

	MESSAGE_TYPE_ALIAS = 'state_entry'

	def __init__(self, state_name, start_timestamp, end_timestamp, state_id):
		"""

		:param str state_name:
		:param float start_timestamp:
		:param float end_timestamp:
		:param int state_id:
		"""

		self.state_id = state_id # type: int
		self.state_name = state_name # type: str
		self.start_timestamp = start_timestamp # type: float
		self.end_timestamp = end_timestamp # type: float

		BoardMessage.__init__(self, board_timestamp=self.start_timestamp,
		                      content="{0}: {1} --> {2}".format(state_name, self.start_timestamp, self.end_timestamp))

	@property
	def start_timestamp(self):
		return self._start_timestamp

	@start_timestamp.setter
	def start_timestamp(self, value):
		self._start_timestamp = value

	@property
	def end_timestamp(self):
		return self._end_timestamp

	@end_timestamp.setter
	def end_timestamp(self, value):
		self._end_timestamp = value

	@property
	def state_id(self):
		return self._state_id

	@state_id.setter
	def state_id(self, value):
		self._state_id = value

	def export(self):
		return "{msg_type}, {pc_timestamp}, {state_id}, {state_name}, {start_timestamp}, {end_timestamp}\n".format(
			msg_type=self.MESSAGE_TYPE_ALIAS,
			pc_timestamp=self._pc_timestamp.isoformat(), state_id=self.state_id,
			state_name=self.state_name, start_timestamp=self.start_timestamp, end_timestamp=self.end_timestamp)
