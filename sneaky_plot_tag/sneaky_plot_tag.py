import __main__

import git
import os

import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText

def git_short_hash():

    try:
        repo = git.Repo(os.path.basename(__main__.__file__), search_parent_directories=True)
    except AttributeError: # jupyter notebook
        repo = git.Repo(os.path.abspath(""), search_parent_directories=True)
        # workaround - assumes notebook cwd is equal to script directory, which is not usually true

    return repo.git.rev_parse(repo.head, short=True)

def add_git_hash(axes):

    text_box = AnchoredText(git_short_hash(), frameon=True,  loc='lower left', pad=0.3, prop={"fontsize": "xx-small"})
    plt.setp(text_box.patch, facecolor='white', alpha=0.5)
    axes.add_artist(text_box)

def __figure(*args, **kwargs):

    fig = plt._figure(*args, **kwargs)
    add_git_hash(plt.gca())

    return fig

def global_sneaky_tag_override():

    plt._figure = plt.figure
    plt.figure = __figure

global_sneaky_tag_override()
