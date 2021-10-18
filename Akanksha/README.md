#Files from Akanksha

##Installation with conda taken from https://pyautolens.readthedocs.io/en/latest/installation/conda.html

1) Open Anaconda prompt in Windows 10
2) Run '''conda --version'''
3) Run '''conda update conda''' (The latest version is 4.10.3)
4) Type y (if new update is available)

Now installing PyAutoLens
5) Run '''conda create -n autolens astropy numba numpy scikit-image scikit-learn scipy'''
6) Run '''conda activate autolens (everytime you want to run PyAutoLens)'''
7) Once in autolens environment run '''pip install --upgrade pip --user'''
8) Check if numba and llvmlite are installed, to check run '''pip show llvmlite''' and '''pip show numba'''
9) If uninstalled follow steps from https://pyautolens.readthedocs.io/en/latest/installation/troubleshooting.html
10) If installed run '''pip install autolens==2021.10.14.1 --ignore-installed numba llvmlite'''

Error encountered
ERROR: Could not install packages due to an OSError: [WinError 3] The system cannot find the path specified:
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths

Corrected using https://www.howtogeek.com/266621/how-to-make-windows-10-accept-file-paths-over-260-characters/

Installing autolens workspace
11) '''cd /path/on/your/computer/you/want/to/put/the/autolens_workspace'''
12) '''git clone https://github.com/Jammy2211/autolens_workspace --depth 1'''

Note: Better not to clone the repository into Galaxies repository

Testing PyAutoLens Installation
1) Run '''python welcome.py'''
2) If PyAutoLens is succesfully installed 4 plots appear.
