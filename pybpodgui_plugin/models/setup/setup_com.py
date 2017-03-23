# !/usr/bin/python3
# -*- coding: utf-8 -*-

from pybpodgui_plugin.models.setup.setup_dockwindow import SetupDockWindow


class ComSetup(SetupDockWindow):
	"""
	Define board actions that are triggered by setup.

	.. seealso::
		This class heavy relies on the corresponding API module.

		:py:class:`pycontrolapi.model.setup.setup_com.ComSetup`

	**Methods**

	"""

	def stop_task(self):
		"""
		Stop task by calling API.

		Also, update UI by calling :py:meth:`pycontrolgui.models.setup.setup_uibuisy.SetupUIBusy.update_ui`.
		"""
		super(ComSetup, self).stop_task()
		self.update_ui()