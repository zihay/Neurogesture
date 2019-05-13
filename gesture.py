import numpy as np
from util import *
import networkx as nx
# data = np.genfromtxt('data/text.txt', dtype=np.str)[:145]
data = np.genfromtxt('data/perspectives_script&gestures11082018v4.txt', dtype=np.str)
data = data.tolist()
gesture = ['beats', 'deictic', 'metaphoric', 'iconic']

state = list(set(data))
gesture_fre = frequency(data)
transition_fre = transition_prop(data)
draw_fre(gesture_fre)
print('')
draw_transition(state,transition_fre)


