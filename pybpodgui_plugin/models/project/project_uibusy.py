# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtGui import QIcon
else:
	from PyQt4.QtGui import QIcon

from pybpodgui_plugin.models.board import Board
from pybpodgui_plugin.models.project.project_dockwindow import ProjectDockWindow


class ProjectUIBusy(ProjectDockWindow):
	"""
	
	"""

	def update_ui(self):
		"""
		Update user interface
		"""

		busy_status = Board.STATUS_READY
		for board in self.boards:
			if board.status > Board.STATUS_READY:
				busy_status = board.status
				break

		if busy_status == Board.STATUS_READY:

			self.node.setIcon(0, QIcon(conf.PROJECT_SMALL_ICON))
			self.experiments_node.setIcon(0, QIcon(conf.EXPERIMENTS_SMALL_ICON))
			self.boards_node.setIcon(0, QIcon(conf.BOARDS_SMALL_ICON))

		elif busy_status in [Board.STATUS_RUNNING_TASK]:

			self.node.setIcon(0, QIcon(conf.PLAY_SMALL_ICON))
			self.experiments_node.setIcon(0, QIcon(conf.PLAY_SMALL_ICON))
			self.boards_node.setIcon(0, QIcon(conf.PLAY_SMALL_ICON))

		for exp in self.experiments:
			exp.update_ui()

		for board in self.boards:
			board.update_ui()
