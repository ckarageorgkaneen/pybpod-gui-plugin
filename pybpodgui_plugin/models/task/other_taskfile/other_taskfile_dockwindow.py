# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pyforms import conf

from pybpodgui_plugin.models.task.windows.code_editor import CodeEditor
from pybpodgui_plugin.models.task.other_taskfile.other_taskfile_treenode import OtherTaskFileTreeNode

logger = logging.getLogger(__name__)


class OtherTaskTaskDockWindow(OtherTaskFileTreeNode):
	"""
	Dock window settings.
	Define here behaviors associated with board dock window.

	**Properties**

		mainwindow
			Returns project main window.

	**Methods**

	"""

	def __init__(self, task):
		super(OtherTaskTaskDockWindow, self).__init__(task)
		#self._edit_btn.value = self.edit_btn_evt

	def show(self):
		"""
		Select this window as the main window on the details section.
		"""
		self.mainwindow.details.value = self

	def focus_name(self):
		"""
		Sets interface focus on the task name text field
		"""
		#self._name.form.lineEdit.setFocus()
		pass

	def remove(self):
		"""

		Prompts user to confirm task removal and closes mdi windows associated with this task.

		.. seealso::
			This method extends task tree node :py:meth:`pybpodgui_plugin.models.task.task_treenode.TaskTreeNode.remove`.

		"""
		reply = self.question('Task {0} will be deleted. Are you sure?'.format(self.name), 'Warning')
		if reply:
			if hasattr(self, '_code_editor'):
				self.mainwindow.mdi_area -= self._code_editor
			super(TaskDockWindow, self).remove()

	def edit_btn_evt(self):
		"""
		Open code editor window on the mdi section for the task source code.

		.. seealso::
			This event may be fired on:
				* Double click event (tree node): :py:meth:`pybpodgui_plugin.models.task.task_treenode.TaskTreeNode.node_double_clicked_event`.
				* Key press event (tree node): :py:meth:`pybpodgui_plugin.models.task.task_treenode.TaskTreeNode.node_key_pressed_event`.
		"""
		if self.project.path is None:
			self.warning("The project was not saved yet.\nPlease save it first.", "Cannot edit the file yet.")
		else:
			try:
				if not hasattr(self, '_code_editor'):
					self._code_editor = CodeEditor(self)
				self.mainwindow.mdi_area += self._code_editor
			except FileNotFoundError as err:
				logger.warning(str(err))
				self.warning(
					"Task file does not exist yet.\nPlease save the project to create the task file.",
					"Cannot edit the file yet.")

	@property
	def mainwindow(self):
		return self.task.mainwindow
