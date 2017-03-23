# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pybpodgui_plugin.models.session.session_treenode import SessionTreeNode

logger = logging.getLogger(__name__)


class SessionDockWindow(SessionTreeNode):
	def show(self):
		if len(self.messages_history) == 0: self.load_contents(self.path)

		self.mainwindow.details.value = self

	@property
	def mainwindow(self):
		return self.setup.mainwindow

	def beforeClose(self):
		return False
