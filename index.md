# Python 101

This tutorial aims to get you set up with a working installation of Python on your computer, and to provide a minimal introduction of how to write and run a simple data analysis script.

## Step 1: Installing Python and VSCode

Python is different than some computational software (e.g. Matlab) in that the core language is generally separate from the software you use to write, edit, and often run, the code. The language is also available from multiple sources, and can exist in multiple different, potentially conflicting versions, on your computer. The way I suggest setting up Python here is the one I've found to be the easiest and to minimize potential issues.

### Install Python
We will use the version of Python available from [Anaconda](https://www.anaconda.com/). It is useful to use this one, rather than downloading from [python.org](https://www.python.org), because the anaconda version is carefully packaged not to interfere with other versions of python you might have installed on your computer, and comes with the `conda` tool, which provides a very helpful way to manage packages and "virtual environments" (not something to worry about for now, but very handy when you're juggling projects with different dependencies).

Steps:

* Download the appropriate version of Python 3.8 from [here](https://docs.conda.io/en/latest/miniconda.html)
* Follow the appropriate instructions for your operating system [here](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#starting-conda) to open a command line window.
    - Windows: open "Anaconda Prompt" from the start menu
    - Mac: open the "Termial" app
* Create a new python environment: type `conda create --name py38 python=3.8` in the command line. 
    - An "environment" is a version of python on your computer that has a particular set of packages installed. Typically, you can just have one main environment, but sometimes you might have a project that depends on having specific versions of packages that you want to keep separate from your main environment.
* Activate the environment: type `conda activate py38`.
* Specify that we'd like to get packages from [conda-forge](https://conda-forge.org/): type `conda config --add chanels conda-forge`, followed by `conda config --set channel_priority strict`. 
    - Conda-forge is a community-driven portal for accessing python packages. They put a ton of work into ensuring a successful installation process and compatibility between different package versions. These commands will make conda-forge the default download site. 
* Install some useful packages: `conda install pandas matplotlib geopandas pygeoprocessing jupyter ipython`.
    - This will also install a lot of other packages that these ones depend on. Answer "Y" if it asks for confirmation.


