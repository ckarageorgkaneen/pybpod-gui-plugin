# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import logging

from pysettings import conf

import pyforms as app
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton

from bpodgui_plugin.api.models.board import Board

logger = logging.getLogger(__name__)


class BoardWindow(Board, BaseWidget):
	"""
	Define here which fields from the board model should appear on the details section.

	The model fields shall be defined as UI components like text fields, buttons, combo boxes, etc.

	You may also assign actions to these components.

	**Properties**

		name
			:class:`string`

			Name associated with this board. Returns the current value stored in the :py:attr:`_name` text field.

		serial_port
			:class:`string`

			Serial port associated with this board. Returns the current value stored in the :py:attr:`_serial_port` text field.


	**Private attributes**

		_name
			:class:`pyforms.Controls.ControlText`

			Text field to edit board name. Editing this field fires the event :meth:`BoardWindow._BoardWindow__name_changed_evt`.

		_serial_port
			:class:`pyforms.Controls.ControlText`

			Text field to edit serial port. Editing this field fires the event :meth:`BoardWindow._BoardWindow__serial_changed_evt`.

		_edit_framework_btn
			:class:`pyforms.Controls.ControlButton`

			Button to edit framework code. Pressing the button fires the event :class:`BoardDockWindow._BoardDockWindow__edit_framework_btn`.

		_install_framework_btn
			:class:`pyforms.Controls.ControlButton`

			Button to install framework on board. Pressing the button fires the event :class:`BoardWindow._BoardWindow__install_framework_btn_evt`.

		_log_btn
			:class:`pyforms.Controls.ControlButton`

			Button to show this board events on a console window. Pressing the button fires the event :class:`BoardDockWindow.open_log_window`.

		_formset
			Describe window fields organization to PyForms.

	**Methods**

	"""

	def __init__(self, project=None):
		"""

		:param project: project where this board belongs
		:type project: pycontrolgui.models.project.Project
		"""
		BaseWidget.__init__(self, 'Board')
		self.layout().setContentsMargins(5,10,5,5)

		self._name = ControlText('Box name')
		self._serial_port = ControlText('Serial port')
		self._log_btn = ControlButton('Console')

		Board.__init__(self, project)

		self._formset = [
			'_name',
			'_serial_port',
			(' ', ' ', '_log_btn'),
			' '
		]

		self._name.changed_event = self.__name_changed_evt
		self._serial_port.changed_event = self.__serial_changed_evt

	def __name_changed_evt(self):
		"""
		React to changes on text field :py:attr:`_name`.

		This methods is called every time the user changes the field.
		"""
		if not hasattr(self, '_update_name') or not self._update_name:
			self.name = self._name.value

	def __serial_changed_evt(self):
		"""
		React to changes on text field :py:attr:`_serial_port`.

		This methods is called every time the user changes the field.
		"""

		if not hasattr(self, '_update_serial') or not self._update_serial:
			self.serial_port = self._update_serial.value

	@property
	def name(self):
		return self._name.value

	@name.setter
	def name(self, value):
		self._update_name = True  # Flag to avoid recursive calls when editing the name text field
		self._name.value = value
		self._update_name = False

	@property
	def serial_port(self):
		return self._serial_port.value

	@serial_port.setter
	def serial_port(self, value):
		self._update_serial = True  # Flag to avoid recursive calls when editing the name text field
		self._serial_port.value = value
		self._update__serial = False

	


# Execute the application
if __name__ == "__main__":
	app.start_app(BoardWindow)
