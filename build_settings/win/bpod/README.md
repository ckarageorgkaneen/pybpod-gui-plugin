# How to create a binary for Windows using PyInstaller 

We provide the *build.bat* script to create binaries using Jenkins. If you need to run it locally please run the following steps.
 
1. Install WinPython
2. Open standard windows command line
3. Change *build.bat* file to match your WinPython installation:
```
    set "WINPYDIR=C:\WinPython\WinPython-64bit-3.5.3.0Qt5-behavior\python-3.5.3.amd64"
    set "WINPYVER=3.5.3.0Qt5"
    set "HOME=%WINPYDIR%\..\settings"
    set "WINPYARCH=WIN-AMD64"
```
4. Set local vars (change according with your preference):

````
    > build_settings\win\bpod\set-local-vars.bat
````

5. From the root folder of the project, run the following command:

````
    > build_settings\win\bpod\build.bat
````
