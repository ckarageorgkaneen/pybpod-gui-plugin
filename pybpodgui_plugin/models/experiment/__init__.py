# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pysettings import conf
from pybpodgui_plugin.models.experiment.experiment_uibusy import ExperimentUIBusy

Experiment = type(
	'Experiment',
	tuple(conf.GENERIC_EDITOR_PACKAGES_FINDER.find_class('models.experiment.Experiment') + [ExperimentUIBusy]),
	{}
)

