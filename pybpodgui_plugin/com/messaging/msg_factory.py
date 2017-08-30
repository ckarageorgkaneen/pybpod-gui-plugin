# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import re
import dateutil.parser

from pybranch.com.messaging.error 	import ErrorMessage
from pybranch.com.messaging.debug 	import DebugMessage
from pybranch.com.messaging.stderr 	import StderrMessage
from pybranch.com.messaging.stdout 	import StdoutMessage
from pybranch.com.messaging.warning import WarningMessage
from pybranch.com.messaging.parser  import MessageParser

from pybpodapi.bpod.com.messaging.base_message			import BaseMessage
from pybpodapi.bpod.com.messaging.end_trial				import EndTrial
from pybpodapi.bpod.com.messaging.trial					import Trial
from pybpodapi.bpod.com.messaging.event_occurrence 		import EventOccurrence
from pybpodapi.bpod.com.messaging.state_occurrence 		import StateOccurrence
from pybpodapi.bpod.com.messaging.softcode_occurrence 	import SoftcodeOccurrence

from pybpodapi.bpod.com.messaging.trial import Trial



logger = logging.getLogger(__name__)

class BpodMessageParser(MessageParser):

	MESSAGES_TYPES_CLASSES = [
		Trial,
		EndTrial,
		ErrorMessage,
		DebugMessage,
		StderrMessage,
		StdoutMessage,
		WarningMessage,
		SoftcodeOccurrence,
		StateOccurrence,
		EventOccurrence
	]


def parse_board_msg(data):
	"""
	Parses a board message and creates the appropriate event for session history.

	.. seealso::

		:py:meth:`pybpodgui_plugin.api.models.session.session_base.SessionBase.log_msg`

	:returns: list of board messages
	:rtype: list(BoardMessage)
	"""

	if not data:
		logger.warning("Parsed message: data is empty")
		return [ErrorMessage(data)]

	try:
		parsed_message = []

		if isinstance(data, BaseMessage):
			parsed_message.append(data)
		
	except Exception as err:
		logger.warning("Could not parse bpod message: {0}".format(data), exc_info=True)
		parsed_message.append(ErrorMessage(data))  # default case

	# logger.debug('Parsed message: {0} | Message type: {1}'.format(parsed_message, str(type(parsed_message))))

	return parsed_message
