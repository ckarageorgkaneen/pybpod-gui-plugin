#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from PyQt4 import QtGui

import pyforms as app
from pyforms import BaseWidget
from pyforms.Controls import ControlList
from pyforms.Controls import ControlButton

from pybpodgui_plugin.api.models.setup.board_task import BoardTask

logger = logging.getLogger(__name__)


class BoardTaskWindow(BoardTask, BaseWidget):
	"""
	Define here which fields from the board_task model should appear on the setup configuration window.

	The model fields shall be defined as UI components like text fields, buttons, combo boxes, etc.

	You may also assign actions to these components.

	.. seealso::
		This class heavy relies on the corresponding API module.

		:py:class:`pycontrolapi.model.setup.board_task.BoardTask`

	**Properties**

		states
			A list of task states associated with this BoardTask. States are defined on the task code.

		events
			A list of task events associated with this BoardTask. Events are defined on the task code.

		variables
			A list of task variables associated with this BoardTask. Variables are defined on the task code.

	**Private attributes**

		_states
			:class:`pyforms.Controls.ControlList`

			UI list to show BoardTask states.

		_events
			:class:`pyforms.Controls.ControlList`

			UI list to show BoardTask events.

		_vars
			:class:`pyforms.Controls.ControlList`

			UI list to show BoardTask variables.

		_sync_btn
			:class:`pyforms.Controls.ControlButton`

			Button to sync variables with board. Pressing the button fires the event :meth:`BoardTaskWindow.sync_variables`.

		_load_btn
			:class:`pyforms.Controls.ControlButton`

			Button to read task variables from board. Pressing the button fires the event :meth:`BoardTaskWindow._BoardTaskWindow__load_task_details`.

		_formset
			Describe window fields organization to PyForms.

	**Methods**

	"""

	def __init__(self, setup):
		BaseWidget.__init__(self, "Variables config for {0}".format(setup.name))
		self.layout().setMargin(5)

		self._vars = ControlList('Variables')
		self._states = ControlList('States')
		self._events = ControlList('Events')
		self._sync_btn = ControlButton('Sync variables')
		self._load_btn = ControlButton('Read task file')

		BoardTask.__init__(self, setup)

		self._vars.horizontalHeaders = ['NAME', 'VALUE', 'PERSISTENT']
		# self._vars.dataChangedEvent 	= self._table_task_variables_data_changed

		self._states.horizontalHeaders = ['ID', 'NAME']
		self._states.readOnly = True
		self._states.selectEntireRow = True

		self._events.horizontalHeaders = ['ID', 'NAME']
		self._events.readOnly = True
		self._events.selectEntireRow = True

		self._load_btn.value = self.__load_task_details
		self._sync_btn.value = self.sync_variables

		self._formset = [
			('_states', '_events'),
			'_vars',
			(' ', '_load_btn', '_sync_btn')
		]

	@property
	def states(self):
		return dict([(int(values[0]), values[1]) for values in self._states.value])

	@states.setter
	def states(self, value):
		self._states.value = value.items()
		if value and len(value) > 0:
			self.highest_state_id = sorted( map(int, value.keys()) )[-1]

	@property
	def events(self):
		return dict([(int(values[0]), values[1]) for values in self._events.value])

	@events.setter
	def events(self, value):
		self._events.value = value.items()
		

	@property
	def variables(self):
		logger.debug(self._vars.value)
		values = []
		for var in self._vars.value:
			var_name 		= str(var[0])
			var_persistent 	= var[2].isChecked()
			var_value 		= str(var[1]) if (str(var[1])!='None' and len(str(var[1]))>0) else None
			values.append( self.create_variable(var_name, var_value, var_persistent) )

		return values
		#return [self.create_variable(str(var[0]), None if (var[1] == 'None' or var[1] == '') else eval(str(var[1])),
		#                     var[2].isChecked()) for var in self._vars.value]

	@variables.setter
	def variables(self, value):
		rows = []

		for var in value:
			checkbox = QtGui.QCheckBox(self)
			checkbox.setChecked(var.persistent)
			#value = "'{0}'".format(var.value) if isinstance(var.value, str) else var.value
			#if value == None: value = ''
			row = [var.name, var.value, checkbox]
			rows.append(row)

		self._vars.value = rows

	def beforeClose(self):
		"""
		Define behavior before window is closed.
		"""
		return False

	def sync_variables(self):
		"""
		Defines behavior of the button :attr:`BoardTaskWindow._sync_btn`.
		This methods is called every time the user presses the button.

		.. seealso ::
			This method invokes a board operation:

			:py:meth:`pycontrolgui.models.board.board_com.ComBoard.sync_variables`
		"""
		if self.board and self.task:
			self.board.sync_variables(self)

	def __load_task_details(self):
		"""
		Defines behavior of the button :attr:`BoardTaskWindow._load_btn`.
		This methods is called every time the user presses the button.

		.. seealso ::
			This method invokes API:

			:py:meth:`pycontrolapi.models.setup.board_task.BoardTask.load_task_details`
		"""
		reply = QtGui.QMessageBox.question(self, 'Attention',
		                                   'All the configured values will be deleted. Are sure you want to procede?',
		                                   QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
		if reply == QtGui.QMessageBox.Yes:
			self.load_task_details()


# Execute the application
if __name__ == "__main__":
	app.start_app(BoardTaskWindow)
