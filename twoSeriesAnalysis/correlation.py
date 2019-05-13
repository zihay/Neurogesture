from util import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


result = []

gesture = ['beats', 'metaphoric', 'deictics', 'iconic']
# VID_SCORE = [[13, 15, 14, 16, 19, 4],[10, 14, 14, 13, 18, 8],[18, 14, 16, 11, 6, 6]]
# VID_SCORE_TOTAL = [[20, 20, 20, 20, 20, 20], [20, 20, 20, 20, 20, 20], [20, 20, 20, 20, 20, 20]]


# VID_SCORE_DUAL = [[16, 12, 10, 14, 13, 10],[17, 17, 19, 11, 20, 4],[16, 17, 14, 13, 8, 7]]

# VID_SCORE_SINGLE = [[20, 13, 12, 14, 19, 9],[12, 15, 10, 8, 16, 3],[12, 18, 14, 12, 2, 7]]


# bi = [
#     'metaphoric',
#     'beats',
#     'beats',
#     'deictics',
#     'deictics',
#     'iconic'
# ]

# ps = [
#     'metaphoric',
#     'metaphoric',
#     'deictics',
#     'iconic',
#     'metaphoric',
#     'beats'
# ]

# ta = ['metaphoric',
#       'metaphoric',
#       'beats',
#       'beats',
#       'beats',
#       'metaphoric']

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

TYPE = [['recall', 'recall', 'infer', 'recall', 'recall', 'infer'],
        ['recall', 'infer', 'recall', 'recall', 'infer', 'recall'],
        ['recall', 'recall', 'infer', 'infer', 'recall', 'recall']]

fig, ax = plt.subplots()
index = np.arange(4)
fig, ax = plt.subplots()
bar_width = 0.2
opacity = 0.4


def flatmap(array):
    return [e for l in array for e in l]


all_ges = bi + ps + ta
all_score = flatmap(VID_SCORE)

result = {g: 0 for g in gesture}
total = {g: 0 for g in gesture}
for i, g in enumerate(all_ges):
    result[g] += all_score[i]
    total[g] += 20

for k in result:
    result[k] = result[k]/total[k]


rects1 = ax.bar(index, list(result.values()), bar_width,
                alpha=opacity, color='b',
                label='Full')


all_score = flatmap(VID_SCORE_DUAL)

result = {g: 0 for g in gesture}
total = {g: 0 for g in gesture}
for i, g in enumerate(all_ges):
    result[g] += all_score[i]
    total[g] += 21

for k in result:
    result[k] = result[k]/total[k]

rects2 = ax.bar(index + bar_width, list(result.values()), bar_width,
                alpha=opacity, color='r',
                label='Dual')

all_score = flatmap(VID_SCORE_SINGLE)

result = {g: 0 for g in gesture}
total = {g: 0 for g in gesture}
for i, g in enumerate(all_ges):
    result[g] += all_score[i]
    total[g] += 22

for k in result:
    result[k] = result[k]/total[k]

rects2 = ax.bar(index + bar_width + bar_width, list(result.values()), bar_width,
                alpha=opacity, color='g',
                label='Single')

ax.set_xlabel('Gestures')
ax.set_ylabel('Scores')
ax.set_title('Gestures & Scores')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels([*result])
ax.legend()

fig.tight_layout()
plt.show()
