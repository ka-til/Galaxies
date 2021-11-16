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


Installation

1) Install make
2) Install gcc
3) Follow steps from manual - under compiling

Steps

1) ./tiny1 outfilename [jitter=4 mas] taken from https://www.stsci.edu/files/live/sites/www/files/home/hst/instrumentation/acs/documentation/instrument-science-reports-isrs/_documents/isr1708.pdf

For object - SDSSJ0252+0039
Instrument and camera - 15
Detector - 1(WFC1)
Position - 2194, 3178(Graeme) --- after correction y-coordinate is 1130 [ 2048 - (2*2048 - 3178)]
Filter - F814W
Spectrum - 1 - 7(A07) (Not sure what value to put in, will change later on)
PSF Diameter - 3.0
Focus, secondary mirror despace - -0.7765668337488701 (Focus model - https://www.stsci.edu/hst/instrumentation/focus-and-pointing/focus/hst-focus-model for 2006,
                                                       Modified Julian Date converter - https://www.timeanddate.com/calendar/?year=2006&country=23
                                                       Value calculated in InterpolatingFocus.ipynb)

Root File name - outfilename
2) ./tiny2 outfilename
3) ./tiny2 outfilename option_parameter_file(.tt3 from tiny2)


1) Get a focus model, including it with tinytim should be easy. But what model should we use, the 2011 paper discusses using focus model. But the paper we are using states the following procedure.

"We first identified stars in the deep, stacked image using their locus in size–magnitude space.
We then measured the ellipticity of each star in individual exposures. By comparing these to TinyTim (46)
models of the HST PSF (created by raytracing through the telescope at different focus positions but at
the appropriate wavelengths for the band), we determined the focus position for each exposure. We then
interpolated (second and fourth shape moments of) the TinyTim PSF model to the position of the galaxies,
rotating into the reference frame of the MultiDrizzle mosaic" - taken from https://arxiv.org/pdf/1503.07675.pdf

2) How do you know where the peak is?

3) How is WFC1 different from WFC2??

4) What should be the subsampling value

5) Spectrum value?

6) Produce for how many pixels? The PSF diameter is 3 arcseconds - our galaxy lens is about 3 arcseconds?

Work left

1) Include focusing
2) covolution with image - https://het.as.utexas.edu/HET/Software/Astropy-0.4.2/convolution/index.html

Covolution

#### For ACS

https://www.stsci.edu/files/live/sites/www/files/home/hst/instrumentation/focus-and-pointing/documentation/_documents/tinytim.pdf

Because of the significant distortion in the ACS, the way Tiny Tim computes ACS PSFs is
somewhat different than for the other cameras. This includes the use of a third program, tiny3, that
does geometric distortion

ACS is composed of three channels. The wide field channel (WFC:f/26, 0.05”/pixel) has two 4096 × 2048 CCD
detectors for λ = 400 – 1100 nm imaging. The high resolution channel (HRC:f/72, 0.025”/pixel) has a single 1024 ×
1024 CCD for λ = 170 – 1000 nm imaging. The solar blind channel (SBC:f/72, 0.030”/pixel) uses a STIS-like MAMA
detector for λ = 115 – 170 nm imaging, and it shares the HRC optical train and field of view (an actuated mirror selects
the detector). WFC and HRC/SBC image separate portions of the HST focal plane. The HRC is no longer in operation
due to an electronic failure. That channel also had a selectable coronagraphic mode (occulted sources are not simulated
by Tiny Tim, though field sources are by including the Lyot stop in the obscuration pattern).

### PSF

https://www.stsci.edu/hst/instrumentation/wfc3/data-analysis/psf

ACS - https://www.stsci.edu/itt/APT_help/ACS_Cycle21/c05_imaging7.html


### Focus model

https://www.stsci.edu/hst/instrumentation/focus-and-pointing/focus/hst-focus-model
