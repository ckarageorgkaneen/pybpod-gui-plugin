# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

from pybpodgui_plugin.models.subject.subject_treenode import SubjectTreeNode


class SubjectDockWindow(SubjectTreeNode):
	
	def show(self):
		self.mainwindow.details.value = self
		super(SubjectDockWindow, self).show()
		self.reload_setups()

	def focus_name(self):
		"""
		Sets interface focus on the board name text field
		"""
		self._name.form.lineEdit.setFocus()

	def remove(self):
		"""

        Prompts user to confirm subject removal and closes mdi windows associated with this subject.

        .. seealso::
            This method extends subject tree node :py:meth:`pybpodgui_plugin.models.subject.subject_treenode.SubjectTreeNode.remove`.

        """
		reply = self.question('Subject {0} will be deleted. Are you sure?'.format(self.name), 'Warning')
		if reply == 'yes':
			if hasattr(self, '_code_editor'):
				self.mainwindow.mdi_area -= self._code_editor
			super(SubjectDockWindow, self).remove()


	def close(self, silent=False):
		self.mainwindow.details.value = None
		super(SubjectDockWindow, self).close(silent)

	@property
	def mainwindow(self):
		return self.project.mainwindow
