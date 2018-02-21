# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pyforms import conf

if conf.USE_MULTIPROCESSING:
	from pybranch.run_handlers.multiprocessing.multiprocess_runner import MultiprocessRunner as PybranchRunHandler
else:
	from pybranch.run_handlers.singleprocessing.singleprocess_runner import SingleprocessRunner as PybranchRunHandler
