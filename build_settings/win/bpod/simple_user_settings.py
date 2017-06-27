# !/usr/bin/python3
# -*- coding: utf-8 -*-

SETTINGS_PRIORITY = 0

import logging

############ LOGGERS SETTINGS ############

# GUI logger
#BPODGUI_LOG_HANDLER_FILE_LEVEL = logging.DEBUG # default is logging.WARNING
#BPODGUI_LOG_HANDLER_CONSOLE_LEVEL = logging.DEBUG # default is logging.WARNING

# Other libraries logger
#APP_LOG_HANDLER_CONSOLE_LEVEL = logging.DEBUG # default is logging.WARNING
#APP_LOG_HANDLER_FILE_LEVEL = logging.DEBUG # default is logging.WARNING

############ PYFORMS GENERIC EDITOR SETTINGS ############

GENERIC_EDITOR_WINDOW_GEOMETRY = 100, 100, 1200, 800

GENERIC_EDITOR_TITLE = "PyBpod GUI"

PYFORMS_MAINWINDOW_MARGIN = 0
PYFORMS_STYLESHEET = ''
PYFORMS_STYLESHEET_DARWIN = ''
PYFORMS_SILENT_PLUGINS_FINDER = True

PYFORMS_MATPLOTLIB_ENABLED = True
PYFORMS_WEB_ENABLED = False
PYFORMS_GL_ENABLED = False
PYFORMS_VISVIS_ENABLED = False

############ INSTALLED PLUGINS ############

GENERIC_EDITOR_PLUGINS_PATH = None
GENERIC_EDITOR_PLUGINS_LIST = [
	'pybpodgui_plugin',
	'pybpodgui_plugin_timeline',
	'pybpodgui_plugin_session_history',
]

############ BPODLGUI PLUGIN SETTINGS ############

# YOU MUST USE DOUBLE SLASH FOR PATHS
#DEFAULT_PROJECT_PATH = 'C:\\Users\\YOUR_NAME\\pybpod\\simple_project'


#BOARD_LOG_WINDOW_REFRESH_RATE = 0.5 # timer to update content on console (seconds), default is 1s
#SESSIONLOG_PLUGIN_REFRESH_RATE = 0.5 # timer to update plugin content (seconds), default is 1s

#PYBRANCH_THREAD_IDLE_REFRESH_TIME  = 5 # timer for thread look for events (seconds), default is 1s
#PYBRANCH_PROCESS_TIME_2_LIVE = 5 # wait before killing process (seconds), default is 5s
