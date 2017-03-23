# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pybpodgui_plugin.api.exceptions.pycontrol_api_error import PyControlAPIError


class PycontrolError(PyControlAPIError):
	""" Exception raised when a board operation fails"""
	pass
