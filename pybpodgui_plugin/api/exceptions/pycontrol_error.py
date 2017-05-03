# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pybpodgui_plugin.api.exceptions.api_error import APIError


class PycontrolError(APIError):
	""" Exception raised when a board operation fails"""
	pass
