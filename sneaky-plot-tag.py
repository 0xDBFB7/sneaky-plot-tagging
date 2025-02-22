import __main__

import git
import os


def get_project_root():
    # does not do what it says on the tin - gets the root of the *bl_API* project
    return str(Path(__file__).absolute().parent.parent.parent)

def is_notebook():
    try:
        shell = get_ipython().__class__.__name__
        return True
    except NameError:
        return False     

def git_short_hash():

    try:
        repo = git.Repo(os.path.basename(__main__.__file__), search_parent_directories=True)
    except AttributeError: # jupyter notebook
        repo = git.Repo(os.path.abspath(""), search_parent_directories=True)
        # workaround - assumes notebook cwd is equal to script directory, which is not usually true

    return repo.git.rev_parse(repo.head, short=True)

from time import sleep 

import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText

def add_git_hash(axes):
    text_box = AnchoredText(git_short_hash(), frameon=True,  loc='lower left', pad=0.3, prop={"fontsize": "xx-small"})
    plt.setp(text_box.patch, facecolor='white', alpha=0.5)
    axes.add_artist(text_box)


