# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pybpodgui_plugin.com.messaging import HistoryMessage


class PrintStatement(HistoryMessage):
	"""
	Print statement on bpod protocol
	"""

	MESSAGE_TYPE_ALIAS = 'print_statement'

	def __init__(self, message):
		super(PrintStatement, self).__init__(content=message)

	@property
	def print_statement(self):
		return self._print_statement

	@print_statement.setter
	def print_statement(self, value):
		self._print_statement = value
