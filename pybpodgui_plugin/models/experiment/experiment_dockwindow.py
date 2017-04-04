# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pysettings import conf

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtWidgets import QMessageBox
else:
	from PyQt4.QtGui import QMessageBox

from pybpodgui_plugin.models.experiment.experiment_treenode import ExperimentTreeNode

logger = logging.getLogger(__name__)


class ExperimentDockWindow(ExperimentTreeNode):
	"""
	Dock window settings.
	Define here behaviors associated with experiment details section.

	**Properties**

		mainwindow
			Returns project main window.

	**Methods**

	"""

	MARKED_FOR_REMOVAL = False  # This flag will be activated while removing experiment and its setups

	def show(self):
		"""
		Select this window as the main window on the details section.
		Also reload tasks list on combo box.
		"""
		self.mainwindow.details.value = self
		self.reload_tasks(current_selected_task=self.task)

	def focus_name(self):
		"""
		Sets interface focus on the board name text field
		"""
		self._name.form.lineEdit.setFocus()

	def remove(self):
		"""
		Prompts user to confirm experiment removal.

		.. seealso::
			This method extends experiment tree node :py:meth:`pybpodgui_plugin.models.experiment.experiment_treenode.ExperimentTreeNode.remove`.

		"""
		reply = QMessageBox.question(self, 'Warning',
		                             'Experiment {0} and all subjects will be deleted. Are you sure?'.format(
			                             self.name),
		                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			self.MARKED_FOR_REMOVAL = True
			self.mainwindow.details.value = None
			super(ExperimentDockWindow, self).remove()

	@property
	def mainwindow(self):
		return self.project.mainwindow
