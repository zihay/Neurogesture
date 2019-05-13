from util import *
import numpy as np
import json
import itertools
pose = []
result = []

head = ['camera','look_away_slide','slide','look_down','other']
gesture = ['beats','metaphoric','deictic','iconic','None']
total_state = itertools.product(head,gesture)
total_state = [s[0]+'_'+s[1] for s in total_state]

with open('data/bi.csv') as f:
    lines = f.readlines()
    result = [line.split() for line in lines]

for i,s in enumerate(result):
    result[i] = s[0]+'_'+s[1]

state = list(set(result))
fre = frequency(total_state,result)

transition_fre = transition_prop(result)
draw_fre(fre)

with open('bi.js', 'w') as outfile:
    j = json.dumps(fre)
    outfile.write('bi_fre='+j)

draw_transition(state,transition_fre)

with open('bi_trans.js', 'w') as outfile:
    links=[]
    for t in transition_fre:
        a,b = t
        prob=transition_fre[t]
        links.append({'source':a,'target':b,'prob':prob})
    
    j = json.dumps(links)
    outfile.write('bi_trans='+j)

table = get_transition_table(state,transition_fre)
np.savetxt("bi_table.csv", np.array(table),fmt='%s',delimiter=',')








with open('data/ps.csv') as f:
    lines = f.readlines()
    result = [line.split() for line in lines]

for i,s in enumerate(result):
    result[i] = s[0]+'_'+s[1]

state = list(set(result))
fre = frequency(total_state,result)

transition_fre = transition_prop(result)
draw_fre(fre)

with open('ps.js', 'w') as outfile:
    j = json.dumps(fre)
    outfile.write('ps_fre='+j)

draw_transition(state,transition_fre)

with open('ps_trans.js', 'w') as outfile:
    links=[]
    for t in transition_fre:
        a,b = t
        prob=transition_fre[t]
        links.append({'source':a,'target':b,'prob':prob})
    
    j = json.dumps(links)
    outfile.write('ps_trans='+j)

table = get_transition_table(state,transition_fre)
np.savetxt("ps_table.csv", np.array(table),fmt='%s',delimiter=',')









with open('data/ta.csv') as f:
    lines = f.readlines()
    result = [line.split() for line in lines]

for i,s in enumerate(result):
    result[i] = s[0]+'_'+s[1]

state = list(set(result))
fre = frequency(total_state,result)

transition_fre = transition_prop(result)
draw_fre(fre)

with open('ta.js', 'w') as outfile:
    j = json.dumps(fre)
    outfile.write('ta_fre='+j)

draw_transition(state,transition_fre)

with open('ta_trans.js', 'w') as outfile:
    links=[]
    for t in transition_fre:
        a,b = t
        prob=transition_fre[t]
        links.append({'source':a,'target':b,'prob':prob})
    
    j = json.dumps(links)
    outfile.write('ta_trans='+j)

table = get_transition_table(state,transition_fre)
np.savetxt("ta_table.csv", np.array(table),fmt='%s',delimiter=',')

