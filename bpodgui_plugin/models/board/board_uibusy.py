# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from pysettings import conf

from PyQt4 import QtGui

from bpodgui_plugin.models.board.board_dockwindow import BoardDockWindow

logger = logging.getLogger(__name__)


class BoardUIBusy(BoardDockWindow):
	"""
	Perform operations related with UI reloading
	"""

	def __init__(self, project):
		super(BoardUIBusy, self).__init__(project)

	def update_ui(self):
		"""
		update ui now
		"""
		if not hasattr(self, 'node'): return

		logger.debug('Board [{0}] status: {1}'.format(self.name, self.status))

		if self.status > BoardUIBusy.STATUS_READY:
			self._edit_framework_btn.enabled = False
			self._install_framework_btn.enabled = False
			self.node.setIcon(0, QtGui.QIcon(conf.PLAY_SMALL_ICON))
		else:
			self._edit_framework_btn.enabled = True
			self._install_framework_btn.enabled = True
			self.node.setIcon(0, QtGui.QIcon(conf.BOX_SMALL_ICON))

	##########################################################################
	####### PROPERTIES #######################################################
	##########################################################################

	@property
	def status(self):
		return BoardDockWindow.status.fget(self)

	@status.setter
	def status(self, value):
		BoardDockWindow.status.fset(self, value)
		self.project.update_ui()

	##########################################################################
	####### FUNCTIONS ########################################################
	##########################################################################
