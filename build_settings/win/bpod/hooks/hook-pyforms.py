from PyInstaller.utils.hooks import collect_data_files

hiddenimports = ["pyforms.settings", "pyforms.gui.settings", "pyforms.Controls", "PyQt5.uic.plugins"]

datas = collect_data_files('pyforms')
