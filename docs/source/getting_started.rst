Getting started
===============

Architecture
------------
**pybpodgui_plugin** is a *Graphical User Interface (GUI)* for the `pyControl framework <https://pycontrol.readthedocs.io>`_. It is written in Python3 with PyQT4 and it is composed of several independent packages in order to achieve better flexibility and maintenance. You can find detailed documentation for all these projects below.

External libraries
^^^^^^^^^^^^^^^^^^

=========================================================================================================================================================================== =================================================================
Library name                                                                                                                                                                Description
=========================================================================================================================================================================== =================================================================
pysettings `readthedocs <https://pysettings.readthedocs.io/en/latest/>`_ `github <https://github.com/UmSenhorQualquer/pysettings>`_                                         Python library to provide settings files for modular applications
pyForms `readthedocs <https://pyforms.readthedocs.io/en/latest/>`_ `github <https://github.com/UmSenhorQualquer/pyforms>`_                                                  Python layer of Windows forms, based on PyQT and OpenGL
pyforms-generic-editor `readthedocs <http://pyforms-generic-editor.readthedocs.io/en/latest/>`_ `bitbucket <https://bitbucket.org/fchampalimaud/pyforms-generic-editor>`_   Easy way to bootstrap projects that make use of pyForms
pyserial `readthedocs <https://pyserial.readthedocs.io/en/latest/)>`_ `github <https://github.com/pyserial/pyserial>`_                                                       Python serial port access library
Send2Trash `github <https://github.com/hsoft/send2trash>`_                                                                                                                  Python library to natively send files to Trash (or Recycle bin) on all platforms.
=========================================================================================================================================================================== =================================================================


pyControl Framework and Command Line Interface (CLI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=========================================================================================================================================================================== ================= ===============================================================
Library name                                                                                                                                                                Description       mercurial link
=========================================================================================================================================================================== ================= ===============================================================
pyControl framework `wiki <https://bitbucket.org/takam/pycontrol/wiki/Home>`_ `bitbucket <https://bitbucket.org/takam/pycontrol/wiki/Home>`_                                CLI and framework https://bitbucket.org/takam/pycontrol
=========================================================================================================================================================================== ================= ===============================================================

pyControl Graphical User Interface (GUI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

============================================================================================================================================================ =================================== =============================================================
Library name                                                                                                                                                 Description                         Git link
============================================================================================================================================================ =================================== =============================================================
pycontrol-gui `readthedocs <https://pycontrol-gui.readthedocs.io/>`_ `bitbucket <https://bitbucket.org/fchampalimaud/pycontrol-gui>`_                        GUI library                         https://bitbucket.org/fchampalimaud/pycontrol-gui.git
pycontrol-api `readthedocs <https://pycontrol-api.readthedocs.io>`_ `bitbucket <https://bitbucket.org/fchampalimaud/pycontrol-api>`_                         Model description API               https://bitbucket.org/fchampalimaud/pycontrol-api.git
pyboard-communication `readthedocs <https://pyboard-communication.readthedocs.io>`_ `bitbucket <https://bitbucket.org/fchampalimaud/pyboard-communication>`_ pyBoard communication for pyControl https://bitbucket.org/fchampalimaud/pyboard-communication.git
============================================================================================================================================================ =================================== =============================================================


Step-by-step installation for running GUI
-----------------------------------------

Install python3 and PyQt (with QScintilla2) environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download GUI libraries sources from git
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To develop for pyControl GUI, you will need to download the sources of the following libraries: ::

    # folder pyboard-communication is created
    git clone https://bitbucket.org/fchampalimaud/pyboard-communication.git

    # folder pycontrol-api is created
    git clone https://bitbucket.org/fchampalimaud/pycontrol-api.git

    # folder pycontrol-gui is created
    git clone https://bitbucket.org/fchampalimaud/pycontrol-gui.git


Install required libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^
On the command line, navigate inside the pycontrol-gui folder. You will find a "requirements.txt" file.
To install requirements, run pip as this: ::

    cd pycontrol-gui
    pip3 install -r requirements.txt --upgrade

This file assumes that "pyboard-communication" and "pycontrol-api" sources are on the parent folder. You should expect the following directory structure:::

    | pyboard-communication
       | pyboard-communication
       | ...
    | pycontrol-api
       | pycontrolapi
       | ...
    | pycontrol-gui
       | pybpodgui_plugin
       | requirements.txt
       | ...

Download and configure pycontrol framework
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Download pycontrol-framework source code from [here](https://bitbucket.org/takam/pycontrol/get/37fd9d1d22fd.zip) and unzip it (you should see a pyControl folder).
2. Inside the pycontrol-gui folder, locate the file "user_settings.py.template". Make a copy and change the name for "user_settings.py".
3. Open the file "user_settings.py".
4. Change the variable value **PYCONTROLAPI_PYCONTROL_PATH** to point to the folder "pyControl" inside the pycontrol-framework project just downloaded
5. Change the variable value **PYCONTROLAPI_DEVICES_PATH** to point to the folder "devices" inside the pycontrol-framework project just downloaded

Folder structure should look like these: ::

    | pycontrol-gui
       | pybpodgui_plugin
       | requirements.txt
       | user_settings.py.template
       | user_settings.py
       | ...

    | pyControl
       | devices
       | examples
       | host
       | license
       | pyControl
       | ...


Run project
---------------
On the command line, navigate inside the pycontrol-gui folder.
Run the following command: ::

    python3 -m pybpodgui_plugin
