#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pyforms import conf

from AnyQt.QtCore import QTimer

from pyforms import BaseWidget
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlCheckBox
from pyforms.controls import ControlButton

from pybranch.com.messaging.debug import DebugMessage
from pybpodgui_api.exceptions.run_setup import RunSetupError

from AnyQt.QtWidgets import QApplication

logger = logging.getLogger(__name__)


class LogWindow(BaseWidget):
	def __init__(self, board):
		BaseWidget.__init__(self, board.name)
		self.board = board
		self.layout().setContentsMargins(5, 5, 5, 5)

		self._autoscroll_checkbox = ControlCheckBox('Auto-scroll', default=True)
		self._autoscroll_checkbox.changed_event = self.__auto_scroll_evt

		self._refresh_button = ControlButton('Clear', default=self.__clear_log_evt)
		self._log 			 = ControlTextArea(readonly=True, autoscroll=False)

		self._session_history_index = 0
		self._read_active = True

		self._timer = QTimer()
		self._timer.timeout.connect(self.read_message_queue)

		self.formset = [(' ', '_autoscroll_checkbox', '_refresh_button'), '_log']

	def show(self):
		# show only the last 20 messages
		if self._session_history_index<(len(self.board.log_messages)-20):
			self._log += "\n\n...\n\n"
		self._session_history_index = len(self.board.log_messages)-20

		# Prevent the call to be recursive because of the mdi_area
		if hasattr(self, '_show_called'):
			BaseWidget.show(self)
			return
		self._show_called = True
		self.mainwindow.mdi_area += self
		del self._show_called

		self._timer.start(conf.BOARD_LOG_WINDOW_REFRESH_RATE)



	def hide(self):
		self._timer.stop()

	def beforeClose(self):
		self._timer.stop()
		return False

	def __auto_scroll_evt(self):
		self._log.autoscroll = self._autoscroll_checkbox.value

	def __clear_log_evt(self):
		self._log.value = ''

	def read_message_queue(self):
		""" Update board queue and retrieve most recent messages """
		recent_history = self.board.log_messages[self._session_history_index:]

		try:
			for message in recent_history:
				self._session_history_index += 1

				if isinstance(message, DebugMessage) and message.DEBUG_LEVEL == 2 and not self._debug_checkbox.value:
					pass
				else:

					self._log += "{idx} | {pc_timestamp} | {message_type} | {message}".format(
						idx=self._session_history_index,
						pc_timestamp=message.pc_timestamp.strftime(
							'%Y%m%d_%H%M%S'),
						message_type=message.MESSAGE_TYPE_ALIAS,
						message=str(message) )

					QApplication.processEvents()


		except RunSetupError as err:
			self._timer.stop()

	@property
	def title(self):
		return BaseWidget.title.fget(self)

	@title.setter
	def title(self, value):
		BaseWidget.title.fset(self, "{0} log".format(value))

	@property
	def mainwindow(self):
		return self.board.mainwindow
