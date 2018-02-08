# !/usr/bin/python
# -*- coding: utf-8 -*-

import logging, sys, traceback, os

import pybpodgui_plugin
from datetime import datetime
from pybpodgui_plugin.com.run_handlers import PybranchRunHandler
from pybranch.com.messaging.stderr import StderrMessage
from pybranch.com.messaging.stdout import StdoutMessage
from pybpodapi.bpod import Bpod
from pybpodapi.session import Session
from pybpodapi.com.messaging.session_info 			import SessionInfo

logger = logging.getLogger(__name__)



class BpodRunner(PybranchRunHandler):
	"""

	"""
	INFO_CREATOR_NAME 		= 'CREATOR-NAME'
	INFO_PROJECT_NAME 		= 'PROJECT-NAME'
	INFO_EXPERIMENT_NAME 	= 'EXPERIMENT-NAME'
	INFO_BOARD_NAME 		= 'BOARD-NAME'
	INFO_SETUP_NAME 		= 'SETUP-NAME'
	INFO_SUBJECT_NAME 		= 'SUBJECT-NAME'
	INFO_BPODGUI_VERSION	= 'BPOD-GUI-VERSION'
	

	def __init__(self, in_queue=None, out_queue=None, refresh_time=None):
		"""

		:param in_queue:
		:param out_queue:
		:param refresh_time:
		"""

		PybranchRunHandler.__init__(self, in_queue, out_queue, refresh_time)

	def runner_bpod_run_protocol(self, bpod_settings, protocol_path, 
		user_name, project_name, experiment_name, board_name, 
		setup_name, session_name, session_path, subjects, variables):
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
		sys.path.insert(0,os.path.dirname(protocol_path))
		
		global_dict['PYBPOD_PROJECT'] 	   = project_name
		global_dict['PYBPOD_EXPERIMENT']   = experiment_name
		global_dict['PYBPOD_BOARD'] 	   = board_name
		global_dict['PYBPOD_SETUP'] 	   = setup_name
		global_dict['PYBPOD_SESSION'] 	   = session_name
		global_dict['PYBPOD_SESSION_PATH'] = session_path
		global_dict['PYBPOD_SUBJECTS'] 	   = subjects
		
		try:
			#execute the settings first
			exec(bpod_settings, global_dict)
			
			for var_name, var_value in variables: 
				global_dict[var_name] = var_value
			exec(open(protocol_path).read(), global_dict)
			
			#force bpod stop
			for var in global_dict.values():
				if isinstance(var, Bpod):
					var.stop()
					
		except Exception as err:
			self.my_print( StderrMessage( err ))

		for var in global_dict.values():
			if isinstance(var, Bpod):
				
				var.session += SessionInfo(self.INFO_CREATOR_NAME, 		user_name) 	# TODO
				var.session += SessionInfo(self.INFO_PROJECT_NAME, 		project_name) 	
				var.session += SessionInfo(self.INFO_EXPERIMENT_NAME, 	experiment_name)
				var.session += SessionInfo(self.INFO_SETUP_NAME, setup_name)
				var.session += SessionInfo(var.session.INFO_SESSION_ENDED, datetime.now())
				for subject in subjects: var.session += SessionInfo(self.INFO_SUBJECT_NAME, subject)
				var.session += SessionInfo(self.INFO_BPODGUI_VERSION, pybpodgui_plugin.__version__)
				del var
			

"""	def my_print(self, *args):
		if len(args)>1: 
			msg = ' '.join(map(str, args))
		else:
			msg = args[0]
		
		if isinstance(msg, str): msg = StdoutMessage(msg)

		#self.original_print(msg)
		self.log_msg(msg, last_call=False, evt_idx=self._current_evt_idx)
"""
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
