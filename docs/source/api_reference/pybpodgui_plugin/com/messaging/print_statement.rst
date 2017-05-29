.. _api_reference_print_statement-label:

==========================================
:mod:`print_statement` --- Print statement
==========================================

.. module:: pybpodgui_plugin.com.messaging.print_statement
   :synopsis: Experiment communication

--------
Overview
--------

User defined print messages on protocol. Example of a protocol:

.. code-block:: python

	my_bpod = BPOD_INSTANCE

	sma = StateMachine(my_bpod.hardware)

	sma.add_state(
		state_name='myState',
		state_timer=1,
		state_change_conditions={EventName.Tup: 'exit'},
		output_actions=[])

	my_bpod.send_state_machine(sma)

	print("Running state matrix now...")

	my_bpod.run_state_machine(sma)

	print("Current trial info: {0}".format(my_bpod.session.current_trial()))

	my_bpod.stop()


"Print" messages will show up on session history:

::

    print_statement, 2017-05-29T18:22:36.486828, Running state matrix now...
    event_occurrence, 2017-05-29T18:22:37.489392, 88, Tup, 2017-05-29 18:22:37.489392
    state_entry, 2017-05-29T18:22:37.517053, 1, myState, 0, 1.0
    state_change, 2017-05-29T18:22:37.517075, 1, Tup, 1.0
    print_statement, 2017-05-29T18:22:37.536195, Current trial info: {'Bpod start timestamp': 0.009, 'States timestamps': {'myState': [(0, 1.0)]}, 'Events timestamps': {'Tup': [1.0]}}


--------------
Implementation
--------------

.. autoclass:: pybpodgui_plugin.com.messaging.print_statement.PrintStatement
    :members:
    :private-members:

