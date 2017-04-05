@echo off
SETLOCAL enableextensions enabledelayedexpansion

:: 1
:: WINPYTHON SETTINGS

set "WINPYDIR=C:\WinPython\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64"
set "WINPYVER=3.6.1.0Qt5"
set "HOME=%WINPYDIR%\..\settings"
set "WINPYARCH=WIN-AMD64"

:: SET PATH FOR PYTHON
SET "PYTHON_PATH=%WINPYDIR%\Lib\site-packages\PyQt5;%WINPYDIR%\Lib\site-packages\PyQt4;%WINPYDIR%\;%WINPYDIR%\DLLs;%WINPYDIR%\Scripts;%WINPYDIR%\..\tools;"

:: SAVE CURRENT PATH AND OVERRIDE FOR PYTHON
SET "ORIGINAL_PATH=%PATH%"
SET "PATH=%PYTHON_PATH%"

:: keep nbextensions in Winpython directory, rather then %APPDATA% default
set "JUPYTER_DATA_DIR=%HOME%"

:: force default pyqt5 kit
set "QT_API=pyqt5"

:: 2
:: PYINSTALLER SETTINGS

set PROJECTNAME="pybpod-gui-plugin"

python --version

pip uninstall -y %PROJECTNAME%
pip install .
pip show %PROJECTNAME%

python setup.py sdist --formats=zip