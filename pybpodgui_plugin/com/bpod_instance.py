# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from copy import deepcopy
from pybpodapi.model.bpod import Bpod

logger = logging.getLogger(__name__)


class BpodInstance(Bpod):
	def __init__(self, gui_logger_fn):
		"""

		:param gui_logger_fn:
		"""
		self.gui_logger_fn = gui_logger_fn

		Bpod.__init__(self)

	def _publish_data(self, data):
		"""

		:param trial:
		"""
		Bpod._publish_data(self, data)
		self.gui_logger_fn(deepcopy(data))
