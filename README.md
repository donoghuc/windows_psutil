# Project Req
- Enumerate all the running processes.
- List all the running threads within process boundary.
- Enumerate all the loaded modules within the processes.
- Is able to show all the executable pages within the processes.
- Gives us a capability to read the memory.

### SETUP
- on windows 7, get miniconda, go through their install
```
https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe
```
- pip install virtualenv
- make virtualenv
- activate new env
```
pip install virtualenv
virtualenv -p C:\Users\John\Miniconda3\Python.exe --no-site-packages env_hw5
env_hw5\Scripts\activate
```
- install pyinstaller
- build exe for windows
- execute
```
pip install pyinstaller
pyinstaller hw_5.py
dist\hw_5\hw_5.exe
```
## portability
Note that I transfer the "dist" folder to USB stick (54 items, 12MB) to a separate machine running windows 10 (with no python installation) and the program seems to operate just fine! 
