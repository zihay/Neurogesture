from typing import Dict, List, Tuple
from typing import List, Tuple
from tabulate import tabulate
import sys
Frequency = List[Tuple[any, int]]
import itertools

def normalize(array):
    return [float(e)/(sum(array)+sys.float_info.epsilon) for e in array]

def transition_prop(states):
    transitions = list(zip([states[i] for i in range(0, len(states)-1)],
                 [states[i] for i in range(1, len(states))]))
    state = set(states)
    transition_matrix = [normalize([transitions.count((i,j)) for j in state]) for i in state]
    trans_prop = {(i,j):0.0 for i in state for j in state}
    
    for i,first in enumerate(state):
        for j,second in enumerate(state):
            trans_prop[(first,second)] = transition_matrix[i][j]
    return trans_prop

def second_order_transition_count(states, state):
    transitions = list(zip([states[i] for i in range(0, len(states)-2)],
                 [states[i] for i in range(1, len(states)-1)],
                 [states[i] for i in range(2, len(states))]))
    second_order_state = list(itertools.product(state, state))
    trans_count = {(s,s1):transitions.count((s[0],s[1],s1)) for s in second_order_state for s1 in state}
    return trans_count

def second_order_transition_prop(states, state):
    transitions = list(zip([states[i] for i in range(0, len(states)-2)],
                 [states[i] for i in range(1, len(states)-1)],
                 [states[i] for i in range(2, len(states))]))
    # state = set(states)
    second_order_state = list(itertools.product(state, state))
    transition_matrix = [normalize([transitions.count((s[0], s[1], s1)) for s1 in state]) for s in second_order_state]
    trans_prop = {(i,j):0.0 for i in second_order_state for j in state}
    for i,first in enumerate(second_order_state):
        for j,second in enumerate(state):
            trans_prop[(first,second)] = transition_matrix[i][j]
    return trans_prop

def frequency1(data: List[any])-> Frequency:
    unique = set(data)
    count = [data.count(u) for u in unique]
    fre = [float(c)/sum(count) for c in count]
    return {u:f for u,f in zip(unique,fre)}

def frequency(state,data: List[any])-> Frequency:
    unique = state
    count = [data.count(u) for u in unique]
    fre = [float(c)/(sum(count)+sys.float_info.epsilon) for c in count]
    return {u:f for u,f in zip(unique,fre)}


def draw_fre(frequency):
    header = ['']+[str(k) for k in frequency]
    row = ['frequency'] + [frequency[k] for k in frequency]
    print(tabulate([row], headers=header))


def draw_transition(state, transition):
    transition_matrix = [[transition[(i, j)] if (i, j) in transition else 0 for j in state]
                         for i in state]
    header = [''] + [str(s) for s in state]
    rows = [[str(state[i])] + row for i, row in enumerate(transition_matrix)]
    
    print(tabulate(rows, headers=header))

def get_transition_table(state, transition):
    transition_matrix = [[transition[(i, j)] if (i, j) in transition else 0 for j in state]
                         for i in state]
    header = [''] + [str(s) for s in state]
    rows = [[str(state[i])] + row for i, row in enumerate(transition_matrix)]
    return [header]+rows

if __name__ == "__main__":
    pass