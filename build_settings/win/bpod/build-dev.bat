@echo off
SETLOCAL enableextensions enabledelayedexpansion

SET "QT5_DLL_PATH=C:\WinPython\WinPython-64bit-3.5.3.0Qt5\python-3.5.3.amd64\Lib\site-packages\PyQt5\Qt\bin"

:: 2
:: PYINSTALLER SETTINGS

SET "PROJECTNAME=PyBpodGUI"
SET "BUILDSETTINGSDIR=build_settings\win\bpod"
SET "MAINSCRIPT=pyforms_generic_editor\__main__.py"
SET "BUILDOUTDIR=build"
SET "DISTOUTDIR=dist"
SET "ICONNAME=cf_icon_128x128.ico"

ECHO Removing old build dir...
@RD /S /Q %BUILDOUTDIR%

ECHO Removing old dist dir...
@RD /S /Q %DISTOUTDIR%

:: install pip dependencies

SET "BUILD_DEPENDENCIES=false"

IF "%BUILD_DEPENDENCIES%"=="true" (

   ECHO Installing dependencies with pip...

   pip install pyserial
   pip install Send2Trash
   pip install pyqt5
   pip install numpy
   pip install qscintilla
   pip install python-dateutil
   pip install matplotlib

   pip install https://github.com/UmSenhorQualquer/pysettings/archive/master.zip --upgrade
   pip install https://github.com/UmSenhorQualquer/pyforms/archive/v2.0.0.beta.zip --upgrade

   pip install https://bitbucket.org/fchampalimaud/logging-bootstrap/get/master.zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pybranch/get/master.zip --upgrade

   pip install https://bitbucket.org/fchampalimaud/pybpod-api/get/master.zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pybpod-gui-plugin/get/development.zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pybpod-gui-plugin-timeline/get/master.zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pybpod-gui-plugin-session-history/get/master.zip --upgrade
)

IF "%WITH_MATPLOTLIB%"=="true" (
    ECHO Matplot lib activated
    SET "EXCLUDE_MATPLOTLIB= "
) ELSE (
    ECHO Matplot lib disabled
    SET "EXCLUDE_MATPLOTLIB=--exclude-module matplotlib.backends --exclude-module matplotlib"
)

IF "%WITH_PYQT_WEB%"=="true" (
    ECHO PyQt5 Web lib activated
    SET "EXCLUDE_PYQT_WEB= "
) ELSE (
    ECHO PyQt Web lib disabled
    SET "EXCLUDE_PYQT_WEB=--exclude-module PyQt5.QtWebEngineWidgets"
)

:: python setup.py sdist

:: RUN PYINSTALLER

ECHO Running pyinstaller now...
SET "DISTJOBDIR=pybpod"
pyinstaller --additional-hooks-dir "%BUILDSETTINGSDIR%\hooks" --name "!DISTJOBDIR!" --exclude-module IPython --exclude-module sqlalchemy --exclude-module PIL %EXCLUDE_MATPLOTLIB% %EXCLUDE_PYQT_WEB% --exclude-module requests --exclude-module xml.dom.domreg --exclude-module visvis --exclude-module OpenGL --exclude-module OpenGL_accelerate --icon "%BUILDSETTINGSDIR%\%ICONNAME%" --debug --onedir --paths "%QT5_DLL_PATH%" "%MAINSCRIPT%"

:: SAVE VARS ON FILE

echo DEV_VERSION=%DEV_VERSION% > env.propsfile
echo GIT_VERSION=%GIT_VERSION%  >> env.propsfile
echo DISTOUTDIR=%DISTOUTDIR:\=\\%  >> env.propsfile
echo PROJECTNAME=%PROJECTNAME% >> env.propsfile
echo DISTJOBDIR=!DISTJOBDIR! >> env.propsfile



ECHO Copying user settings
copy /Y "build_settings\win\bpod\simple_user_settings.py"  "dist\%DISTJOBDIR%\pyforms_generic_editor_user_settings.py"
