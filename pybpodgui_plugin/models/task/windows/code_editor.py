#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import pyforms, os
from pyforms import conf
from pyforms import BaseWidget
from pyforms.controls import ControlCodeEditor

logger = logging.getLogger(__name__)

class CodeEditor(BaseWidget):

    def __init__(self, task):
        BaseWidget.__init__(self, task.name if task else '')
        self.set_margin(5)
        self.task = task
        
        try:
            with open(self.task.filepath, "r") as file: 
                code = file.read()
        except:
            code = ''

        self._code = ControlCodeEditor(default=code, changed_event=self.__code_changed_evt)

        
    def __code_changed_evt(self):
        if self.task.project.path is None:
            self.warning('It is not possible to save the file', 'The project does not exists yet. Please save it before to be able save this file.')

        # in case the file task file not exists yet
        if not self.task.filepath or not os.path.exists(self.task.filepath):

            # check if the tasks path exists, if not create it
            tasks_path = os.path.join(self.task.project.path, 'tasks')
            if not os.path.exists(tasks_path):  os.makedirs(tasks_path)

            # check if the task path exists, if not create it
            task_folder = os.path.join(tasks_path, self.task.name)
            if not os.path.exists(task_folder): os.makedirs(task_folder)

            # create an empty __init__.py file
            initfile = os.path.join(task_folder, '__init__.py')
            if not os.path.exists(initfile): 
                with open(initfile, "w") as file: pass

        # save the code to the file
        with open(self.task.filepath, "w") as file: file.write( self._code.value )

        return True


    def beforeClose(self):
        """ 
        Before closing window, ask user if she wants to save (if there are changes)
        
        .. seealso::
            :py:meth:`pyforms.gui.Controls.ControlMdiArea.ControlMdiArea._subWindowClosed`.
        
        """
        if self._code.is_modified:
            reply = self.question('Save the changes', 'Save the file')

            if reply:
                self.__code_changed_evt()


    @property
    def title(self):
        return BaseWidget.title.fget(self)

    @title.setter
    def title(self, value):
        BaseWidget.title.fset(self, "{0} task editor".format(value))


# Execute the application
if __name__ == "__main__":
    pyforms.start_app(CodeEditor)
