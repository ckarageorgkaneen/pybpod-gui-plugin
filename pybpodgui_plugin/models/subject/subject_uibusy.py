# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pyforms import conf

from AnyQt.QtGui import QIcon

from pybpodgui_api.models.setup import Setup
from pybpodgui_api.models.subject import Subject
from pybpodgui_api.models.project import Project
from pybpodgui_plugin.models.subject.subject_dockwindow import SubjectDockWindow

logger = logging.getLogger(__name__)

class SubjectUIBusy(SubjectDockWindow):
    """
	Extends subject with UI refreshment logic.

	"""

    def __init__(self, project):
        super(SubjectUIBusy, self).__init__(project)
        self.__running_icon = QIcon(conf.PLAY_SMALL_ICON)
        print('SUBJECT UI BUSY INIT')

    def update_ui(self):
        print('SUBJECT UI BUSY UPDATE UI')