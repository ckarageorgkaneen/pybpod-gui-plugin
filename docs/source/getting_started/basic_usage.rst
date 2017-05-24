.. _basic_usage-label:

***********
Basic usage
***********


========
Projects
========

When you open the Bpod GUI for the first time, you can create a new project or load a previous project from your filesystem.

.. image:: /_images/basic_usage/file_menu.png
    :scale: 100 %

With PyBpod GUI you can easily organize your work. Projects allow you to aggregate several experiments in one place. Moreover, you can have several projects open at the same time to compare data.
Each project has a set of experiments, boxes and protocols.

.. image:: /_images/basic_usage/projects.png
    :scale: 100 %

.. image:: /_images/basic_usage/project_detail_window.png
    :scale: 100 %


=====
Boxes
=====

PyBpod GUI supports multiple Bpod boxes to be run in parallel. Just add a new box, select serial port, run your experiment and open the console window.

.. image:: /_images/basic_usage/boxes.png
    :scale: 100 %

.. image:: /_images/basic_usage/box_detail_window.png
    :scale: 100 %

The console window allows you to see real time output from the Bpod.

.. image:: /_images/basic_usage/box_window_console.png
    :scale: 100 %


=========
Protocols
=========

Protocols allow you to define how the state matrix works. They are fully written in Python but follow a similar syntax from the Bpod Matlab equivalents.

PyBpod GUI ships with a code editor with syntax highlight and you don't have to hardcode the serial port or other settings.
Let the GUI do the job for you and focus on your experiments!

.. image:: /_images/basic_usage/writing_protocols.png
    :scale: 100 %


========================
Experiments and subjects
========================

Experiments hold all your experiment important data. Each experiment has a list of subjects. From each subject you can run the corresponding Bpod box.
The workflow goes like this:

    1. Inside the project, add an experiment
    2. Assign a protocol to the experiment
    3. Inside the experiment, add several subjects
    4. Assign a Bpod box to each of the subjects
    5. Run the experiment for one subject or run them all at the same time!

.. image:: /_images/basic_usage/experiment_detail_window.png
    :scale: 100 %

.. image:: /_images/basic_usage/subject_detail_window.png
    :scale: 100 %

.. warning::
    Currently, all subjects inside the same experiment are assigned the same protocol. We are working to support a specific protocol per subject.


========
Sessions
========

Each time you run a Bpod protocol on a subject a new session is created. The GUI collects output from the PyBpod API and processes these events on a list (which we call session history).
Besides being on memory, this history is automatically saved on a text file, so you never loose Bpod data.

If you navigate to your project on the filesystem, and locate the desired subject, you should find several files:

    * CSV and JSON are default outputs from the pybpod-api (for example, you can open CSV on excel and quickly produce some plots)
    * Plain text file is the output from the GUI

.. image:: /_images/basic_usage/session_data_filesystem.png
    :scale: 100 %

You can also develop plugins that enhance session data visualization and access them by right-clicking the desired session.

.. image:: /_images/basic_usage/session_details_plugins.png
    :scale: 100 %


=================
GUI User settings
=================

You can edit user settings directly from the GUI. User settings enable you to tweak the GUI the way you like it.
Example of parameters you may change are:

    * Loaded plugins
    * Default project path
    * Refresh time for console window
    * And much more...

.. image:: /_images/basic_usage/user_settings.png
    :scale: 100 %