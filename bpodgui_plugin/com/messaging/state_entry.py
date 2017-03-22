# !/usr/bin/python3
# -*- coding: utf-8 -*-

from bpodgui_plugin.com.messaging.state_entry import StateEntry


class StateEntry(StateEntry):
	""" Message from board that represents a state entry"""

	MESSAGE_TYPE_ALIAS = 'state_change'

	def __init__(self, state_name, state_timestamp, state_id):
		super(StateEntry, self).__init__(message="", board_timestamp=None, state_id=0, states_names=['asd'])

		self.board_timestamp = state_timestamp
		self.state_id = state_id
		self.state_name = state_name

		self.format_string = "{0}: {1}".format(state_name, state_timestamp)
		self.content = self.format_string
