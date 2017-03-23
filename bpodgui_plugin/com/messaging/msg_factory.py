# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pybpodapi.model.trial import Trial as BpodTrial

from bpodgui_plugin.com.messaging.error_message import ErrorMessage

from bpodgui_plugin.com.messaging.print_statement import PrintStatement
from bpodgui_plugin.com.messaging.event_fired import EventFired
from bpodgui_plugin.com.messaging.state_entry import StateEntry

logger = logging.getLogger(__name__)


def parse_board_msg(data):
	"""
	Parse board message and return appropriate event
	:param board_task: the board and task association
	:type board_task: pycontrolapi.models.board_task
	:param data: data to be parsed
	:type data: string
	:returns: list with instances of HistoryMessage
	"""

	if not data:
		logger.warning("Parsed message: data is empty")
		return [ErrorMessage(data)]

	try:

		parsed_message = []

		if isinstance(data, BpodTrial):
			bpod_trial = data
			#			states = bpod_instance.session.trials[0].states_timestamps
			#			events = bpod_instance.session.trials[0].events_timestamps
			states = bpod_trial.states_timestamps
			events = bpod_trial.events_timestamps

			for index, state_name in enumerate(states.keys(), start=1):
				for state_timestamp in states[state_name][0]:
					parsed_message.append(StateEntry(state_name, state_timestamp, index))

			for index, event_name in enumerate(events.keys(), start=1):
				for event_timestamp in events[event_name]:
					parsed_message.append(EventFired(event_name, event_timestamp, index))

		else:
			data = str(data).strip()

			parsed_message.append(PrintStatement(data))


	except Exception as err:
		# The msg is considered a comment for the cases where the events formats are not correct
		logger.warning("Could not parse bpod message: {0}".format(data), exc_info=True)
		parsed_message = ErrorMessage(data)  # default case

	# logger.debug('Parsed message: {0} | Message type: {1}'.format(parsed_message, str(type(parsed_message))))

	return parsed_message
