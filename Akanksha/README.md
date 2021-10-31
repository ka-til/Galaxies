# Files from Akanksha

## Installation with conda
Taken from https://pyautolens.readthedocs.io/en/latest/installation/conda.html
Pre-req: Install Anaconda Navigator(anaconda3) before running the following steps.
1) Open Anaconda prompt in Windows 10 (This step changes depending on the OS)
2) Run '''conda --version'''
3) Run '''conda update conda''' (The latest version is 4.10.3)
4) Type y (if new update is available)

Now installing PyAutoLens
1) Run '''conda create -n autolens astropy numba numpy scikit-image scikit-learn scipy'''.
2) Run '''conda activate autolens (everytime you want to run PyAutoLens)'''.
3) Once in autolens environment run '''pip install --upgrade pip --user'''.
4) Check if numba and llvmlite are installed, to check run '''pip show llvmlite''' and '''pip show numba'''.
5) If uninstalled follow steps from https://pyautolens.readthedocs.io/en/latest/installation/troubleshooting.html.
6) If installed run '''pip install autolens==2021.10.14.1 --ignore-installed numba llvmlite'''.

Error encountered
ERROR: Could not install packages due to an OSError: [WinError 3] The system cannot find the path specified:
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths

Corrected using https://www.howtogeek.com/266621/how-to-make-windows-10-accept-file-paths-over-260-characters/

Installing autolens workspace
1) '''cd /path/on/your/computer/you/want/to/put/the/autolens_workspace'''.
2) '''git clone https://github.com/Jammy2211/autolens_workspace --depth 1'''.

Note: Better not to clone the repository into Galaxies repository

Testing PyAutoLens Installation
1) Run '''python welcome.py'''.
2) If PyAutoLens is succesfully installed 4 plots appear.


## Basic Git commands
1) '''git clone (repository https)''' cloning the repository.
2) '''git status''' current status of local repository
3) '''git add (file/folder name)''' adds file to git staging area.
4) '''git commit -m '(message for the commit)' ''' captures the snapshot of the project's currently staged changes.
5) '''git push origin (branch name)''' push local contents to github.
6) '''git pull''' update local version of repository.

### Creating SSH keys
1) Run '''ssh-keygen -t rsa -b 4096 -C "(your git email id)" ''' in repository folder
2) press enter key (now ssh key will be saved in path specified)
3) enter your passphrase (remember this to push the changes into the repository)
4) cat /path/to/ssh/key/.ssh/id_rsa.pub and copy the content
5) go to https://github.com/settings/keys and create a new key
6) Run '''ssh -T git@github.com''' and type yes when prompted.
7) Run '''git remote set-url origin git@github.com:(username)/(repository name).git'''
<<<<<<< HEAD

## Finding Data

F814W (I-band)

Data - https://archive.stsci.edu/missions-and-data/hst#section-5a09530d-b489-4f42-83e2-ee44394040c0
 https://mast.stsci.edu/search/hst/ui/#/


## Data Reduction

### arCTIc software

https://github.com/jkeger/arcticpy

### calacs
https://hst-docs.stsci.edu/acsdhb/chapter-3-acs-calibration-pipeline/3-3-structure-of-calacs
https://github.com/spacetelescope/hstcal

### astrodrizzle

https://github.com/spacetelescope/drizzlepac
https://www.stsci.edu/itt/review/DrizzlePac/HTML/DrizzlePac.cover.html#533584


### TinyTim

https://www.stsci.edu/files/live/sites/www/files/home/hst/instrumentation/focus-and-pointing/documentation/_documents/krist_tinytim_spie.pdf
https://github.com/spacetelescope/tinytim
=======
>>>>>>> 8d55828d5a385e32a7c14b1f43c9b1cda96940cd
