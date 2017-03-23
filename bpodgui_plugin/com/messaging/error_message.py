# !/usr/bin/python3
# -*- coding: utf-8 -*-

from bpodgui_plugin.com.messaging.board_message import BoardMessage


class ErrorMessage(BoardMessage):
	""" Message that represents an error """
	MESSAGE_TYPE_ALIAS = 'error_message'
