# !/usr/bin/python3
# -*- coding: utf-8 -*-

import os


def path(filename):
	return os.path.join(os.path.dirname(__file__), 'icons', filename)


ADD_SMALL_ICON = path('add.png')
NEW_SMALL_ICON = path('new.png')
OPEN_SMALL_ICON = path('open.png')
SAVE_SMALL_ICON = path('save.png')
EXIT_SMALL_ICON = path('exit.png')
CLOSE_SMALL_ICON = path('close.png')

PLAY_SMALL_ICON = path('play.png')
BUSY_SMALL_ICON = path('busy.png')
PROJECT_SMALL_ICON = path('project.png')
REMOVE_SMALL_ICON = path('remove.png')

# BOARD_SMALL_ICON = path('board.png')
BOARDS_SMALL_ICON = path('boxes.png')
BOX_SMALL_ICON = path('box.png')

SUBJECT_SMALL_ICON = path('subject.png')
UPLOAD_SMALL_ICON = path('upload.png')

EXPERIMENT_SMALL_ICON = path('experiment.png')
EXPERIMENTS_SMALL_ICON = path('experiments.png')

TASK_SMALL_ICON = path('task.png')
TASKS_SMALL_ICON = path('tasks.png')
