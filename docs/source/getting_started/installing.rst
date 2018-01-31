.. pybpodapi documentation master file, created by
   sphinx-quickstart on Wed Jan 18 09:35:10 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _installing-label:

**********
Installing
**********


1. Download & install `Anaconda <https://www.anaconda.com/download/>`_ or `Miniconda <https://conda.io/miniconda.html>`_.
2. Download the environment configuration file for your Operating System ( `Windows 10 <https://bitbucket.org/fchampalimaud/pybpod/raw/e6c1c8da96c240ae638309359a97b28a2d36ca55/environment-windows-10.yml>`_ ) and create a virtual environment with it by executing the following commands in the "Anaconda Prompt".

.. code::

  conda env create -f environment-windows-10.yml

.. note::

  * On windows if you install Anaconda/Miniconda for all the users, you should make sure you run the "Anaconda Prompt" as administrator.  
  * To avoid issues, make sure you install Anaconda/Miniconda only for your user.


3. Activate the environment you just created.

.. code::

  activate pybpod-environment

4. Clone the PyBpod repository.

.. code::

  git clone https://UmSenhorQualquer@bitbucket.org/fchampalimaud/pybpod.git

5. Access the created repository folder.

.. code::

  cd pybpod


6. Run the "install.py" script to install all necessary dependencies.

.. code::

  python install.py

7. Run the PyBpod application.

.. code::

  python -m pybpodgui_plugin


********************
Execute PyBpod GUI
********************

1. Open "Anaconda Prompt" and activate the "pybpod-environment".

.. code::

  activate pybpod-environment

2. Run the application.

.. code::

  python -m pybpodgui_plugin


*******************
Update PyBpod GUI
*******************

1. Open the "Anaconda Prompt" and activate the "pybpod-environment".

.. code::

  activate pybpod-environment

2. Execute the script "update.py".

.. code::

  python update.py
