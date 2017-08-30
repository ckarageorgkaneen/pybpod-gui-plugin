# !/usr/bin/python
# -*- coding: utf-8 -*-

import logging, sys, traceback

from pybpodgui_plugin.com.run_handlers import PybranchRunHandler
from pybranch.com.messaging.stderr import StderrMessage
from pybpodapi.bpod import Bpod

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
		global_dict = globals()
		local_dict  = locals()

		__builtins__['print'] = self.my_print


		try:

			exec("""
from pysettings import conf

class RunnerSettings:
	SETTINGS_PRIORITY = 0
	WORKSPACE_PATH 	= None
	PROTOCOL_NAME 	= None
	SERIAL_PORT 	= '{serialport}'

	PYBPOD_API_PUBLISH_DATA_FUNC = print

conf += RunnerSettings
			""".format(serialport=serial_port, workspace=workspace_path), 
			global_dict, local_dict)

			exec( open(protocol_path).read(), global_dict, local_dict)
			for var in local_dict.values():
				if isinstance(var, Bpod):
					var.stop()

		except Exception as err:
			self.my_print( StderrMessage( err ))
			

	def my_print(self, *args):
		if len(args)>1: 
			msg = ' '.join(map(str, args))
		else:
			msg = args[0]
			
		self.log_msg(msg, last_call=False, evt_idx=self._current_evt_idx)

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
