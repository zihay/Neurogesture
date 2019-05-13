# %% [markdown]
# # Load Data:

# %%
from util import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import scipy.stats as stats

def flatmap(array):
    return [e for l in array for e in l]


# %%
VID_SCORE = [[13, 14, 13, 15, 18, 4], [
    10, 14, 13, 12, 17, 8], [17, 14, 15, 11, 6, 6]]

VID_SCORE_DUAL = [[15, 11, 10, 13, 12, 9], [
    16, 16, 18, 10, 19, 4], [16, 17, 13, 13, 8, 7]]

VID_SCORE_SINGLE = [[17, 11, 12, 12, 17, 9], [
    9, 13, 8, 7, 13, 3], [10, 15, 14, 10, 1, 6]]


bi = [
    'metaphoric',
    'beats',
    'beats',
    'deictics',
    'deictics',
    'iconic'
]

ps = [
    'metaphoric',
    'metaphoric',
    'deictics',
    'iconic',
    'metaphoric',
    'beats'
]

ta = ['metaphoric',
      'metaphoric',
      'beats',
      'beats',
      'beats',
      'metaphoric']

TYPE = [['recall','recall','infer','recall','recall','infer'],['recall','infer','recall','recall','infer','recall'],['recall','recall','infer','infer','recall','recall']]

# %%
bar_width = 0.2
opacity = 0.4

all_ges = bi + ps + ta
TYPE = flatmap(TYPE)
full_score = flatmap(VID_SCORE)
full_num = 19
dual_score = flatmap(VID_SCORE_DUAL)
dual_num = 20
single_score = flatmap(VID_SCORE_SINGLE)
single_num = 19
print(all_ges)
print(full_score)

# %% [markdown]
# ## metaphoric:

# %%
all_ges.count('metaphoric')


# %%
def plot_barchart(type):
    num = all_ges.count(type)
    index = np.arange(num)
    
    full = [full_score[i] for i, t in enumerate(all_ges) if t == type]
    dual = [dual_score[i] for i, t in enumerate(all_ges) if t == type]
    single = [single_score[i] for i, t in enumerate(all_ges) if t == type]
    t = [TYPE[i] for i, t in enumerate(all_ges) if t == type]
    full = np.array(full)
    dual = np.array(dual)
    single = np.array(single)

    full = full/full_num
    dual = dual/dual_num
    single = single/single_num

    fig, ax = plt.subplots()
    rects1 = ax.bar(index, full, bar_width,
                    alpha=opacity, color='b',
                    label='Full')
    rects2 = ax.bar(index + bar_width, dual, bar_width,
                    alpha=opacity, color='r',
                    label='Dual')
    rects3 = ax.bar(index + bar_width + bar_width, single, bar_width,
                    alpha=opacity, color='g',
                    label='Single')
    ax.set_xlabel('type')
    ax.set_ylabel('Scores')
    ax.set_title(type)
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(t)
    ax.legend()

    fig.tight_layout()
    plt.show()


# %%
plot_barchart('metaphoric')


#%%
plot_barchart('beats')

#%%
plot_barchart('deictics')

#%%
plot_barchart('iconic')

#%%
