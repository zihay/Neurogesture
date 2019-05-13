import numpy as np
from util import *
import networkx as nx
from hmmlearn.hmm import MultinomialHMM
from sklearn.preprocessing import LabelEncoder

data = np.genfromtxt('data/out.csv',delimiter='\t', dtype=np.str)
data = data[:,1]
pose = data[data!='']
pose = pose.tolist()

# merge duplicate adjancent state
pose = [p for i,p in enumerate(pose) if i==0 or p!=pose[i-1]]


transitions = list(zip([pose[i] for i in range(0, len(pose)-1)],
                 [pose[i] for i in range(1, len(pose))]))

#%%

state = list(set(pose))
pose_fre = frequency(pose)
transition_fre = transition_prop(pose)
draw_fre(pose_fre)
print('')
draw_transition(state,transition_fre)

# state = LabelEncoder().fit_transform(state)
# # a=[0,1,0,1,0,1]
# a=np.atleast_2d(state).T
# hmm = MultinomialHMM(n_components=2)
# # state = np.array(state)
# # state = np.reshape(state,(1,-1)).tolist()

# hmm.fit(a)
# s = hmm.score(a)
# print(s)