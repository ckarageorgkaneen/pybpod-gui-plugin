# !/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from pybpodgui_plugin.com.run_handlers import PybranchRunHandler
from pybpodgui_plugin.com.bpod_instance import BpodInstance

logger = logging.getLogger(__name__)


class BpodRunner(PybranchRunHandler):
	"""

	"""

	def __init__(self, in_queue=None, out_queue=None, refresh_time=None):
		"""

		:param in_queue:
		:param out_queue:
		:param refresh_time:
		"""

		PybranchRunHandler.__init__(self, in_queue, out_queue, refresh_time)

	def runner_bpod_run_protocol(self, serial_port, protocol_name, protocol_path, workspace_path):
		"""

		http://stackoverflow.com/questions/14197009/how-can-i-redirect-print-output-of-a-function-in-python
		http://stackoverflow.com/questions/550470/overload-print-python
		http://stackoverflow.com/questions/33291792/cleanly-and-optionally-redirect-stderr-or-stdout-to-file
		http://stackoverflow.com/questions/1463306/how-does-exec-work-with-locals

		:param serial_port:
		:param protocol_path:
		:return:
		"""
		print = self.my_print
		BPOD_INSTANCE = BpodInstance(self.my_print).start(serial_port, workspace_path, protocol_name)
		ldict = locals()
		exec(open(protocol_path).read(), globals(), ldict)
		mybpod = ldict['my_bpod']
		BPOD_INSTANCE.stop()

	def my_print(self, *args):
		self.log_msg(args[0], last_call=False, evt_idx=self._current_evt_idx)

#
# class MyWriter(object):
#
# 	def __init__(self, queue_handler):
# 		self.queue_handler = queue_handler
#
#
# 	def write(self, my_string):
# 		self.queue_handler.log_msg("P 1 {0}\n".format(my_string), last_call=False, evt_idx=self._current_evt_idx)
#
#
