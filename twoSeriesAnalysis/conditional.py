result = []
import matplotlib.pyplot as plt
from util import *

head = ['camera','look_away_slide','slide','look_down','other']
gesture = ['beats','metaphoric','deictic','iconic','None']

with open('data/ta.csv') as f:
    lines = f.readlines()
    result = [line.split() for line in lines]

poses = [r[0] for r in result]
gestures = [r[1] for r in result]
poses_fre = frequency(head, poses)
ges_fre = frequency(gesture, gestures)
poses_fre = [poses_fre[p] for p in poses_fre]
ges_fre = [ges_fre[p] for p in ges_fre]
plt.bar(range(len(poses_fre)),poses_fre,tick_label=head)
plt.show()
plt.bar(range(len(ges_fre)),ges_fre,tick_label=gesture)
plt.show()

cond_probs = []
for p in head:
    ges = [r[1] for r in result if r[0]==p]
    fre = frequency(gesture,ges)
    cond_probs.append(fre)

for i,p in enumerate(head):
    cond = cond_probs[i]
    probs = [cond[k] for k in cond]
    label = [k for k in cond]
    ax = plt.subplot(3, 2, i+1)
    plt.bar(range(len(probs)),probs,tick_label=label)
    ax.set_title(p)
plt.show()

cond_probs = []
for p in gesture:
    h = [r[0] for r in result if r[1]==p]
    fre = frequency(head,h)
    cond_probs.append(fre)

for i,p in enumerate(gesture):
    cond = cond_probs[i]
    probs = [cond[k] for k in cond]
    label = [k for k in cond]
    ax = plt.subplot(3, 2, i+1)
    plt.bar(range(len(probs)),probs,tick_label=label)
    ax.set_title(p)
plt.show()