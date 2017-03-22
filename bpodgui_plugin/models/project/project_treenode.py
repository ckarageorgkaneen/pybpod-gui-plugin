# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import logging

from PyQt4 import QtGui

from pysettings import conf

from bpodgui_plugin.models.project.project_window import ProjectWindow
from bpodgui_plugin.models.experiment import Experiment
from bpodgui_plugin.models.board import Board
from bpodgui_plugin.models.task import Task

logger = logging.getLogger(__name__)


class ProjectTreeNode(ProjectWindow):
	def __init__(self, projects):
		ProjectWindow.__init__(self)

		self.projects = projects
		self.projects += self

		self.create_treenode(self.tree)

	def create_treenode(self, tree):
		self.node = tree.create_child(self.name, icon=QtGui.QIcon(conf.PROJECT_SMALL_ICON))
		self.node.window = self
		self.node.setExpanded(True)

		tree.add_popup_menu_option('Save', self.save, item=self.node, icon=QtGui.QIcon(conf.SAVE_SMALL_ICON))
		tree.add_popup_menu_option('Save as', self.save_as, item=self.node, icon=QtGui.QIcon(conf.SAVE_SMALL_ICON))
		tree.add_popup_menu_option('Close', self.close, item=self.node, icon=QtGui.QIcon(conf.CLOSE_SMALL_ICON))

		self.experiments_node = tree.create_child('Experiments', parent=self.node,
		                                          icon=QtGui.QIcon(conf.EXPERIMENTS_SMALL_ICON))
		self.experiments_node.window = self
		self.experiments_node.setExpanded(True)

		tree.add_popup_menu_option('Add experiment', self._add_experiment, item=self.experiments_node,
		                           icon=QtGui.QIcon(conf.ADD_SMALL_ICON))

		self.boards_node = tree.create_child('Bpod Boxes', parent=self.node, icon=QtGui.QIcon(conf.BOARDS_SMALL_ICON))
		self.boards_node.window = self
		self.boards_node.setExpanded(True)

		tree.add_popup_menu_option('Add Bpod box', self._add_board, item=self.boards_node,
		                           icon=QtGui.QIcon(conf.ADD_SMALL_ICON))

		self.tasks_node = tree.create_child('Protocols', parent=self.node, icon=QtGui.QIcon(conf.TASKS_SMALL_ICON))
		tree.add_popup_menu_option('Add protocol', self._add_task, item=self.tasks_node,
		                           icon=QtGui.QIcon(conf.ADD_SMALL_ICON))
		self.tasks_node.window = self
		self.tasks_node.setExpanded(True)

		tree.add_popup_menu_option('Import protocol', self.import_task, item=self.tasks_node,
		                           icon=QtGui.QIcon(conf.OPEN_SMALL_ICON))

		return self.node

	def _add_experiment(self):
		entity = self.create_experiment()
		entity.focus_name()

	def _add_board(self):
		entity = self.create_board()
		entity.focus_name()

	def _add_task(self):
		if self.path is None or len(self.path) == 0:
			reply = QtGui.QMessageBox.warning(self, 'Project not saved yet',
			                                  'To create a new protocol you need to save the project first.')
		else:
			entity = self.create_task()
			entity.focus_name()

	def create_experiment(self):
		experiment = Experiment(self)
		self.tree.setCurrentItem(experiment.node)
		return experiment

	def create_board(self):
		board = Board(self)
		self.tree.setCurrentItem(board.node)
		return board

	def create_task(self):
		task = Task(self)
		self.tree.setCurrentItem(task.node)
		return task

	def close(self):
		reply = QtGui.QMessageBox.question(self, 'Close project', 'Are sure you want to close the project?',
		                                   QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)

		if reply == QtGui.QMessageBox.Yes:
			super(ProjectTreeNode, self).close()

			# for index in range(len(self.experiments) - 1, -1, -1):   self.experiments[index].remove()
			# for index in range(len(self.tasks) - 1, -1, -1):         self.tasks[index].remove()
			# for index in range(len(self.boards) - 1, -1, -1):        self.boards[index].remove()

			tree = self.tree
			tree -= self.node

	def save_as(self):
		folder = QtGui.QFileDialog.getExistingDirectory(self,
		                                                "Select a directory to save the project: {0}".format(self.name))
		if folder:
			folder = os.path.join(folder, self.name)
			self.save(str(folder))

	def load(self, project_path):
		ProjectWindow.load(self, project_path)

		self.tree.setCurrentItem(self.node)

	def import_task(self, filepath=None):
		if not filepath:
			filepath = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
		if filepath:
			task = self.create_task()
			task.load(str(filepath), {})
			task.name = task.name

	@property
	def name(self):
		if hasattr(self, 'node'):
			return str(self.node.text(0))
		else:
			name = ProjectWindow.name.fget(self)
			if len(name) == 0:
				name = "Untitled project {0}".format(len(self.projects.projects))
				ProjectWindow.name.fset(self, name)
				return name
			else:
				return ProjectWindow.name.fget(self)

	@name.setter
	def name(self, value):
		ProjectWindow.name.fset(self, value)
		if hasattr(self, 'node'): self.node.setText(0, value)

	@property
	def tree(self):
		return self.projects.tree
