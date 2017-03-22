# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

from bpodgui_plugin.models.project.project_treenode import ProjectTreeNode


class ProjectDockWindow(ProjectTreeNode):
	def show(self):
		self.mainwindow.details.value = self

	def focus_name(self):
		"""
		Sets interface focus on the board name text field
		"""
		self._name.form.lineEdit.setFocus()

	def close(self):
		self.mainwindow.details.value = None
		super(ProjectDockWindow, self).close()

	@property
	def mainwindow(self):
		return self.projects.mainwindow
