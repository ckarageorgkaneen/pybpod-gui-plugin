# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pybpodgui_plugin.com.messaging.board_message import BoardMessage


class PrintStatement(BoardMessage):
	"""
	User generated print statement.
	If users want to use characters in their strings to indicate things
	like comments that is up to them but there is no specific support for this.
	"""

	MESSAGE_TYPE_ALIAS = 'print_statement'

	def __init__(self, message):
		super(PrintStatement, self).__init__(content=message, format_string=message)

	@property
	def print_statement(self):
		return self._print_statement

	@print_statement.setter
	def print_statement(self, value):
		self._print_statement = value
