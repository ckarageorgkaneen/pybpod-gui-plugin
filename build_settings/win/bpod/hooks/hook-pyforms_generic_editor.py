from PyInstaller.utils.hooks import collect_submodules, collect_data_files

from pyforms import conf

hiddenimports = [
 'pyforms_generic_editor.settings',
 'pyforms_generic_editor.resources',
 'pybpodgui_plugin.settings',
 'pybpodgui_plugin.resources',
 'pybpodgui_plugin_timeline.settings',
 'pybpodgui_plugin_timeline.resources',
 'pybpodgui_plugin_session_history.settings',
 'pybpodgui_plugin_session_history.resources',] \
 + collect_submodules('pyforms_generic_editor.models') \
 + collect_submodules('pybpodgui_plugin.models') \
 + collect_submodules('pybpodgui_plugin.com') \
 + collect_submodules('pybpodgui_api') \
 + collect_submodules('pybpodgui_plugin_timeline.models') \
 + collect_submodules('pybpodgui_plugin_session_history.models')

datas = [('pybpodgui_plugin\\resources', 'pybpodgui_plugin\\resources'),] \
        + collect_data_files('pyforms_generic_editor') \
        + collect_data_files('pybpodgui_plugin') \
        + collect_data_files('pybpodgui_plugin_timeline') \
        + collect_data_files('pybpodgui_plugin_session_history')

