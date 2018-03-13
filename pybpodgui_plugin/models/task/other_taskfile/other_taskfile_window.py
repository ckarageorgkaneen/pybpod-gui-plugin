# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

import pyforms as app
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlCheckBox
from pybpodgui_api.models.task import Task

from pybpodgui_plugin.models.task.other_taskfile.windows.code_editor import CodeEditor
from pybpodgui_api.models.task.other_taskfile                        import OtherTaskFile

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

        self._name_field = ControlText('Task name', changed_event=self.__name_changed_evt)
        self._edit_btn   = ControlButton('Edit')

        self._execute_field  = ControlCheckBox('Execute before the task', changed_event=self.__execute_changed_evt)
        self._detached_field = ControlCheckBox('Detached execution', changed_event=self.__detached_changed_evt)


        self._formset  = [
            '_name_field',
            (' ', '_edit_btn'),
            '_execute_field',
            '_detached_field',
            ' '
        ]

        #self._name.changed_event = self.__name_edited_evt

        OtherTaskFile.__init__(self, task)

    def __name_changed_evt(self):
        self.name = self._name_field.value

    def __execute_changed_evt(self):
        self._execute = self._execute_field.value

    def __detached_changed_evt(self):
        #self._update_detached_flag = True
        self._detached = self._detached_field.value

    def edit_btn_evt(self):
        """
        Open code editor window on the mdi section for the task source code.

        .. seealso::
            This event may be fired on:
                * Double click event (tree node): :py:meth:`pybpodgui_plugin.models.task.task_treenode.TaskTreeNode.node_double_clicked_event`.
                * Key press event (tree node): :py:meth:`pybpodgui_plugin.models.task.task_treenode.TaskTreeNode.node_key_pressed_event`.
        """
        if self.project.path is None:
            self.warning("The project was not saved yet.\nPlease save it first.", "Cannot edit the file yet.")
        else:
            try:
                if not hasattr(self, '_code_editor'):
                    self._code_editor = CodeEditor(self)
                self.mainwindow.mdi_area += self._code_editor
            except FileNotFoundError as err:
                logger.warning(str(err))
                self.warning(
                    "Task file does not exist yet.\nPlease save the project to create the task file.",
                    "Cannot edit the file yet.")

    @property
    def name(self): return OtherTaskFile.name.fget(self)

    @name.setter
    def name(self, value):
        OtherTaskFile.name.fset(self, value)
        self._name_field.value = value


    @property
    def execute(self): return OtherTaskFile.execute.fget(self)

    @execute.setter
    def execute(self, value):
        OtherTaskFile.execute.fset(self, value)
        self._execute_field.value = value
        

    @property
    def detached(self): return OtherTaskFile.detached.fget(self)

    @detached.setter
    def detached(self, value):
        OtherTaskFile.detached.fset(self, value)
        self._detached_field.value = value
        



        