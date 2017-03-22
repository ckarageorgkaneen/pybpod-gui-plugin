# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignal

import pyforms

from pyforms_generic_editor.models.projects import GenericProjects

from bpodgui_plugin.models.project import Project
from bpodgui_plugin.models.session import Session

logger = logging.getLogger(__name__)


class ProjectsWindow(GenericProjects):
	"""

	"""

	signal_session_create_treenode = pyqtSignal(Session)

	def __init__(self, mainwindow=None):
		GenericProjects.__init__(self, mainwindow)

	def create_project(self):
		"""
		Invoke project creation

		.. seealso::
			* Create project treenode: :class:`pybehavior.models.projects.projects_treenode.ProjectsTreeNode.create_project`.

		:rtype: Project
		"""
		project = Project(self)

		return project

	def open_project(self, project_path=None):
		"""
		Open project

		.. seealso::
			* Open project treenode: :class:`pybehavior.models.projects.projects_treenode.ProjectsTreeNode.open_project`.

		:param str project_path:
		"""
		project = None
		if not project_path:
			project_path = QtGui.QFileDialog.getExistingDirectory(self, "Select the project directory")
		if project_path:
			project = self.create_project()
			project.load(str(project_path))

		return project


if __name__ == "__main__": pyforms.start_app(ProjectsWindow)
