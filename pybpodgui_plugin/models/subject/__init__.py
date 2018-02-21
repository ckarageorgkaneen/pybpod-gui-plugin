# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pyforms import conf

from pybpodgui_plugin.models.subject.subject_dockwindow import SubjectDockWindow

Subject = type(
    'Subject',
    tuple(conf.GENERIC_EDITOR_PLUGINS_FINDER.find_class('models.subject.Subject') + [SubjectDockWindow]),
    {}
)
