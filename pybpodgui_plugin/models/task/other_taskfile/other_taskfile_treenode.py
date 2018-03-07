# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from pyforms import conf
from AnyQt.QtWidgets import QApplication
from AnyQt.QtGui import QIcon
from AnyQt import QtCore

from pybpodgui_plugin.models.task.other_taskfile.other_taskfile_window import OtherTaskFileWindow


logger = logging.getLogger(__name__)


class OtherTaskFileTreeNode(OtherTaskFileWindow):
    """
    Extends task window to show up in the project tree section.
    Define here actions related to the task tree node.

    **Properties**

        name
            Handles task tree node name.

        tree
            Returns project tree.

    **Methods**

    """

    def __init__(self, task):
        super(OtherTaskFileTreeNode, self).__init__(task)

        self.create_treenode(self.tree)

    

    def create_treenode(self, tree):
        """
        Creates node for this task under the parent "Tasks" node.

        This methods is called when the task is first created.

        The following actions get assigned to node:
            * *Remove*: :meth:`TaskTreeNode.remove`.

        Sets key events:
            * :meth:`TaskTreeNode.node_key_pressed_event`


        :param tree: the project tree
        :type tree: pyforms.controls.ControlTree
        :return: new created node
        :return type: QtGui.QTreeWidgetItem
        """
        self.node = tree.create_child(self.name, self.task.node, icon=QIcon(conf.TASK_SMALL_ICON))
        #self.node.key_pressed_event = self.node_key_pressed_event
        #self.node.double_clicked_event = self.node_double_clicked_event
        self.node.window = self
        self.node.setExpanded(True)

        #tree.add_popup_menu_option('Remove', self.remove, item=self.node, icon=QIcon(conf.REMOVE_SMALL_ICON))
        return self.node

    def node_double_clicked_event(self):
        """
        Fires event :py:meth:`pybpodgui_plugin.models.task.task_dockwindow.TaskDockWindow.edit_btn_evt` when tree node is double clicked.
        """
        pass

    def remove(self):
        """

        Remove task from project and remove node from tree.

        .. seealso::
            * Task removal (dock window): :py:meth:`pybpodgui_plugin.models.task.task_dockwindow.TaskDockWindow.remove`.
            * Task removal (API): :meth:`pybpodgui_api.models.board.board_base.TaskBase.remove`.
            * Remove task from project: :meth:`pybpodgui_api.models.project.project_base.ProjectBase.__sub__`.

        """
        self.task -= self
        self.task.otherfiles_node.removeChild(self.node)

    @property
    def tree(self):
        return self.task.tree


    @property
    def name(self): return OtherTaskFileWindow.name.fget(self)

    @name.setter
    def name(self, value):
        OtherTaskFileWindow.name.fset(self, value)
        if hasattr(self, 'node'): self.node.setText(0, value)
        
