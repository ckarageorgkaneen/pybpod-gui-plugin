# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf

from pybpodgui_plugin.models.session.session_uibusy import SessionUIBusy

Session = type(
	'Session',
	tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.session.Session') + [SessionUIBusy]),
	{}
)