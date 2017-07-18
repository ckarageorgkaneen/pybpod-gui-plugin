from PyInstaller.utils.hooks import collect_data_files, is_module_satisfies
from PyInstaller.compat import is_py2

if is_module_satisfies('botocore >= 1.4.36'):
    if is_py2:
        hiddenimports = ['HTMLParser']
    else:
        hiddenimports = ['html.parser']

datas = collect_data_files('botocore')