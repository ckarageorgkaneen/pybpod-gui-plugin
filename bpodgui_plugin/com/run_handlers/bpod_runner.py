# !/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from bpodgui_plugin.com.run_handlers import PybranchRunHandler

from bpodgui_plugin.com.bpod_instance import BpodInstance

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

	def runner_bpod_run(self, serial_port, protocol_path):
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
		BPOD_INSTANCE = BpodInstance(self.my_print).start(serial_port)
		ldict = locals()
		exec(open(protocol_path).read(), globals(), ldict)
		mybpod = ldict['my_bpod']
		BPOD_INSTANCE.disconnect()
		#print(mybpod.session)

#		self.log_msg("P 1 Bpod now running\n", last_call=False, evt_idx=self._current_evt_idx)
#		self.log_msg("P 2 Bpod serial port: {0}\n".format(serial_port), last_call=False, evt_idx=self._current_evt_idx)
#		self.log_msg("P 3 Bpod protocol path: {0}\n".format(protocol_path), last_call=False, evt_idx=self._current_evt_idx)


	def my_print(self, *args):
		# self.log_msg("P 1 {0}\n".format(args[0]), last_call=False, evt_idx=self._current_evt_idx)
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
