# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from PyQt4 import QtGui

from bpodgui_plugin.models.setup.setup_treenode import SetupTreeNode

logger = logging.getLogger(__name__)


class SetupDockWindow(SetupTreeNode):
	"""
	Dock window settings.
	Define here behaviors associated with board dock window.

	**Properties**

		mainwindow
			Returns project main window.

	**Methods**

	"""
	def __init__(self, experiment):
		super(SetupDockWindow, self).__init__(experiment)

		self._configure_task_btn.value = self.__configure_task_btn_evt

	def show(self):
		"""
		Select this window as the main window on the details section.
		Also reload boards list on combo box.
		"""
		self.mainwindow.details.value = self
		self.reload_boards(current_selected_board=self.board)

	def focus_name(self):
		"""
		Sets interface focus on the board name text field
		"""
		self._name.form.lineEdit.setFocus()

	def remove(self):
		"""

		Prompts user to confirm setup removal.

		.. seealso::
			This method extends setup tree node :py:meth:`pycontrolgui.models.setup.setup_treenode.SetupTreeNode.remove`.

		"""
		if not self.experiment.MARKED_FOR_REMOVAL:
			reply = QtGui.QMessageBox.question(self, 'Warning',
			                                   'Subject {0} will be deleted. Are you sure?'.format(self.name),
			                                   QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		else:
			reply = True

		if reply == QtGui.QMessageBox.Yes:
			self.mainwindow.details.value = None
			super(SetupDockWindow, self).remove()

	def __configure_task_btn_evt(self):
		self.mainwindow.mdi_area += self.board_task

	@property
	def mainwindow(self):
		return self.experiment.mainwindow