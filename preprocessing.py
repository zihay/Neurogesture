import datetime
result = []
with open('data/bicycles_script&gestures11082018v4.txt') as f:
    content = f.readlines()
    base = datetime.datetime.strptime('00:00:00:00', '%H:%M:%S:%f')
    for line in content:
        line = line.split()
        t = line[0]
        start = line[2]
        time = datetime.datetime.strptime(start, '%H:%M:%S:%f')
        time = time-base
        time = time.seconds
        ges = line[6]
        result.append([time,ges])

result = result[:145]
