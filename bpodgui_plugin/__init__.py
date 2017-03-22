# !/usr/bin/python3
# -*- coding: utf-8 -*-

__version__ = "1.4.0.beta"
__author__ = "Carlos Mao de Ferro"
__credits__ = ["Carlos Mao de Ferro", "Ricardo Ribeiro"]
__license__ = "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>"
__maintainer__ = ["Carlos Mao de Ferro", "Ricardo Ribeiro"]
__email__ = ["cajomferro@gmail.com", "ricardojvr@gmail.com"]
__status__ = "Development"

import logging
import loggingbootstrap

from pysettings import conf;

conf += 'bpodgui_plugin.settings'

conf += 'bpodgui_plugin.resources'

# load the user settings in case the file exists
# try:
# 	import pycontrolgui_plugin_user_settings
#
# 	conf += pycontrolgui_plugin_user_settings
# except Exception as err:
# 	print('Error when importing user_settings!!!')
# 	print(str(err))

### configure loggers

# setup different loggers but output to single file
loggingbootstrap.create_double_logger("bpodgui_plugin", conf.BPODGUI_LOG_HANDLER_CONSOLE_LEVEL,
                                      conf.APP_LOG_FILENAME,
                                      conf.BPODGUI_LOG_HANDLER_FILE_LEVEL)

#loggingbootstrap.create_double_logger("pycontrolapi", conf.PYCONTROLAPI_LOG_HANDLER_CONSOLE_LEVEL,
#                                      conf.APP_LOG_FILENAME,
#                                      conf.PYCONTROLAPI_LOG_HANDLER_FILE_LEVEL)


#loggingbootstrap.create_double_logger("pyboard_communication", conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
#                                      conf.APP_LOG_FILENAME,
#                                      conf.APP_LOG_HANDLER_FILE_LEVEL)

loggingbootstrap.create_double_logger("pybranch", conf.APP_LOG_HANDLER_CONSOLE_LEVEL,
                                      conf.APP_LOG_FILENAME,
                                      conf.APP_LOG_HANDLER_FILE_LEVEL)

if conf.USE_MULTIPROCESSING:
	# https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.freeze_support
	from multiprocessing import freeze_support  # @UnresolvedImport

# try:
# 	import pycontrolapi
# except ImportError as err:
# 	logging.getLogger(__name__).critical(str(err), exc_info=True)
# 	exit("Could not load pycontrol-api! Is it installed?")

if conf.USE_MULTIPROCESSING:
	freeze_support()
