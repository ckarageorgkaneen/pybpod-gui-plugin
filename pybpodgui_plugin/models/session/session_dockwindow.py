# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pybpodgui_plugin.models.session.session_treenode import SessionTreeNode

logger = logging.getLogger(__name__)


class SessionDockWindow(SessionTreeNode):
	def show(self):
		try:
			if len(self.messages_history) == 0:
				self.load_contents(self.filepath)
		except FileNotFoundError as err:
			logger.warning("Trying to load contents from session without file.")

		self.mainwindow.details.value = self

	@property
	def mainwindow(self):
		return self.setup.mainwindow

	def beforeClose(self):
		return False
