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
# print(all_ges)
# print(full_score)

def anova(type):
    full = [full_score[i] for i, t in enumerate(all_ges) if t == type]
    dual = [dual_score[i] for i, t in enumerate(all_ges) if t == type]
    single = [single_score[i] for i, t in enumerate(all_ges) if t == type]
    # print(full)
    F,p = stats.f_oneway(full,dual)
    print(type,F,'\t',p)
    # F,p = stats.f_oneway(dual,single)
    # print(F,p)
    # F,p = stats.f_oneway(full,single)
    # print(F,p)

anova('beats')
anova('metaphoric')
anova('deictics')
anova('iconic')

#%%

def anova2(type):
    full = [full_score[i] for i, t in enumerate(all_ges) if t == type]
    dual = [dual_score[i] for i, t in enumerate(all_ges) if t == type]
    n = len(full)
    full = sum(full)
    dual = sum(dual)
    full = [1 if i<full else 0 for i in range(19*n)]
    dual = [1 if i<dual else 0 for i in range(20*n)]
    F,p = stats.f_oneway(full,dual)
    print(type,F,'\t',p)

anova2('beats')
anova2('metaphoric')
anova2('deictics')
anova2('iconic')
#%%

def ttest(type):
    full = [full_score[i] for i, t in enumerate(all_ges) if t == type]
    dual = [dual_score[i] for i, t in enumerate(all_ges) if t == type]
    F,p = stats.ttest_ind(full,dual)
    print(type,F,p)

ttest('beats')
ttest('metaphoric')
ttest('deictics')
ttest('iconic')
#%%
F,p = stats.f_oneway(dual_score,single_score)
print(F,p)


#%%
