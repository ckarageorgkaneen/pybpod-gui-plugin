# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import os

from PyQt4 import QtGui

import pyforms as app
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton

from pyforms_generic_editor.models.project import GenericProject

from pybpodgui_plugin.api.models.board import Board
from pybpodgui_plugin.api.models.project import Project

logger = logging.getLogger(__name__)

class ProjectWindow(Project, GenericProject):
	""" ProjectWindow represents the project entity as a GUI window"""

	def __init__(self):
		"""

		"""

		GenericProject.__init__(self)

		self._name = ControlText('Project name')
		self._path = ControlText('Project path')

		self.formset = ['_name', '_path', ' ']

		self._name.changed = self.__name_edited_evt
		self._path.value = self.path
		self._path.enabled = False

		Project.__init__(self)

	def __name_edited_evt(self):
		if not hasattr(self, '_update_name') or not self._update_name:
			self.name = self._name.value

	@property
	def path(self):
		return self._path.value

	@path.setter
	def path(self, value):
		self._path.value = value

	@property
	def name(self):
		return self._name.value

	@name.setter
	def name(self, value):
		self._update_name = True  # Flag to avoid recurse calls when editing the name text field
		self._name.value = value
		self._update_name = False

	def save(self, project_path=None):
		if project_path:
			Project.save(self, project_path)
		elif self.path:
			Project.save(self, self.path)
		else:
			folder = QtGui.QFileDialog.getExistingDirectory(self, "Select a directory to save the project: {0}".format(
				self.name))
			if folder:
				folder = os.path.join(folder, self.name)
				try:
					Project.save(self, str(folder))
				except FileExistsError as err:
					logger.warning(str(err))
					QtGui.QMessageBox.warning(self, 'Project exists',
											  'Project with same name already exists. Please select another path.')

	def close(self):
		self.projects -= self
		super(ProjectWindow, self).close()


# Execute the application
if __name__ == "__main__":
	app.startApp(ProjectWindow)