# %%
import numpy as np

data = np.genfromtxt('data/text.txt', dtype=np.str)

gesture = ['beats', 'deictic', 'metaphoric', 'iconic']

data = data.tolist()

data = [d for d in data if d in gesture]

transitions = list(zip([data[i] for i in range(0, len(data)-1)],
                 [data[i] for i in range(1, len(data))]))

unique, counts = np.unique(data, return_counts=True)
counts = counts/sum(counts)

transition_set = set(transitions)

transition_count = [transitions.count(t) for t in transition_set]
transition_fre = [float(t)/len(transitions) for t in transition_count]


print(list(zip(list(transition_set),transition_fre)))

print(list(zip(unique, counts)))