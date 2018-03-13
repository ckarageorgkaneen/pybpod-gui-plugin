#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import pyforms
from pyforms import conf
from pyforms import BaseWidget

logger = logging.getLogger(__name__)

try:
    from pyforms.controls import ControlCodeEditor
except:
    logger.error("Could not import ControlCodeEditor. Is QScintilla installed?")


class CodeEditor(BaseWidget):
    def __init__(self, other_taskfile):
        BaseWidget.__init__(self, other_taskfile.name if other_taskfile else '')

        self.layout().setContentsMargins(5, 5, 5, 5)

        self._code = ControlCodeEditor()
        self._code.value = other_taskfile.code

        self.other_taskfile = other_taskfile
        self._code.changed_event = self.__code_changed_evt

    def __code_changed_evt(self):
        self.other_taskfile.code = self._code.value
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
