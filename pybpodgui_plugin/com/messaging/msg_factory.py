# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import re
import dateutil.parser

from pybpodapi.trial import Trial as BpodTrial
from pybpodapi.event_occurrence import EventOccurrence as BpodEventOccurrence

from pybpodgui_plugin.com.messaging import ErrorMessage
from pybpodgui_plugin.com.messaging import BoardMessage
from pybpodgui_plugin.com.messaging import PrintStatement
from pybpodgui_plugin.com.messaging import StateChange
from pybpodgui_plugin.com.messaging import StateEntry
from pybpodgui_plugin.com.messaging import EventOccurrence

logger = logging.getLogger(__name__)


def parse_session_msg(data):
	"""
	Parses messages saved on session history file

	.. seealso::

		:py:meth:`pybpodgui_plugin.api.models.session.session_io.SessionIO.load_contents`


	:param str data: file line entry
	:returns: list of history messages
	:rtype: list(BoardMessage)
	"""

	# logger.debug("Parsing message from session file: %s", data)

	if not data:
		logger.warning("Parsed message: data is empty")
		return ErrorMessage(data)

	try:

		parsed_message = None

		message_code = re.compile(r'(?P<type>.*?),.*').search(data).group('type')

		if message_code is None:
			raise Exception("Unknown message code: %s", message_code)

		elif message_code == PrintStatement.MESSAGE_TYPE_ALIAS:
			# sample: print_statement, 2017-03-27T14:05:23.580120, Raw events: {'States': [0], 'TrialStartTimestamp': [0.007], 'EventTimestamps': [1.0], 'Events': [88], 'StateTimestamps': [0, 1.0]}
			regex = re.compile(r'.*?\s(?P<timestamp>.*?),\s(?P<value>.*)')
			result = regex.search(data)
			parsed_message = PrintStatement(result.group('value'))
			parsed_message.pc_timestamp = dateutil.parser.parse(result.group('timestamp'))

		elif message_code == StateChange.MESSAGE_TYPE_ALIAS:
			# sample: state_change, 2017-03-27T14:05:22.581343, 1, Tup, 1.0
			regex = re.compile(
				r'.*?\s(?P<pc_timestamp>.*?),\s(?P<event_id>.*),\s(?P<event_name>.*),\s(?P<board_timestamp>.*)')
			result = regex.search(data)
			parsed_message = StateChange(result.group('event_name'), float(result.group('board_timestamp')),
			                             int(result.group('event_id')))
			parsed_message.pc_timestamp = dateutil.parser.parse(result.group('pc_timestamp'))

		elif message_code == StateEntry.MESSAGE_TYPE_ALIAS:
			# sample state_entry, 2017-03-27T14:05:22.581329, 1, myState, 0
			regex = re.compile(
				r'.*?\s(?P<pc_timestamp>.*?),\s(?P<state_id>.*),\s(?P<state_name>.*),\s(?P<start_timestamp>.*),\s(?P<end_timestamp>.*)')
			result = regex.search(data)
			parsed_message = StateEntry(result.group('state_name'), float(result.group('start_timestamp')),
			                            float(result.group('end_timestamp')), int(result.group('state_id')))
			parsed_message.pc_timestamp = dateutil.parser.parse(result.group('pc_timestamp'))

		elif message_code == EventOccurrence.MESSAGE_TYPE_ALIAS:
			# sample event_occurrence, 2017-04-28T15:30:19.940747, 88, Tup, None
			regex = re.compile(
				r'.*?\s(?P<pc_timestamp>.*?),\s(?P<bpod_event_code>.*),\s(?P<bpod_event_name>.*),\s.*')
			result = regex.search(data)
			parsed_message = EventOccurrence(result.group('bpod_event_name'),
			                                 dateutil.parser.parse(result.group('pc_timestamp')),
			                                 result.group('bpod_event_code'))
			parsed_message.pc_timestamp = dateutil.parser.parse(result.group('pc_timestamp'))

		else:
			raise Exception("Unknown message code: %s", message_code)

	except Exception as err:
		logger.warning("Could not parse bpod message: {0}".format(data), exc_info=True)
		parsed_message = ErrorMessage(data)  # default case

	# logger.debug('Parsed message: {0} | Message type: {1}'.format(parsed_message, str(type(parsed_message))))

	return parsed_message


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

		if isinstance(data, BpodEventOccurrence):
			bpod_event_occurrence = data
			parsed_message.append(EventOccurrence(bpod_event_occurrence.name, bpod_event_occurrence.timestamp,
			                                      bpod_event_occurrence.index))

			logger.debug(str(bpod_event_occurrence))

		elif isinstance(data, BpodTrial):
			bpod_trial = data
			states = bpod_trial.states_occurrences
			events = bpod_trial.get_all_timestamps_by_event()

			for index, state in enumerate(states, start=1):
				for state_duration in state.timestamps:
					parsed_message.append(StateEntry(state.name, state_duration.start, state_duration.end, index))

			for index, event_name in enumerate(events.keys(), start=1):
				for event_timestamp in events[event_name]:
					parsed_message.append(StateChange(event_name, event_timestamp, index))

		elif isinstance(data, str):
			# get message code (character variable number string before the first space)
			message_code = data.split(' ')[0]
			if message_code == '!':
				parsed_message.append(ErrorMessage(data))

			else:
				data = str(data).strip()
				parsed_message.append(PrintStatement(data))


	except Exception as err:
		logger.warning("Could not parse bpod message: {0}".format(data), exc_info=True)
		parsed_message.append(ErrorMessage(data))  # default case

	# logger.debug('Parsed message: {0} | Message type: {1}'.format(parsed_message, str(type(parsed_message))))

	return parsed_message
