# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import logging
import shutil

from pyforms import conf

from AnyQt.QtWidgets import QFileDialog
from AnyQt.QtGui import QIcon

from pybpodgui_plugin.models.project.project_window import ProjectWindow
from pybpodgui_plugin.models.experiment import Experiment
from pybpodgui_plugin.models.board import Board
from pybpodgui_plugin.models.task import Task
from pybpodgui_plugin.models.subject import Subject

logger = logging.getLogger(__name__)


class ProjectTreeNode(ProjectWindow):
    def __init__(self, projects):
        ProjectWindow.__init__(self)

        self.projects = projects
        self.projects += self

        self.create_treenode(self.tree)

    def create_treenode(self, tree):
        self.node = tree.create_child(self.name, icon=QIcon(conf.PROJECT_SMALL_ICON))
        self.node.window = self
        self.node.setExpanded(True)

        tree.add_popup_menu_option('Save', self.save, item=self.node, icon=QIcon(conf.SAVE_SMALL_ICON))
        tree.add_popup_menu_option('Save as', self.save_as, item=self.node, icon=QIcon(conf.SAVE_SMALL_ICON))
        tree.add_popup_menu_option('Close', self.close, item=self.node, icon=QIcon(conf.CLOSE_SMALL_ICON))

        self.experiments_node = tree.create_child('Experiments', parent=self.node,
                                                  icon=QIcon(conf.EXPERIMENTS_SMALL_ICON))
        self.experiments_node.window = self
        self.experiments_node.setExpanded(True)

        tree.add_popup_menu_option('Add experiment', self._add_experiment, item=self.experiments_node,
                                   icon=QIcon(conf.ADD_SMALL_ICON))

        self.subjects_node = tree.create_child('Subjects', parent=self.node, icon=QIcon(conf.SUBJECTS_SMALL_ICON))
        tree.add_popup_menu_option('Add subject', self.create_subject, item=self.subjects_node,
                                   icon=QIcon(conf.ADD_SMALL_ICON))
        self.subjects_node.window = self
        #self.subjects_node.setExpanded(True)


        self.boards_node = tree.create_child('Bpod boards', parent=self.node, icon=QIcon(conf.BOARDS_SMALL_ICON))
        self.boards_node.window = self
        #self.boards_node.setExpanded(True)

        tree.add_popup_menu_option('Add Bpod boards', self._add_board, item=self.boards_node,
                                   icon=QIcon(conf.ADD_SMALL_ICON))

        self.tasks_node = tree.create_child('Protocols', parent=self.node, icon=QIcon(conf.TASKS_SMALL_ICON))
        tree.add_popup_menu_option('Add protocol', self._add_task, item=self.tasks_node,
                                   icon=QIcon(conf.ADD_SMALL_ICON))
        self.tasks_node.window = self
        #self.tasks_node.setExpanded(True)

        
        tree.add_popup_menu_option('Import protocol', self.import_task, item=self.tasks_node,
                                   icon=QIcon(conf.OPEN_SMALL_ICON))

        return self.node

    def _add_experiment(self):
        entity = self.create_experiment()
        entity.focus_name()

    def _add_board(self):
        entity = self.create_board()
        entity.focus_name()

    def create_experiment(self):
        experiment = Experiment(self)
        self.tree.setCurrentItem(experiment.node)
        return experiment

    def create_board(self):
        board = Board(self)
        self.tree.setCurrentItem(board.node)
        return board

    def create_task(self):
        task = Task(self)
        self.tree.setCurrentItem(task.node)
        return task

    def create_subject(self):
        subject = Subject(self)
        self.tree.setCurrentItem(subject.node)
        return subject

    def close(self, silent=False):
        confirmation = True

        if not silent:
            reply = self.question('Are sure you want to close the project?','Close project')

            if reply:
                confirmation = True
            else:
                confirmation = False

        if confirmation:
            super(ProjectTreeNode, self).close(silent)
            tree = self.tree
            tree -= self.node

    def save_as(self):
        folder = QFileDialog.getExistingDirectory(self,
                                                  "Select a directory to save the project: {0}".format(self.name))
        if folder:
            folder = os.path.join(folder, self.name)
            self.save(str(folder))

    def load(self, project_path):
        super(ProjectTreeNode, self).load(project_path)

        self.tree.setCurrentItem(self.node)

    def _add_task(self):
        if self.path is None or len(self.path) == 0 or not self.is_saved():
            reply = self.warning('To create a new protocol you need to save the project first.','Project not saved yet')
        else:
            entity = self.create_task()
            entity.focus_name()



    def import_task(self, filepath=None):
        """
        Import task file to project
        
        Qt5 change:
        https://www.reddit.com/r/learnpython/comments/2xhagb/pyqt5_trouble_with_openinggetting_the_name_of_the/
        
        :param filepath: 
        :return: 
        """
        if self.path is None or len(self.path) == 0 or not self.is_saved():
            reply = self.warning('To import a protocol you need to save the project first.','Project not saved yet')
        else:
            if not filepath:
                filepath, _ = QFileDialog.getOpenFileName(self, 'OpenFile')

            if filepath:
                task = self.create_task()
                filename, file_extension = os.path.splitext(os.path.basename(filepath))
                task.name = filename
                if not os.path.exists(task.path): os.makedirs(task.path)
                task.filepath = os.path.join(task.path, task.name+'.py')

                shutil.copy(filepath, os.path.join(task.path, task.name+'.py'))

    @property
    def name(self):
        if hasattr(self, 'node'):
            return str(self.node.text(0))
        else:
            name = ProjectWindow.name.fget(self)
            if len(name) == 0:
                name = "Untitled project {0}".format(len(self.projects.projects))
                ProjectWindow.name.fset(self, name)
                return name
            else:
                return ProjectWindow.name.fget(self)

    @name.setter
    def name(self, value):
        ProjectWindow.name.fset(self, value)
        if hasattr(self, 'node'): self.node.setText(0, value)

    @property
    def tree(self):
        return self.projects.tree
