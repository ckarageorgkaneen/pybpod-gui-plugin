# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from pysettings import conf

from bpodgui_plugin.api.models.setup import Setup
from bpodgui_plugin.models.session.session_signals import SessionSignals


class SessionUIBusy(SessionSignals):

	def update_ui(self):
		if not hasattr(self,'node'): return

		if self.setup.status in [
			Setup.STATUS_RUNNING_TASK, 
			Setup.STATUS_RUNNING_TASK_HANDLER,
			Setup.STATUS_RUNNING_TASK_ABOUT_2_STOP
		]:
			self.node.setIcon(0, QtGui.QIcon(conf.PLAY_SMALL_ICON))
		else:
			self.node.setIcon(0, QtGui.QIcon())