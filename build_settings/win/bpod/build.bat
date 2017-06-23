@echo off
SETLOCAL enableextensions enabledelayedexpansion

:: 1
:: WINPYTHON SETTINGS

set "WINPYDIR=C:\WinPython\WinPython-64bit-3.5.3.0Qt5-behavior\python-3.5.3.amd64"
set "WINPYVER=3.5.3.0Qt5"
set "HOME=%WINPYDIR%\..\settings"
set "WINPYARCH=WIN-AMD64"

:: SET PATH FOR PYTHON
SET "PYTHON_PATH=%WINPYDIR%\Lib\site-packages\PyQt5;%WINPYDIR%\Lib\site-packages\PyQt4;%WINPYDIR%\;%WINPYDIR%\DLLs;%WINPYDIR%\Scripts;%WINPYDIR%\..\tools;"

:: SAVE CURRENT PATH AND OVERRIDE FOR PYTHON
SET "ORIGINAL_PATH=%PATH%"
SET "PATH=%PYTHON_PATH%"

ECHO Python path activated

:: keep nbextensions in Winpython directory, rather then %APPDATA% default
SET "JUPYTER_DATA_DIR=%HOME%"

:: force default pyqt5 kit
SET "QT_API=pyqt5"

:: http://stackoverflow.com/questions/38674400/missing-dll-files-when-using-pyinstaller
SET "QT5_DLL_PATH=C:\WinPython\WinPython-64bit-3.5.3.0Qt5\python-3.5.3.amd64\Lib\site-packages\PyQt5\Qt\bin"

:: 2
:: PYINSTALLER SETTINGS

SET "PROJECTNAME=PyBpodGUI"
SET "BUILDSETTINGSDIR=%WORKSPACE%\build_settings\win\bpod"
SET "MAINSCRIPT=%WORKSPACE%\pybpodgui_plugin\__main__.py"
SET "BUILDOUTDIR=%WORKSPACE%\build"
SET "DISTOUTDIR=%WORKSPACE%\dist"
SET "ICONNAME=cf_icon_128x128.ico"

ECHO Removing old build dir...
@RD /S /Q %BUILDOUTDIR%

ECHO Removing old dist dir...
@RD /S /Q %DISTOUTDIR%

:: install pip dependencies

IF "%BUILD_DEPENDENCIES%"=="true" (

   ECHO Installing dependencies with pip...

   pip install pyinstaller --upgrade
   pip install pyserial --upgrade
   pip install Send2Trash --upgrade
   pip install sip --upgrade
   pip install pyqt5 --upgrade
   pip install numpy --upgrade
   pip install qscintilla --upgrade
   pip install python-dateutil --upgrade
   pip install matplotlib --upgrade

   pip install https://github.com/UmSenhorQualquer/pysettings/archive/"%PYSETTINGS_GIT_BRANCH%".zip --upgrade
   pip install https://github.com/UmSenhorQualquer/pyforms/archive/"%PYFORMS_GIT_BRANCH%".zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/logging-bootstrap/get/"%LOGGING_BOOTSTRAP_GIT_BRANCH%".zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pybranch/get/"%PYBRANCH_GIT_BRANCH%".zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pyforms_generic_editor/get/"%PGE_GIT_BRANCH%".zip --upgrade

   pip install https://bitbucket.org/fchampalimaud/pybpod-api/get/"%PYBPODAPI_GIT_BRANCH%".zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pybpod-gui-plugin-timeline/get/"%PYBPODGUIPLUGIN_TIMELINE_GIT_BRANCH%".zip --upgrade
   pip install https://bitbucket.org/fchampalimaud/pybpod-gui-plugin-session-history/get/"%PYBPODGUIPLUGIN_SESSION_HISTORY_GIT_BRANCH%".zip --upgrade
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

python "%WORKSPACE%\build_settings\get_package_version.py" pybpodgui_plugin > software_version.txt
"C:\Program Files\Git\bin\git.exe" rev-list  --all --count > git_version.txt
SET /p DEV_VERSION= < software_version.txt
SET /p GIT_VERSION= < git_version.txt
SET DEV_VERSION=%DEV_VERSION%_git%GIT_VERSION%_build%BUILD_NUMBER%
DEL software_version.txt
DEL git_version.txt

:: python setup.py sdist

:: RUN PYINSTALLER

ECHO Running pyinstaller now...

IF /I "%GIT_BRANCH%" EQU "master" (
   set "DISTJOBDIR=%PROJECTNAME%_v%DEV_VERSION%"
   pyinstaller --additional-hooks-dir "%BUILDSETTINGSDIR%\hooks" --name "!DISTJOBDIR!" --exclude-module IPython --exclude-module sqlalchemy --exclude-module PIL %EXCLUDE_MATPLOTLIB% %EXCLUDE_PYQT_WEB% --exclude-module requests --exclude-module xml.dom.domreg --exclude-module visvis --exclude-module OpenGL --icon "%BUILDSETTINGSDIR%\%ICONNAME%" --onedir  --noconsole --paths "%QT5_DLL_PATH%" "%MAINSCRIPT%"
) ELSE (
   set "DISTJOBDIR=%PROJECTNAME%_v%DEV_VERSION%.DEV"
   pyinstaller --additional-hooks-dir "%BUILDSETTINGSDIR%\hooks" --name "!DISTJOBDIR!" --exclude-module IPython --exclude-module sqlalchemy --exclude-module PIL %EXCLUDE_MATPLOTLIB% %EXCLUDE_PYQT_WEB% --exclude-module requests --exclude-module xml.dom.domreg --exclude-module visvis --exclude-module OpenGL --icon "%BUILDSETTINGSDIR%\%ICONNAME%" --debug --onedir --paths "%QT5_DLL_PATH%" "%MAINSCRIPT%"
)

:: SAVE VARS ON FILE

echo DEV_VERSION=%DEV_VERSION% > env.propsfile
echo GIT_VERSION=%GIT_VERSION%  >> env.propsfile
echo DISTOUTDIR=%DISTOUTDIR:\=\\%  >> env.propsfile
echo PROJECTNAME=%PROJECTNAME% >> env.propsfile
echo DISTJOBDIR=!DISTJOBDIR! >> env.propsfile

SET "PATH=%ORIGINAL_PATH%"
ECHO System path activated

ECHO Copying user settings
copy /Y "%WORKSPACE%\build_settings\win\bpod\simple_user_settings.py"  "%WORKSPACE%\dist\%DISTJOBDIR%\user_settings.py"

:: ZIP DIST FOLDER
ECHO Zipping folder now...
jar -cMf "%DISTOUTDIR%\%DISTJOBDIR%.zip" -C "%DISTOUTDIR%\%DISTJOBDIR%" .

:: UPLOAD DIST FOLDER FOR BITBUCKET
IF "%UPLOAD_2_BITBUCKET%"=="true" (
   ECHO Uploading to bitbucket now...
   curl --progress-bar --netrc-file c:\curl_auth\bitbucket_auth.txt -X POST https://api.bitbucket.org/2.0/repositories/fchampalimaud/pycontrol-gui/downloads -F files=@"%DISTOUTDIR%\%DISTJOBDIR%.zip" > curl_output.log
   type curl_output.log
)


