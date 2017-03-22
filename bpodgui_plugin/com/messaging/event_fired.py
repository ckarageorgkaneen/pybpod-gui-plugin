# !/usr/bin/python3
# -*- coding: utf-8 -*-

from bpodgui_plugin.com.messaging.board_message import BoardMessage


class EventFired(BoardMessage):
	"""Message from board that represents an event fired"""

	MESSAGE_TYPE_ALIAS = 'event_fired'

	def __init__(self, event_name, event_timestamp, event_id):

		self.board_timestamp = event_timestamp
		self.event_id = event_id
		self.event_name = event_name

		self.format_string = "{0}: {1}".format(event_name, event_timestamp)
		self.content = self.format_string

		super(EventFired, self).__init__(content="",
		                                 format_string='{0} {1} {2}'.format(self.board_timestamp, self.event_id,
		                                                                    self.event_name))

