# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf

from PyQt4 import QtGui

from bpodgui_plugin.models.board import Board
from bpodgui_plugin.models.project.project_dockwindow import ProjectDockWindow


class ProjectUIBusy(ProjectDockWindow):
	def update_ui(self):

		busy_status = Board.STATUS_READY
		for board in self.boards:
			if board.status > Board.STATUS_READY:
				busy_status = board.status
				break

		if busy_status == Board.STATUS_READY:

			self.node.setIcon(0, QtGui.QIcon(conf.PROJECT_SMALL_ICON))
			self.experiments_node.setIcon(0, QtGui.QIcon(conf.EXPERIMENTS_SMALL_ICON))
			self.boards_node.setIcon(0, QtGui.QIcon(conf.BOARDS_SMALL_ICON))
			self._install_framework_btn.enabled = True

		elif busy_status in [
			Board.STATUS_INSTALLING_FRAMEWORK,
			Board.STATUS_INSTALLING_TASK,
			Board.STATUS_SYNCING_VARS,
			Board.STATUS_RUNNING_TASK]:

			self.node.setIcon(0, QtGui.QIcon(conf.PLAY_SMALL_ICON))
			self.experiments_node.setIcon(0, QtGui.QIcon(conf.PLAY_SMALL_ICON))
			self.boards_node.setIcon(0, QtGui.QIcon(conf.PLAY_SMALL_ICON))
			self._install_framework_btn.enabled = False

		for exp in self.experiments:    exp.update_ui()
		for board in self.boards:        board.update_ui()
