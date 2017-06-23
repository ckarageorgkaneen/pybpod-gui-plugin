from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hiddenimports = ["pyforms_generic_editor.settings", "pyforms_generic_editor.resources"] + collect_submodules('pyforms_generic_editor.models')

datas = collect_data_files('pyforms_generic_editor')

