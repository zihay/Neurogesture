import datetime
import numpy as np

result = []
time = 0
with open('data/bicycles_script&gestures.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.split()
        t_start = int(line[1])//1000
        t_end = int(line[3])//1000
        t_len = t_end - t_start
        t_start = int(t_start)
        t_end = int(t_end)
        ges = line[6]
        while time < t_start:
            result.append('None')
            time+=1
        if t_len > 1.5:
            while time <= t_end:
                result.append(ges)
                time+=1
        else:
            result.append(ges)
            time+=1

ges_seq = result

pose_seq = []
with open('data/headposebi.csv') as f:
    lines = f.readlines()
    pose_seq = [line.strip() for line in lines]

merged =[]
for i in range(len(pose_seq)):
    if i < len(ges_seq):
        merged.append([pose_seq[i],ges_seq[i]])
    else:
        merged.append([pose_seq[i],'None'])

merged = np.array(merged)
np.savetxt("data/bi.csv", merged,fmt='%s')

result = []
time = 0
with open('data/perspectives_script&gestures.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.split()
        t_start = int(line[1])/1000
        t_end = int(line[2])/1000
        t_len = t_end - t_start
        t_start = int(t_start)
        t_end = int(t_end)
        ges = line[4]
        
        while time < t_start:
            result.append('None')
            time+=1
        if t_len > 1.5:
            while time <= t_end:
                result.append(ges)
                time+=1
        else:
            result.append(ges)
            time+=1

ges_seq = result

pose_seq = []
with open('data/headposeps.csv') as f:
    lines = f.readlines()
    pose_seq = [line.strip() for line in lines]

merged =[]
for i in range(len(pose_seq)):
    if i < len(ges_seq):
        merged.append([pose_seq[i],ges_seq[i]])
    else:
        merged.append([pose_seq[i],'None'])

merged = np.array(merged)
np.savetxt("data/ps.csv", merged,fmt='%s')


result = []
time = 0
with open('data/tarmac_script&gestures.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        t_start = int(line[1])/1000
        t_end = int(line[2])/1000
        t_len = t_end - t_start
        t_start = int(t_start)
        t_end = int(t_end)
        ges = line[4]
        while time < t_start:
            result.append('None')
            time+=1
        if t_len > 1.5:
            while time <= t_end:
                result.append(ges)
                time+=1
        else:
            result.append(ges)
            time+=1
ges_seq = result

pose_seq = []
with open('data/headposejk.csv') as f:
    lines = f.readlines()
    pose_seq = [line.strip() for line in lines]

merged =[]
for i in range(len(pose_seq)):
    if i < len(ges_seq):
        merged.append([pose_seq[i],ges_seq[i]])
    else:
        merged.append([pose_seq[i],'None'])

merged = np.array(merged)
np.savetxt("data/ta.csv", merged,fmt='%s')
