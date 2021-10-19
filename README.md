# Galaxies
Group project for galaxies course

## Installation with conda taken from https://pyautolens.readthedocs.io/en/latest/installation/conda.html

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

Installing autolens workspace
1) '''cd /path/on/your/computer/you/want/to/put/the/autolens_workspace'''.
2) '''git clone https://github.com/Jammy2211/autolens_workspace --depth 1'''.

Note: Better not to clone the repository into Galaxies repository

Testing PyAutoLens Installation
1) Run '''python welcome.py'''.
2) If PyAutoLens is succesfully installed 4 plots appear.

## Basic Git commands
1) '''git clone (repository https)''' cloning the repository.
2) '''git add (file/folder name)''' adds file to git staging area.
3) '''git commit -m '(message for the commit)' ''' captures the snapshot of the project's currently staged changes.
4) '''git push origin (branch name)''' push local contents to github.
5) '''git pull''' update local version of repository.
### Creating SSH keys

1) Run '''ssh-keygen -t rsa -b 4096 -C "(your git email id)" ''' in repository folder
2) press enter key (now ssh key will be saved in path specified)
3) enter your passphrase (remember this to push the changes into the repository)
4) cat /path/to/ssh/key/.ssh/id_rsa.pub and copy the content
5) go to https://github.com/settings/keys and create a new key
6) Run '''ssh -T git@github.com''' and type yes when prompted.
7) Run '''git remote set-url origin git@github.com:(username)/(repository name).git'''

## Bookeeping

Add descriptions to the files/folders you are adding to the repo
