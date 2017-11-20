# !/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from pybpodgui_plugin.com.run_handlers.bpod_runner import BpodRunner
from pybranch.thread_handlers.async_handler import AsyncHandler
from pybranch.thread_handlers.async_handler import dummy
from pybranch.thread_handlers.qt_thread import QtThread

logger = logging.getLogger(__name__)


class AsyncBpod(AsyncHandler):
	"""
	Provides info and actions related to serial connection when using multiprocessing
	"""

	def __init__(self, serial_port=None, baudrate=115200, inter_char_timeout=1,
				 thread_refresh_time=None, runner_refresh_time=None):
		"""

		:param serial_port:
		:param baudrate:
		:param inter_char_timeout:
		:param thread_refresh_time:
		"""

		self.serial_port = serial_port
		self.baudrate = baudrate
		self.inter_char_timeout = inter_char_timeout

		AsyncHandler.__init__(self, thread_refresh_time=thread_refresh_time, runner_refresh_time=runner_refresh_time)

	#######################################################################################
	###### OVERRIDE METHODS ###############################################################
	#######################################################################################


	def create_runner(self):
		_runner = BpodRunner(
			in_queue=self.in_queue,
			out_queue=self.out_queue,
			refresh_time=self.runner_refresh_time)

		logger.debug("Created PyBoardRunner")

		return _runner  # type: BpodRunner

	def start_handler_execution(self):
		AsyncHandler.start_handler_execution(self)

	def stop_handler_execution(self):
		AsyncHandler.stop_handler_execution(self)
		if self.runner and self.runner.is_running:
			self.runner.close_serial_port()
		logger.debug("Execution handler stopped")

	def run_protocol(self, bpod_settings, protocol_path, 
		project_name, experiment_name, user_name, board_name, setup_name, subjects, 
		variables,
		handler_evt=dummy, extra_args=None, group=None):
		self.call_function('runner_bpod_run_protocol', 
			args=(bpod_settings, protocol_path, project_name, user_name, 
				experiment_name, board_name, setup_name, subjects, variables),
			handler_evt=handler_evt,
			extra_args=extra_args,
			group=group
		)
