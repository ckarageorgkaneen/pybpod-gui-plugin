# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

import pyforms as app
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pybpodgui_api.models.task import Task

from pybpodgui_api.models.task.other_taskfile import OtherTaskFile

logger = logging.getLogger(__name__)


class OtherTaskFileWindow(OtherTaskFile, BaseWidget):
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

    def __init__(self, task=None):
        BaseWidget.__init__(self, 'Other task file')
        
        self.layout().setContentsMargins(5, 10, 5, 5)

        self._name_field = ControlText('Task name')
        self._edit_btn = ControlButton('Edit')

        self._formset  = [
            '_name_field',
            (' ', '_edit_btn'),
            ' '
        ]

        #self._name.changed_event = self.__name_edited_evt

        OtherTaskFile.__init__(self, task)


    @property
    def name(self): return OtherTaskFile.name.fget(self)

    @name.setter
    def name(self, value):
        OtherTaskFile.name.fset(self, value)
        self._name_field.value = value
        


        