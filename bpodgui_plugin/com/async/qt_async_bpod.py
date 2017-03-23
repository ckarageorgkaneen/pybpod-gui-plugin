# !/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from pybranch.thread_handlers.async_handler import AsyncHandler
from pybranch.thread_handlers.qt_thread import QtThread

logger = logging.getLogger(__name__)


class QtAsyncBpod(AsyncHandler):
	"""
	Provides info and actions related to serial connection when using multiprocessing
	"""

	def create_async_thread(self):
		qtt = QtThread(out_queue=self.out_queue,
		               in_queue=self.in_queue,
		               wait_for_results_fn=self.wait_for_results,
		               event_executor_fn=self.event_executor, mainwindow=self.mainwindow)

		logger.debug("Created QtThread")

		return qtt
