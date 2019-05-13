from util import *
import numpy as np
import json
import itertools
import matplotlib.pyplot as plt

head = ['camera','look_away_slide','slide','look_down','other']
gesture = ['beats','metaphoric','deictic','iconic','None']
total_state = itertools.product(head,gesture)
total_state = [s[0]+'_'+s[1] for s in total_state]

result = []
with open('data/bi.csv') as f:
    lines = f.readlines()
    result = [line.split() for line in lines]

for i,s in enumerate(result):
    result[i] = s[0]+'_'+s[1]

trans = second_order_transition_prop(result, total_state)
new_trans  = {}
for t in trans:
    if trans[t] > 0:
        new_trans[t] = trans[t]

trans = second_order_transition_count(result, total_state)
trans = sorted(trans.items(), key=lambda kv: -kv[1])

trans = [[str(t[0]).strip().replace(',','\t'),t[1]] for t in trans]

trans = np.array(trans)

np.savetxt("data/sec_bi.csv", np.array(trans),fmt='%s', delimiter=',')

# plt.bar(range(len(poses_fre)),poses_fre,tick_label=head)
# plt.show()


