# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from PyQt4 import QtGui

import pyforms as app
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
from pyforms.Controls import ControlCombo

from bpodgui_plugin.api.models.task import Task
from bpodgui_plugin.api.models.experiment import Experiment
from bpodgui_plugin.api.models.project import Project
from bpodgui_plugin.api.exceptions.run_setup import RunSetupError

logger = logging.getLogger(__name__)


class ExperimentWindow(Experiment, BaseWidget):
	"""
	Define here which fields from the board model should appear on the details section.

	The model fields shall be defined as UI components like text fields, buttons, combo boxes, etc.

	You may also assign actions to these components.

	**Private attributes**

	_name
		Field to edit experiment name

		:type: :class:`pyforms.Controls.ControlText`

	_button_run_all
		Button to run task for all subjects. Pressing the button fires the event :class:`ExperimentWindow._ExperimentWindow__button_run_all_evt`.

		:type: :class:`pyforms.Controls.ControlButton`

	_button_upload_all
		Button to upload task for all subjects. Pressing the button fires the event :class:`ExperimentWindow._ExperimentWindow__button_upload_all_evt`.

		:type: :class:`pyforms.Controls.ControlButton`

	_button_restore
		Button to restore task variables. Pressing the button fires the event :class:`ExperimentWindow._ExperimentWindow__button_restore_evt`.

		:type: :class:`pyforms.Controls.ControlButton`

	_task
		Combo box of available tasks. Current selected task is the task associated for this experiment
		and all its subjects. Selecting a different task fires the event :class:`ExperimentWindow._ExperimentWindow__task_changed_evt`.

		:type: :class:`pyforms.Controls.ControlCombo`

	**Methods**

	"""

	def __init__(self, project):
		# type: (Project) -> None
		"""

		:param project: project where this experiment belongs
		:type project: pycontrolgui.models.project.Project
		"""
		BaseWidget.__init__(self, 'Experiment')
		self.layout().setContentsMargins(5, 10, 5, 5)

		self._name = ControlText('Exp. name')
		self._task = ControlCombo('Task')

		self._formset = [
			'_name',
			'_task',
		]

		Experiment.__init__(self, project)

		self._name.changed_event = self.__name_changed_evt
		self._task.changed_event = self.__task_changed_evt


	def __task_changed_evt(self):
		"""

		This methods is called every time the user presses the button.
		"""
		self.task = self._task.value
		self.update_ui()

	def __name_changed_evt(self):
		if not hasattr(self, '_update_name') or not self._update_name:
			self.name = self._name.value

	@property
	def name(self):
		return self._name.value

	@name.setter
	def name(self, value):
		self._update_name = True  # Flag to avoid recurse calls when editing the name text field
		self._name.value = value
		self._update_name = False

	@property
	def task(self):
		"""
		Property that holds the task currently associated with this experiment.

		This property returns the current value stored in the combo box of tasks (which should be a task)

		:type task: Task
		"""
		if isinstance(self._task.value, str): return None
		return self._task.value

	@task.setter
	def task(self, value):
		last_task = self._task.value
		if isinstance(value, str): value = self.project.find_task(value)
		self._update_name = True  # Flag to avoid recurse calls when editing the name text field
		self._task.value = value

		try:
			for setup in self.setups:
				setup.task = value
				setup.board_task.load_task_details()
		except FileNotFoundError as err:
			logger.warning(str(err))

			QtGui.QMessageBox.about(self,
			                        "Task file does not exists yet.",
			                        "The task file does not exists yet.\nPlease save the project to create the task file.")

			self._task.value = last_task

		self._update_name = False


if __name__ == "__main__":
	# Execute the application
	app.start_app(ExperimentWindow)
