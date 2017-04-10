# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf

from pybpodgui_plugin.models.setup.setup_uibusy import SetupUIBusy

Setup = type(
	'Setup',
	tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.setup.Setup', silent=conf.DEV_MODE) + [SetupUIBusy]),
	{}
)