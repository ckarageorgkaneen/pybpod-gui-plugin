# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pysettings import conf

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtWidgets import QFileDialog
	from PyQt5.QtCore import pyqtSignal
else:
	from PyQt4.QtGui import QFileDialog
	from PyQt4.QtCore import pyqtSignal

import pyforms

from pybpodgui_plugin.models.project import Project
from pybpodgui_plugin.models.session import Session

logger = logging.getLogger(__name__)


class ProjectsWindow(object):
	"""
	See:
	 - pyforms_generic_editor.models.projects.__init__.py
	 - pyforms_generic_editor.models.projects.projects_window.py
	"""

	signal_session_create_treenode = pyqtSignal(Session)

	def __init__(self, mainwindow=None):
		super(ProjectsWindow, self).__init__(mainwindow)

	def create_project(self):
		"""
		Invoke project creation

		.. seealso::
			* Create project treenode: :class:`pybpodgui_plugin.models.projects.projects_treenode.ProjectsTreeNode.create_project`.

		:rtype: Project
		"""
		project = Project(self)

		return project

	def open_project(self, project_path=None):
		"""
		Open project

		.. seealso::
			* Open project treenode: :class:`pybpodgui_plugin.models.projects.projects_treenode.ProjectsTreeNode.open_project`.

		:param str project_path:
		"""
		project = None
		if not project_path:
			project_path = QFileDialog.getExistingDirectory(self, "Select the project directory")
		if project_path:
			project = self.create_project()
			project.load(str(project_path))

		return project


if __name__ == "__main__": pyforms.start_app(ProjectsWindow)
