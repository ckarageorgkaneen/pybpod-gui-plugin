.. _developing_plugins-label:

******************
Developing plugins
******************

What is a PyBpod GUI plugin?
============================

**PyBpod** works as plugin for a generic GUI framework, called **PyformsGenericEditor**. Thus, you will need to download this project source code.

**PyformsGenericEditor** loads plugins specified on a settings file and looks for code on the Python path.

Thus, every time you want to add a new plugin, you have to install it on the Python path, using PIP.

Because **PyformsGenericEditor** is not restricted to **PyBpod**, if you want to develop plugins for **Bpod**, you always have to activate at least the basic PyBpod plugin (pybpod-gui-plugin).

You can use plugins for:
    * extending or overwriting basic PyBpod functionalities;
    * creating new visualization tools for PyBpod sessions (e.g., plots, message filters);
    * adding new windows, tools or any other GUI-related functionality;


Plugin loading explained
========================

.. warning::
    Will be implemented soon.