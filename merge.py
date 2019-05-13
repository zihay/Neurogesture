from preprocessing import *
from util import *
import numpy as np
import json
ges = result
pose = []
with open('headposebi.csv') as f:
    content = f.readlines()
    for line in content:
        l = line.split()
        pose.append(l[0])

result = []
j = 0
for i in range(len(pose)):
    g = ges[j]
    if g[0]!=i:
        result.append((pose[i],'None'))
    else:
        result.append((pose[i],g[1]))
        j+=1

for i,s in enumerate(result):
    result[i] = s[0]+'_'+s[1]

state = list(set(result))
fre = frequency(result)

transition_fre = transition_prop(result)
draw_fre(fre)
with open('data.json', 'w') as outfile:
    json.dump(fre, outfile)

draw_transition(state,transition_fre)

with open('data_transition.json', 'w') as outfile:
    links=[]
    for t in transition_fre:
        a,b = t
        prob=transition_fre[t]
        links.append({'source':a,'target':b,'prob':prob})

    json.dump(links, outfile)

table = get_transition_table(state,transition_fre)
np.savetxt("bi_table.csv", np.array(table),fmt='%s',delimiter=',')

