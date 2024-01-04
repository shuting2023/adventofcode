import re
filepath = 'assets/Q9.txt'

f = open(filepath,'r')
lines =f.readlines()

history  = [[int(x) for x in line.split(' ')] for line in lines]

last_n = []
for his in history:
    last_n.append(his[-1])
    diff = []
    while set(diff) != {0}:
        diff = [his[i]-his[i-1] for i in range(1,len(his))]
        last_n.append(diff[-1])
        his = diff 

print('part1:',sum(last_n))
        
num_lst = []
for his in history:
    first_n = [his[0]]
    diff = []
    while set(diff) != {0}:
        diff = [his[i]-his[i-1] for i in range(1,len(his))]
        first_n.append(diff[0])
        his = diff 
    first = first_n[::-1]

    beg = 0
    for n in first[1:]:
        output = n - beg
        beg = output
    num_lst.append(output)

print('part2:',sum(num_lst))

