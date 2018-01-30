# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

from pybpodgui_plugin.models.subject.subject_treenode import SubjectTreeNode
from AnyQt.QtWidgets import QApplication

class SubjectDockWindow(SubjectTreeNode):
	def show(self):
		self.mainwindow.details.value = self
		QApplication.processEvents()

	def focus_name(self):
		"""
		Sets interface focus on the board name text field
		"""
		self._name.form.lineEdit.setFocus()

	def close(self, silent=False):
		self.mainwindow.details.value = None
		super(SubjectDockWindow, self).close(silent)

	@property
	def mainwindow(self):
		return self.project.mainwindow
