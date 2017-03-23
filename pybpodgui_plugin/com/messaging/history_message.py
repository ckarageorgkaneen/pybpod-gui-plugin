#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime


class HistoryMessage(object):
	"""
	Represents a session message
	It may have been originated from the board of from pc
	"""

	MESSAGE_TYPE_ALIAS = None

	def __init__(self, content, format_string=None):
		self.pc_timestamp = datetime.now()
		self.content = content

		if format_string:
			self.format_string = format_string
		else:
			self.format_string = content

		if not self.MESSAGE_TYPE_ALIAS:
			self.MESSAGE_TYPE_ALIAS = 'history_message'

	def __unicode__(self):
		return "{0}: {1}".format(self._pc_timestamp.strftime('%Y%m%d_%H%M%S'), self.format_string)

	def __str__(self):
		return self.__unicode__()

	@property
	def content(self):
		return self._content

	@content.setter
	def content(self, value):
		self._content = value

	@property
	def pc_timestamp(self):
		return self._pc_timestamp

	@pc_timestamp.setter
	def pc_timestamp(self, value):
		self._pc_timestamp = value

	@property
	def format_string(self):
		return self._format_string

	@format_string.setter
	def format_string(self, value):
		self._format_string = value
