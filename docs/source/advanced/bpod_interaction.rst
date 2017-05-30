.. _bpod_communication-label:

****************
Bpod interaction
****************

.. warning::

    To be implemented soon:
        * Explaining  how GUI handles protocols and communicates with API.
        * How multiprocessing works.
        * How messages from bpod since "_publish_data" go to the multiprocessing queue until they are parsed on the factory.


From the moment you press the button "run" on the GUI until output shows up in the console and it is saved on session history file, a lot of stuff is going on.

=====================
Handling "run button"
=====================

.. image:: /_images/bpod_interaction/setup_window_detail.png
    :scale: 100 %

First, let's see how the GUI handles the "run" button. SetupWindow class is responsible for painting the setup window, including input fields and buttons.

.. code-block:: python

    class SetupWindow(Setup, BaseWidget):
        """
        Define here which fields from the setup model should appear on the details section.

        The model fields shall be defined as UI components like text fields, buttons, combo boxes, etc.

        You may also assign actions to these components.

        (...)

        """

        def __init__(self, experiment=None):
            BaseWidget.__init__(self, 'Experiment')
            self.layout().setContentsMargins(5, 10, 5, 5)

            self._name = ControlText('Subject name')
            self._board = ControlCombo('Box')
            self._run_task_btn = ControlButton('Run')

            Setup.__init__(self, experiment)

            self.reload_boards()

            self._formset = [
                '_name',
                '_board',
                (' ', ' ', '_run_task_btn'),
                ' '
            ]

            self._name.changed_event = self.__name_changed_evt
            self._board.changed_event = self.__board_changed_evt

            self._run_task_btn.value = self._run_task

            def _run_task(self):
                """
                Defines behavior of the button :attr:`SetupWindow._run_task_btn`.

                This methods is called every time the user presses the button.
                """
                try:
                    if self.status == SetupWindow.STATUS_RUNNING_TASK_HANDLER:
                        self.stop_task()
                    elif self.status == SetupWindow.STATUS_READY:
                        self.run_task()
                except RunSetupError as err:
                    QMessageBox.warning(self, "Warning", str(err))
                except Exception as err:
                    QMessageBox.critical(self, "Unexpected Error", str(err))


Pressing "run" will fire a complex sequence of calls as we will see later.

=====================
Multiprocessing
=====================

.. image:: /_images/bpod_interaction/gui-multiprocessing-highlevel.png
    :scale: 100 %
