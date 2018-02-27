# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pybpodgui_plugin.models.session.session_treenode import SessionTreeNode

logger = logging.getLogger(__name__)


class SessionDockWindow(SessionTreeNode):

    def show(self):
        
        try:
            if len(self.messages_history) == 0 and not self.is_running:
                self.load_info()
        except FileNotFoundError as err:
            logger.warning("Error when trying to load the session info.")
            self.error("Error when trying to load the session info.")

        self.mainwindow.details.value = self
        
    @property
    def mainwindow(self):
        return self.setup.mainwindow

    def beforeClose(self):
        return False
