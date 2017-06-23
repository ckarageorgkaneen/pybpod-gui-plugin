from PyInstaller.utils.hooks import collect_submodules, collect_data_files

from pysettings import conf

conf.PYFORMS_USE_QT5 = True

hiddenimports = [
 'pybpodgui_plugin.settings',
 'pybpodgui_plugin.resources',
 'pybpodgui_plugin_timeline.settings',
 'pybpodgui_plugin_timeline.resources',
 'pybpodgui_plugin_session_history.settings',
 'pybpodgui_plugin_session_history.resources', ] \
 + collect_submodules('pybpodgui_plugin.models') \
 + collect_submodules('pybpodgui_plugin.com') \
 + collect_submodules('pybpodgui_plugin.api') \
 + collect_submodules('pybpodgui_plugin_timeline.models') \
 + collect_submodules('pybpodgui_plugin_session_history.models')

datas = collect_data_files('pybpodgui_plugin') \
 + collect_data_files('pybpodgui_plugin_timeline') \
 + collect_data_files('pybpodgui_plugin_session_history')
