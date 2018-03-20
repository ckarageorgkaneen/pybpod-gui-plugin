#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging, shutil
import pyforms, os
from pyforms import conf
from pyforms import BaseWidget, hsplitter, vsplitter
from pyforms.controls import ControlTreeView
from pyforms.controls import ControlCodeEditor

from AnyQt.QtCore import QItemSelectionModel
from AnyQt.QtWidgets import QFileSystemModel

logger = logging.getLogger(__name__)

class CodeEditor(BaseWidget):

    def __init__(self, task):
        BaseWidget.__init__(self, task.name if task else '')
        self.set_margin(5)
        self.task = task

        root_path     = os.path.abspath(task.path)
        syspath_model = QFileSystemModel(self)
        syspath_model.setRootPath(root_path)
        syspath_model.setNameFilters(['*.py'])
        syspath_model.setNameFilterDisables(False)
        
        self._browser = ControlTreeView('Files browser', default=syspath_model )
        self._code    = ControlCodeEditor(
            changed_event=self.__code_changed_evt,
            discart_event=self.__code_discart_evt
        )

        self.formset  = [vsplitter('_browser','||','_code')]

        root_index = syspath_model.index(root_path)
        self._browser.setRootIndex(root_index)        
        for i in range(1, 4): self._browser.hideColumn(i)

        self._browser.item_selection_changed_event = self.__item_selection_changed_evt

        task_filepath = syspath_model.index(task.filepath)
        self._browser.setCurrentIndex(task_filepath)

        
        self._browser.add_popup_menu_option('New module', self.__create_module_evt)
        self._browser.add_popup_menu_option('New module folder', self.__create_submodule_evt)
        self._browser.add_popup_menu_option('-')
        self._browser.add_popup_menu_option('Rename', self.__rename_evt)
        self._browser.add_popup_menu_option('Delete', self.__delete_evt)


    def __load_file_content(self, filepath):
        
        try:
            with open(filepath, "r") as file: 
                self._code.value   = file.read()
                self._code.enabled = True
        except:
            self._code.value = ''
            self._code.enabled = False



    def __create_module_evt(self):
        name = self.input_text('Enter the module name', 'Module name')
        if name:
            items = self._browser.selected_item
            if items is not None:
                folder_path = os.path.join(*items)
                if os.path.isfile(folder_path):
                    path = os.path.join(*items[:-1])
                else:
                    path = folder_path
            else:
                path = self.task.path

            new_filename = os.path.join(path, name+'.py')
            if not os.path.isfile(new_filename):
                with open(new_filename, "w") as file: 
                    pass

    def __create_submodule_evt(self):
        name = self.input_text('Enter the module folder name', 'Module folder name')
        if name:
            items = self._browser.selected_item
            if items is not None:
                folder_path = os.path.join(*items)
                if os.path.isfile(folder_path):
                    path = os.path.join(*items[:-1])
                else:
                    path = folder_path
            else:
                path = self.task.path

            try:
                new_folder   = os.path.join(path, name)
                os.makedirs(new_folder)
                new_filename = os.path.join(new_folder, '__init__.py')
                with open(new_filename, "w") as file: 
                    pass
            except:
                pass

    def __rename_evt(self):
        items    = self._browser.selected_item
        fullpath = os.path.join(*items)
        
        if os.path.isfile(fullpath):
            name, extension = os.path.splitext(items[-1])
        else:
            name = items[-1]

        name = self.input_text('Enter the new name', 'New name', name)
        if name:
            if os.path.isfile(fullpath):
                new_path = items[:-1] + [name+extension]
            else:
                new_path = items[:-1] + [name]
            os.rename(fullpath, os.path.join(*new_path) )



    def __delete_evt(self):
        items    = self._browser.selected_item
        fullpath = os.path.join(*items)
        ok = self.question('Please confirm the module [{0}] is to be deleted?'.format(items[-1]))
        if ok:
            if os.path.isfile(fullpath):
                os.remove(fullpath)
            else:
                shutil.rmtree(fullpath)

    def __item_selection_changed_evt(self, selected, deselected):

        if self._code.is_modified:
            self._browser.selectionModel().reset()
            self.info(
                'Please save or discart your modifications first.', 
                'There are still uncommitted modifications'
            )
        else:
            item = self._browser.selected_item
            if item is not None:
                filepath = os.path.join(*item)        
                self.__load_file_content(filepath)

        
    def __code_changed_evt(self):
        items = self._browser.selected_item
        if not items: return
        filepath = os.path.join(*items)

        if filepath is None:
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
        with open(filepath, "w") as file: file.write( self._code.value )

        return True

    def __code_discart_evt(self):
        item = self._browser.selected_item
        if item is not None:
            filepath = os.path.join(*item)        
            self.__load_file_content(filepath)

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
