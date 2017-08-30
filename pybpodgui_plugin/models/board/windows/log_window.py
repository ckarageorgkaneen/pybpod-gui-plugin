#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pysettings import conf

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtCore import QTimer
else:
	from PyQt4.QtCore import QTimer

from pyforms import BaseWidget
from pyforms.Controls import ControlTextArea
from pyforms.Controls import ControlCheckBox
from pyforms.Controls import ControlButton

from pybranch.com.messaging.debug import DebugMessage
from pybpodgui_plugin.api.exceptions.run_setup import RunSetupError

logger = logging.getLogger(__name__)


class LogWindow(BaseWidget):
	def __init__(self, board):
		BaseWidget.__init__(self, board.name)
		self.board = board
		self.layout().setContentsMargins(5, 5, 5, 5)

		self._debug_checkbox = ControlCheckBox('Show detailed log')
		self._debug_checkbox.changed_event = self.reset_history

		self._refresh_button = ControlButton('Reset')
		self._refresh_button.value = self.reset_history

		self._log = ControlTextArea()
		self._log.readOnly = True

		self._session_history_index = 0
		self._read_active = True

		self._timer = QTimer()
		self._timer.timeout.connect(self.read_message_queue)

		self.formset = [(' ', '_debug_checkbox', '_refresh_button'), '_log']

	def show(self):
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

	def reset_history(self):
		self._session_history_index = 0
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
