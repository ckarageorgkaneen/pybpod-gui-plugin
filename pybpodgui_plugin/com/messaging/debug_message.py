# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pybpodgui_plugin.com.messaging.history_message import HistoryMessage


class DebugMessage(HistoryMessage):
	""" Information line for things like experiment name , task name, board id, etc. """
	MESSAGE_TYPE_ALIAS = 'debug'
	DEBUG_LEVEL = 1

	def __init__(self, message):
		# 1 Run task | Running task now...
		# 2 Run task | $: fw.verbose = False
		message_segments = message.strip().split(' ')

		if message_segments[0] == '#2':
			self.DEBUG_LEVEL = 2

		self.debug_statement = " ".join(message_segments[1:])

		super(DebugMessage, self).__init__(content=message, format_string=self.debug_statement)

	@property
	def debug_statement(self):
		return self._debug_statement

	@debug_statement.setter
	def debug_statement(self, value):
		self._debug_statement = value
