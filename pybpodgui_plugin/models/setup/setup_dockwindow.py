# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pysettings import conf

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtWidgets import QMessageBox
else:
	from PyQt4.QtGui import QMessageBox

from pybpodgui_plugin.models.setup.setup_treenode import SetupTreeNode
from AnyQt.QtWidgets import QApplication

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

	def show(self):
		"""
		Select this window as the main window on the details section.
		Also reload boards list on combo box.
		"""
		self.mainwindow.details.value = self
		self._experiment_name.value = self.experiment.name
		self._protocol_name.value = self.experiment._task.text
		self.reload_boards(current_selected_board=self.board)
		QApplication.processEvents()

	def focus_name(self):
		"""
		Sets interface focus on the board name text field
		"""
		self._name.form.lineEdit.setFocus()

	def remove(self):
		"""

		Prompts user to confirm setup removal.

		.. seealso::
			This method extends setup tree node :py:meth:`pybpodgui_plugin.models.setup.setup_treenode.SetupTreeNode.remove`.

		"""
		if not self.experiment.MARKED_FOR_REMOVAL:
			reply = QMessageBox.question(self, 'Warning',
			                             'The setup {0} will be deleted. Are you sure?'.format(self.name),
			                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		else:
			reply = True

		if reply == QMessageBox.Yes:
			self.mainwindow.details.value = None
			super(SetupDockWindow, self).remove()

	@property
	def mainwindow(self):
		return self.experiment.mainwindow
