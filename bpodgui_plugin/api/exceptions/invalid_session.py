# !/usr/bin/python3
# -*- coding: utf-8 -*-


from bpodgui_plugin.api.exceptions.pycontrol_api_error import PyControlAPIError


class InvalidSessionError(PyControlAPIError):
	""" Exception raised when an invalid session is loaded"""

	def __init__(self, value, session_path=None, original_exception=None):
		PyControlAPIError.__init__(self, value, original_exception)
		self.session_path = session_path
