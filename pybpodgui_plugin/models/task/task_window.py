# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

import pyforms as app
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlNumber
from pyforms.controls import ControlCheckBox
from pybpodgui_api.models.task import Task

from .other_taskfile import OtherTaskFile

logger = logging.getLogger(__name__)


class TaskWindow(Task, BaseWidget):
    """
    Define here which fields from the task model should appear on the details section.

    The model fields shall be defined as UI components like text fields, buttons, combo boxes, etc.

    You may also assign actions to these components.

    **Properties**

        name
            :class:`string`

            Name associated with this task. Returns the current value stored in the :py:attr:`_name` text field.

    **Private attributes**

        _name
            :class:`pyforms.controls.ControlText`

            Text field to edit task name. Editing this field fires the event :meth:`TaskWindow._TaskWindow__name_edited_evt`.

        _edit_btn
            :class:`pyforms.controls.ControlButton`

            Button to edit task code. Pressing the button fires the event :meth:`BoardWindow._BoardWindow__install_framework_btn_evt`.

        _formset
            Describe window fields organization to PyForms.

    **Methods**

    """

    def __init__(self, project=None):
        BaseWidget.__init__(self, 'Task')
        self.layout().setContentsMargins(5, 10, 5, 5)

        self._name       = ControlText('Task name')
        self._edit_btn   = ControlButton('Edit')
        self._use_server = ControlCheckBox('Trigger soft codes using a UDP port')
        
        self._formset = [
            '_name',
            (' ', '_edit_btn'),
            '_use_server',
            ' '
        ]

        self._name.changed_event = self.__name_edited_evt

        Task.__init__(self, project)



    def __use_server_changed_evt(self):
        if self._use_server.value:
            self._netport.enabled = True
        else:
            self._netport.enabled = False


    def __name_edited_evt(self):
        """
        React to changes on text field :py:attr:`_name`.

        This methods is called every time the user changes the field.
        """
        if not hasattr(self, '_update_name') or not self._update_name:
            self.name = self._name.value

    def create_otherfile(self):
        """
        Add a other file to a task and return it.
        
        :rtype: Experiment
        """
        return OtherTaskFile(self)

    @property
    def name(self): return self._name.value

    @name.setter
    def name(self, value):
        self._update_name = True  # Flag to avoid recurse calls when editing the name text field
        self._name.value = value
        self._update_name = False

    @property
    def trigger_softcodes(self):
        return self._use_server.value

    @trigger_softcodes.setter
    def trigger_softcodes(self, value):
        self._use_server.value = value==True



# Execute the application
if __name__ == "__main__":
    app.start_app(TaskWindow)
