#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pyforms import conf

from AnyQt.QtCore import QTimer

from pyforms import BaseWidget
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlCheckBox
from pyforms.controls import ControlButton

from pybranch.com.messaging.debug import DebugMessage
from pybpodgui_api.exceptions.run_setup import RunSetupError

from AnyQt.QtWidgets import QApplication

logger = logging.getLogger(__name__)


class LogWindow(BaseWidget):
    def __init__(self, board):
        BaseWidget.__init__(self, board.name)
        self.board = board
        self.layout().setContentsMargins(5, 5, 5, 5)

        self._autoscroll_checkbox = ControlCheckBox('Auto-scroll', default=True, changed_event=self.__auto_scroll_evt)
        self._log  = ControlTextArea(readonly=True, autoscroll=False)
        self._clearbtn = ControlButton('Clear', default=self.__clear_log_evt)

        self.formset = [(' ', '_autoscroll_checkbox','_clearbtn'), '_log']

    def __auto_scroll_evt(self):
        self._log.autoscroll = self._autoscroll_checkbox.value

    def __clear_log_evt(self):
        self._log.value = ''

    def __add__(self, value):
        if self.visible: 
            self._log += value
        return self

    def show(self):
        self.__clear_log_evt()
        super(LogWindow,self).show()
    

    @property
    def title(self):
        return BaseWidget.title.fget(self)

    @title.setter
    def title(self, value):
        BaseWidget.title.fset(self, "{0} log".format(value))

    @property
    def mainwindow(self):
        return self.board.mainwindow
