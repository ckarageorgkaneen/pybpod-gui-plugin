# !/usr/bin/python3
# -*- coding: utf-8 -*-

from bpodgui_plugin.api.exceptions.pycontrol_api_error import PyControlAPIError


class BoardError(PyControlAPIError):
	""" Exception raised when a board operation fails"""
	pass
