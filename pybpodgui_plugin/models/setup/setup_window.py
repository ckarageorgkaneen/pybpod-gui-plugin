# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging, re

from pyforms import conf

import pyforms as app

from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlList
from pyforms.controls import ControlButton
from pyforms.controls import ControlCombo
from pyforms.controls import ControlNumber
from pyforms.controls import ControlCheckBox
from pyforms.controls import ControlEmptyWidget

from pybpodgui_plugin.models.subject import Subject
from pybpodgui_api.models.setup import Setup
from pybpodgui_api.exceptions.run_setup import RunSetupError

from pybpodgui_plugin.models.setup.board_task import BoardTask
from pybpodgui_plugin.models.session import Session

logger = logging.getLogger(__name__)


class SetupWindow(Setup, BaseWidget):
    """
    Define here which fields from the setup model should appear on the details section.

    The model fields shall be defined as UI components like text fields, buttons, combo boxes, etc.

    You may also assign actions to these components.

    **Properties**

        name
            :class:`string`

            Name associated with this setup. Returns the current value stored in the :py:attr:`_name` text field.

        board
            :class:`pybpodgui_plugin.models.board.board_dockwindow.BoardDockWindow`

            Board associated with this setup. Returns the current value stored in the :py:attr:`_board` combo box.

    **Private attributes**

        _name
            :class:`pyforms.controls.ControlText`

            Text field to edit board name. Editing this field fires the event :meth:`SetupWindow._SetupWindow__name_changed_evt`.

        _board
            :class:`pyforms.controls.ControlCombo`

            Combo box to select board associated with this setup. Editing this field fires the event :meth:`SetupWindow._SetupWindow__board_changed_evt`.

        _run_task_btn
            :class:`pyforms.controls.ControlButton`

            Button to run task on board. Pressing the button fires the event :meth:`SetupWindow._SetupWindow__run_task`.

        _formset
            Describe window fields organization to PyForms.

    **Methods**

    """

    def __init__(self, experiment=None):
        """

        :param experiment: Experiment this setup belongs to.
        """
        BaseWidget.__init__(self, 'Experiment')
        self.layout().setContentsMargins(5, 10, 5, 5)

        self._name          = ControlText('Setup name')
        self._board         = ControlCombo('Board')
        
        self._stoptrial_btn = ControlButton('Stop trial', default=self._stop_trial_evt)
        self._pause_btn     = ControlButton('Pause', checkable=True, default=self._pause_evt)
        self._run_task_btn  = ControlButton('Run', checkable=True, default=self._run_task)
        
        self._subjects_list = ControlList('Subjects', remove_function=self.__remove_subject)
        self._add_subject   = ControlButton('Add subject')
        self._allsubjects   = ControlCombo('Add subject')
        self._task          = ControlCombo('Protocol', changed_event=self.__task_changed_evt)
        
        self._detached      = ControlCheckBox('Detach from GUI')

        self._varspanel     = ControlEmptyWidget()
        self._btn           = ControlButton('Open')

        

        Setup.__init__(self, experiment)

        self.reload_boards()
        self.reload_tasks()


        self._formset = [
            '_name',
            '_board',
            '_task',
            ('_detached', '_run_task_btn'),
            ('_stoptrial_btn','_pause_btn'),
            '=',
            {   
                'Subjects':[
                    '_allsubjects',
                    '_add_subject',
                    '_subjects_list',
                ],
                'Variables':[
                    '_varspanel',
                ],
            }           
        ]

        self._subjects_list.readonly = True
        self._varspanel.value     = self.board_task
        self._add_subject.value   = self.__add_subject
        self._name.changed_event  = self.__name_changed_evt
        self._board.changed_event = self.__board_changed_evt
        

    def reload_tasks(self, current_selected_task=None):
        # type: (Task) -> None
        """
        Reload tasks now

        :param current_selected_task: current selected task
        :type current_selected_task: pybpodgui_plugin.models.task.Task
        """
        self._task.clear()
        self._task.add_item('', 0)
        for task in self.project.tasks:
            self._task.add_item(task.name, task)
        self._task.current_index = 0
        if current_selected_task:
            self.task = current_selected_task
    
    def __task_changed_evt(self):
        if hasattr(self, '_update_task'): return 
        self.task = self._task.value

    def __add__(self, obj):
       res = super(SetupWindow, self).__add__(obj)
       if isinstance(obj, Subject):
           self._subjects_list.value = [[s.name] for s in self.subjects]
       return res

    def __sub__(self, obj):
       res = super(SetupWindow, self).__sub__(obj)
       if isinstance(obj, Subject):
           self._subjects_list.value = [[s.name] for s in self.subjects]
       return res

    def __add_subject(self):
        self += self._allsubjects.value

    def __remove_subject(self):
        if self._subjects_list.selected_row_index is not None:
            name    = self._subjects_list.value[self._subjects_list.selected_row_index][0]
            subject = self.project.find_subject(name)
            self    -= subject
            self._subjects_list -= -1

    def _stop_trial_evt(self):
        self.stop_trial()

    def _pause_evt(self):
        if self._pause_btn.checked:
            self.pause_trial()
        else:
            self.resume_trial()

    def _run_task(self):
        """
        Defines behavior of the button :attr:`SetupWindow._run_task_btn`.

        This methods is called every time the user presses the button.
        """
        try:
            if self.status == SetupWindow.STATUS_RUNNING_TASK:
                self.stop_task()
            elif self.status == SetupWindow.STATUS_READY:
                self.run_task()
        except RunSetupError as err:
            self.warning(str(err), "Warning")
        except Exception as err:
            self.alert(str(err), "Unexpected Error")

    def __board_changed_evt(self):
        """
        React to changes on text field :py:attr:`_board`.

        This method is called every time the user changes the field and forces a UI refresh.
        """
        if hasattr(self, '_update_board'): return 
        self.board = self._board.value
        self.update_ui()

    def __name_changed_evt(self):
        """
        React to changes on text field :py:attr:`_name`.

        This methods is called every time the user changes the field.
        """
        if not hasattr(self, '_update_name') or not self._update_name:
            self.name = self._name.value

    def reload_boards(self, current_selected_board=None):
        """
        Reload boards list on combo box

        This method is fired by:
            * setup creation: :py:meth:`pybpodgui_plugin.models.setup.setup_window.SetupWindow._SetupWindow__init__`.
            * setup details section focus (dockwindow): :py:meth:`pybpodgui_plugin.models.setup.setup_dockwindow.SetupDockWindow.show`.

        :param current_selected_board: optional specify current selected board to restore after list update
        """
        self._board.clear()
        self._board.add_item('', 0)
        for board in self.project.boards: self._board.add_item(board.name, board)
        self._board.current_index = 0

        if current_selected_board:  self.board = current_selected_board

        self._allsubjects.clear()
        self._allsubjects.add_item('', 0)
        for subject in sorted([s for s in self.project.subjects], key=lambda x: x.name.lower()): 
            self._allsubjects.add_item(subject.name, subject)
        self._allsubjects.current_index = 0

        self._subjects_list.value = [[s.name] for s in self.subjects]


    def create_board_task(self):
        """
        Creates a new board task by calling the API.

        .. seealso::
            :py:class:`pybpodgui_api.models.setup.board_task.BoardTask`.
        """
        return BoardTask(self)

    def create_session(self):
        """
        Creates a new session by calling the API.

        .. seealso::
            :py:class:`pybpodgui_api.models.session.session_base.SessionBase`.
        """
        return Session(self)

    @property
    def name(self):
        return self._name.value

    @name.setter
    def name(self, value):
        self._update_name = True  # Flag to avoid recurse calls when editing the name text field
        self._name.value = value
        self._update_name = False
        # Update the session windows names
        if hasattr(self, 'sessions'):
            for session in self.sessions:
                session.name = session.name

    @property
    def board(self):
        if isinstance(self._board.value, str) or isinstance(self._board.value, int): return None
        return self._board.value

    @board.setter
    def board(self, value):
        if isinstance(value, str): value = self.project.find_board(value)
        self._update_board = True  # Flag to avoid recurse calls when editing the name text field
        
        if value not in self._board.values: self.reload_boards()
        self._board.value = value
        del self._update_board
        Setup.board.fset(self, value)

    @property
    def task(self):
        if isinstance(self._task.value, str) or isinstance(self._task.value, int): return None
        return self._task.value

    @task.setter
    def task(self, value):
        if isinstance(value, str): value = self.project.find_task(value)
        
        self._update_task = True  # Flag to avoid recurse calls when editing the name text field
        
        if value not in self._task.values: self.reload_tasks()
        self._task.value = value
        del self._update_task
        Setup.task.fset(self, value)

    @property
    def detached(self): return self._detached.value
    @detached.setter
    def detached(self, value): self._detached.value = value


# Execute the application
if __name__ == "__main__":
    app.start_app(SetupWindow)
