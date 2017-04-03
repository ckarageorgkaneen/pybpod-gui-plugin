***************************
Writing a protocol for Bpod
***************************

What is a Bpod protocol?
========================

To use Bpod, you must first program a behavioral protocol. The following guide is based on the original version for `Bpod Matlab <https://sites.google.com/site/bpoddocumentation/bpod-user-guide/protocol-writing>`_.


Protocol example explained
==========================

First, import necessary modules from the pybpod-api library and initialize Bpod. The GUI will automatically set the serial port based on the serial port selected for the board and the workspace will be the the subject folder.

.. code-block:: python
    :linenos:
    :lineno-start: 1

    import random
    from pybpodapi.model.state_machine import StateMachine


    my_bpod = BPOD_INSTANCE # DO NOT CHANGE THIS LINE, KEEP IT EXACTLY LIKE THIS

.. seealso::

    * Bpod class: :py:class:`pybpodapi.model.bpod.Bpod`
    * Bpod start method: :py:meth:`pybpodapi.model.bpod.Bpod.start`


You can run several trials for each Bpod execution. In this example, we will use 5 trials. Each trial can be of type1 (rewarded left) or type2 (rewarded right).

.. code-block:: python
    :linenos:
    :lineno-start: 2

    nTrials = 5
    trialTypes = [1, 2]  # 1 (rewarded left) or 2 (rewarded right)

    for i in range(nTrials):  # Main loop
        print('Trial: {0}'.format(i + 1))

        thisTrialType = random.choice(trialTypes)  # Randomly choose trial type
        if thisTrialType == 1:
            stimulus = 'PWM1'  # set stimulus channel for trial type 1
            leftAction = 'Reward'
            rightAction = 'Punish'
            rewardValve = 1
        elif thisTrialType == 2:
            stimulus = 'PWM3'  # set stimulus channel for trial type 1
            leftAction = 'Punish'
            rightAction = 'Reward'
            rewardValve = 3


Now, inside the loop, we will create and configure a state machine for each trial.

.. code-block:: python
    :linenos:
    :lineno-start: 18

        sma = StateMachine(my_bpod.hardware)

        sma.add_state(
            state_name='WaitForPort2Poke',
            state_timer=1,
            state_change_conditions={'Port2In': 'FlashStimulus'},
            output_actions=[('PWM2', 255)])
        sma.add_state(
            state_name='FlashStimulus',
            state_timer=0.1,
            state_change_conditions={'Tup': 'WaitForResponse'},
            output_actions=[(stimulus, 255)])
        sma.add_state(
            state_name='WaitForResponse',
            state_timer=1,
            state_change_conditions={'Port1In': leftAction, 'Port3In': rightAction},
            output_actions=[])
        sma.add_state(
            state_name='Reward',
            state_timer=0.1,
            state_change_conditions={'Tup': 'exit'},
            output_actions=[('Valve', rewardValve)])  # Reward correct choice
        sma.add_state(
            state_name='Punish',
            state_timer=3,
            state_change_conditions={'Tup': 'exit'},
            output_actions=[('LED', 1), ('LED', 2), ('LED', 3)])  # Signal incorrect choice

.. seealso::

    * :py:class:`pybpodapi.model.state_machine.state_machine.StateMachine`
    * :py:meth:`pybpodapi.model.state_machine.state_machine.StateMachine.add_state`

After configuring the state machine, we send it to the Bpod device by calling the method *send_state_machine*. We are then ready to run the next trial, by calling the *run_state_machine* method.
On run completion, we can print the data that was returned and stored on the *raw_events* variable. On this state, the trial events have been already processed and you don't have to execute anything else.
Finally, the Bpod is disconnected automatically.

.. code-block:: python
    :linenos:
    :lineno-start: 45

        my_bpod.send_state_machine(sma)  # Send state machine description to Bpod device

        print("Waiting for poke. Reward: {0}".format('left' if thisTrialType == 1 else 'right'))

        my_bpod.run_state_machine(sma)  # Run state machine

        print("Raw events: {0}".format(sma.raw_data)) # print data

.. seealso::

    * :py:meth:`pybpodapi.model.bpod.Bpod.send_state_machine`
    * :py:meth:`pybpodapi.model.bpod.Bpod.run_state_machine`
    * :py:meth:`pybpodapi.model.bpod.Bpod.add_trial_events`
    * :py:meth:`pybpodapi.model.bpod.Bpod.stop`


Try the example
===============

You can try the this example by unziping and opening the :download:`simple_project_pybpod.zip </_static/simple_project_pybpod.zip>` on the GUI.