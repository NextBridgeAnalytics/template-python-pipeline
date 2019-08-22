# {{ cookiecutter.project_name }} - Notebooks

The files in this folder are Jupyter Notebooks that are used in the {{ cookiecutter.project_name }} project.

Typically, you use them through the Jupyter Notebook or Jupyter Lab applications. You can either start these from Anaconda Navigator, or from your command line by navigating to this folder and running one of the following commands:

```
$ jupyter notebook
$ jupyter lab
```


# Tools

The `tools` directory contains Python scripts meant to make working with the notebooks more convenient. In addition to these local tools, have a look at the official Notebook extensions.

TODO: More about the extensions

## Easier Github Workflow

Notebooks can be annoying to combine with Github because notebooks are modified simply by executing them.

### Clean Notebook at Save

The `install_clean_save.py` tool installs a save hook to your Jupyter configuration file that cleans your files before saving, so that they cooperate better with Github (or any other version control system).

By running `$ python install_clean_save.py` the following happens:

- All `.ipynb` files inside of folders named `work` are ignored by Git
- A save hook is installed in your current conda environment. This hook will apply everytime you save a notebook **inside a folder named `work`**. The hook will save a copy of your current notebook in the parent directory with all output and execution counts removed.

This allows for the following workflow when using notebooks together with Git:

- If necessary, create a topical directory where you want to save your notebook (for instance `download_data`)
- Inside this directory (or directly in the `notebooks` directory), create a directory named `work` (so the complete path is `download_data/work/` in the example)
- The `work/` directory will be where you work with your notebooks. Go ahead and create a new notebook in this directory
- When you save your notebook, a copy of the notebook **with all outputs and execution counts removed** is stored in the parent folder (`download_data/` in our example)
- When adding and commiting files to Git, you only commit the cleaned notebooks. This should avoid all the "false alarms" about changes in your notebooks

If you have any notebooks where you really want to save the output to Git, for instance as documentation, simply save it directly in the topical directory (for example `download_data/`). Only notebooks directly inside a directory named `work/` will be cleaned.


### Better Diffs and Conflict Handling

The [`nbdime`]() project (NoteBook DIff and MErge) can be used to get notebook-aware diffs in Git. It is available as a Conda- or Pip--install. Use one of the following:

```
$ conda install nbdime
$ python -m pip install nbdime
```