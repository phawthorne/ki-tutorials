# Python 101

This tutorial aims to get you set up with a working installation of Python on your computer, and to provide a minimal introduction of how to write and run a simple data analysis script.

## Step 1: Installing Python and VSCode

Python is different than some computational software (e.g. Matlab) in that the core language is generally separate from the software you use to write, edit, and often run the code. The language is also available from multiple sources and can exist in different, potentially conflicting, versions on your computer. The way I suggest setting up Python here is the one I've found to be the easiest and to minimize potential issues.

### Install Python
We will use the version of Python available from [Anaconda](https://www.anaconda.com/). It is useful to use this one, rather than downloading from [python.org](https://www.python.org), because the anaconda version is carefully packaged not to interfere with other versions of python you might have installed on your computer, and comes with the `conda` tool, which provides a very helpful way to manage packages and "virtual environments" (not something to worry about for now, but very handy when you're juggling projects with different dependencies).

#### Steps:

* Download the appropriate version of Python 3.8 from [here](https://docs.conda.io/en/latest/miniconda.html)
    - This is the "miniconda" version, which provides a minimal set of packages to build on rather than some hundreds of things you might not need. 
* Follow the appropriate instructions for your operating system [here](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#starting-conda) to open a command line window.
    - Windows: open "Anaconda Prompt" from the start menu
    - Mac: open the "Termial" app
* Create a new python environment: type `conda create --name py38 python=3.8` in the command line. 
    - An "environment" is a version of python on your computer that has a particular set of packages installed. Typically, you can just have one main environment, but sometimes you might have a project that depends on having specific versions of packages that you want to keep separate from your main environment.
* Activate the environment: type `conda activate py38`.
* Specify that we'd like to get packages from [conda-forge](https://conda-forge.org/): type `conda config --add channels conda-forge`, followed by `conda config --set channel_priority strict`. 
    - Conda-forge is a community-driven portal for accessing python packages. They put a ton of work into ensuring a successful installation process and compatibility between different package versions. These commands will make conda-forge the default download site. 
* Install some useful packages: `conda install numpy pandas matplotlib`.
    - This will also install a lot of other packages that these ones depend on. Answer "Y" if it asks for confirmation.

In order to use this version of Python you just installed, you'll need to run the command `conda activate py38` in the Anaconda Prompt or Terminal app each time you open a new window (or add it to your start up configuration, which is beyond the scope of this tutorial).

### Install VSCode
In order to use Python effectively, you'll need a separate code editor. There are lots of choices, but I suggest using Microsoft's Visual Studio Code. It's free, very well supported, and also works with nearly every other programming language so you only need to learn one editor to have a very functional tool. Another good choice is PyCharm, which is specific to Python, but the company behind it has similar applications for other languages also.

* Download and install VSCode [here](https://code.visualstudio.com/).


## Step 2: Running a simple script 
Now we're going to create a project in VSCode, add a python script, and run it.

* Open VSCode, and choose "Add workspace folder..." from the "Start" section of the menu.
    - Create a new folder called "python-101" (or whatever you want), and select Add. 
    - Workspaces are the way VSCode organizes files and settings associated with a particular project. When you close the window you'll be asked whether you want to save the workspace.
* Create a new file. Immediately save the file so that you can give it a name. Call it `simple_script.py`. VSCode will see the `.py` ending, and load its Python tools. 
* Here's the tricky part - you need to configure VSCode so that it knows to use the `py38` environment you created in step 1. Down in the lower-left corner of the window, in the blue bar, it will say something like 'Python 3.X ...' or may have a warning that says "Select Python Environment"
    - Click to bring up a prompt about selecting the workspace. Select "Entire workspace"
    - It should display a list of potential environments that includes the `py38` environment - select this one. The [VSCode docs about this](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment) mention that it can take a while for VSCode to find all the environments.
* Copy and paste this code into `simple_script.py` and save the file. Note that this script has a lot of excess `print()` statements and is not structured the way I'd typically write code - just treat it as a demo, not an example to be followed.

```python
import os
# in order to use a package, you have to import it
# adding `as pd` lets us refer to it with a shorter name
import pandas as pd

# load a data file
input_file = "PATH_TO_DATA.CSV"
df = pd.read_csv(input_file)
print()
print("Original Table:")
print(df.head())  # head selects just the first few rows
print()

# group the data by state, and compute the sum (this will drop the 
# non-numeric "county" column)
state_sums = df.groupby(by="state").sum()

# in the summed table, the summed column is still called "value", but
# it will make more sense for us to give it a distinguishable name
state_sums = state_sums.rename(columns={"value": "state_total"})

# merge the sums back to the original table
df = pd.merge(df, state_sums, on="state")
print("After merge:")
print(df.head())
print()

# Calculate some additional statistics
df["county_fraction"] = df["value"] / df["state_total"]
print("With county fraction:")
print(df.head())

# Save the updated table in the same folder as the input file
output_file = os.path.join(os.path.dirname(input_file), "output.csv")
df.to_csv(output_file, index=False)
```

* Make a new file, save it as "data.csv" in the same folder as the python script, and paste in these values:

```csv
state,county,value
MN,A,10
MN,B,20
IA,C,5
IA,D,5
IA,E,8
```

* In `simple_script.py`, find the line that reads `filepath = "PATH_TO_DATA.CSV"`. Edit `PATH_TO_DATA.CSV` to be the correct path to the file on your computer. Hint: if you right click on `data.csv` in the VSCode "Explorer" side bar, there is an option to "Copy Path". 
* Finally, find and click the little green arrow at the top of the editor window to run the script.


## Step 3: Core scientific Python packages

* [Pandas](https://pandas.pydata.org/): Good for dealing with tabular data. Allows grouping, reshaping, filling, joining, plotting, ect...
* [Matplotlib](https://matplotlib.org/): Package for making plots/figures. Pretty straightforward to use for basic things, and with some powerful (but complex) options for customized plots.
* [Numpy](https://numpy.org/): Provides fast numerical arrays and matrices.
* [Scipy](https://scipy.org/): Very wide-ranging package covering things like linear algebra, FFTs, interpolation, and some stats. 
* [Geopandas](https://geopandas.org/): Awesome package for working with shapefiles. Access the data as with Pandas, perform spatial operations, and create maps. 
* [Pygeoprocessing](https://github.com/natcap/pygeoprocessing): A NatCap-created package for working with spatial datasets (rasters, particularly). A bit complicated, but powerful - it is the engine of most NatCap models. An alternative is to use [GDAL](https://pypi.org/project/GDAL/) directly but this has, by my estimation, an even steeper learning curve. 
* [Jupyter](https://jupyter.org/): A "notebook" based system for writing python code - this is an alternative to using something like VSCode. Can be useful for communication because it allows results (e.g. figures) and text blocks interspersed with the code. Also useful for quick prototyping sometimes.

We didn't install all of these to start. To add new packages, make sure you have the right environment activated (e.g. `conda activate py38`), and then type `conda install PACKAGE`. You can also list multiple packages, and conda will ensure that the selected versions are mutually compatible. 