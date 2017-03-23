# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from PyQt4 import QtGui

import pyforms as app
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCombo

from bpodgui_plugin.api.models.setup import Setup
from bpodgui_plugin.api.exceptions.run_setup import RunSetupError

from bpodgui_plugin.models.setup.board_task import BoardTask
from bpodgui_plugin.models.session import Session

logger = logging.getLogger(__name__)


class SetupWindow(Setup, BaseWidget):
	"""
	Define here which fields from the setup model should appear on the details section.

	The model fields shall be defined as UI components like text fields, buttons, combo boxes, etc.

	You may also assign actions to these components.

	**Properties**

		name
			:class:`string`

			Name associated with this setup. Returns the current value stored in the :py:attr:`_name` text field.

		board
			:class:`pycontrolgui.models.board.board_dockwindow.BoardDockWindow`

			Board associated with this setup. Returns the current value stored in the :py:attr:`_board` combo box.

	**Private attributes**

		_name
			:class:`pyforms.Controls.ControlText`

			Text field to edit board name. Editing this field fires the event :meth:`SetupWindow._SetupWindow__name_changed_evt`.

		_board
			:class:`pyforms.Controls.ControlCombo`

			Combo box to select board associated with this setup. Editing this field fires the event :meth:`SetupWindow._SetupWindow__board_changed_evt`.

		_run_task_btn
			:class:`pyforms.Controls.ControlButton`

			Button to run task on board. Pressing the button fires the event :meth:`SetupWindow._SetupWindow__run_task`.

		_formset
			Describe window fields organization to PyForms.

	**Methods**

	"""

	def __init__(self, experiment=None):
		"""

		:param experiment: Experiment this setup belongs to.
		"""
		BaseWidget.__init__(self, 'Experiment')
		self.layout().setContentsMargins(5, 10, 5, 5)

		self._name = ControlText('Subject name')
		self._board = ControlCombo('Box')
		self._run_task_btn = ControlButton('Run')

		Setup.__init__(self, experiment)

		self.reload_boards()

		self._formset = [
			'_name',
			'_board',
			(' ', ' ', '_run_task_btn'),
			' '
		]

		self._name.changed_event = self.__name_changed_evt
		self._board.changed_event = self.__board_changed_evt

		self._run_task_btn.value = self._run_task

	def _run_task(self):
		"""
		Defines behavior of the button :attr:`SetupWindow._run_task_btn`.

		This methods is called every time the user presses the button.
		"""
		try:
			if self.status == SetupWindow.STATUS_RUNNING_TASK_HANDLER:
				self.stop_task()
			elif self.status == SetupWindow.STATUS_READY:
				self.run_task()
		except RunSetupError as err:
			QtGui.QMessageBox.warning(self, "Warning", str(err))
		except Exception as err:
			QtGui.QMessageBox.critical(self, "Unexpected Error", str(err))

	def __board_changed_evt(self):
		"""
		React to changes on text field :py:attr:`_board`.

		This method is called every time the user changes the field and forces a UI refresh.
		"""
		self.board = self._board.value
		self.update_ui()

	def __name_changed_evt(self):
		"""
		React to changes on text field :py:attr:`_name`.

		This methods is called every time the user changes the field.
		"""
		if not hasattr(self, '_update_name') or not self._update_name:
			self.name = self._name.value

	def reload_boards(self, current_selected_board=None):
		"""
		Reload boards list on combo box

		This method is fired by:
			* setup creation: :py:meth:`pycontrolgui.models.setup.setup_window.SetupWindow._SetupWindow__init__`.
			* setup details section focus (dockwindow): :py:meth:`pycontrolgui.models.setup.setup_dockwindow.SetupDockWindow.show`.

		:param current_selected_board: optional specify current selected board to restore after list update
		"""
		self._board.clear()
		self._board.add_item('', 0)
		for board in self.project.boards: self._board.add_item(board.name, board)
		self._board.current_index = 0

		if current_selected_board:
			self.board = current_selected_board

	def create_board_task(self):
		"""
		Creates a new board task by calling the API.

		.. seealso::
			:py:class:`pycontrolapi.models.setup.board_task.BoardTask`.
		"""
		return BoardTask(self)

	def create_session(self):
		"""
		Creates a new session by calling the API.

		.. seealso::
			:py:class:`pycontrolapi.models.session.session_base.SessionBase`.
		"""
		return Session(self)

	@property
	def name(self):
		return self._name.value

	@name.setter
	def name(self, value):
		self._update_name = True  # Flag to avoid recurse calls when editing the name text field
		self._name.value = value
		self._update_name = False
		# Update the session windows names
		if hasattr(self, 'sessions'):
			for session in self.sessions:
				session.name = session.name

	@property
	def board(self):
		if isinstance(self._board.value, str) or isinstance(self._board.value, int): return None
		return self._board.value

	@board.setter
	def board(self, value):
		if isinstance(value, str): value = self.project.find_board(value)
		self._update_name = True  # Flag to avoid recurse calls when editing the name text field
		self._board.value = value
		self._update_name = False
		Setup.board.fset(self, value)


# Execute the application
if __name__ == "__main__":
	app.start_app(SetupWindow)
