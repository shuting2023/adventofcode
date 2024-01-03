import re
import math 

filepath = 'assets/Q8.txt'

f = open(filepath,'r')
lines = f.readlines()

map = [0 if v == 'L' else 1 if v == 'R' else '' for v in lines[0]][:-1]
network = ''.join(lines[2:])
match = re.findall('(\w+A)\s=',network)
num_start = len(match)
# print(match)

# count = 0
# while match != 'ZZZ':
#     for n in range(len(map)):
#         navig = [x.split(', ') for x in re.findall(match +'\s\=\s\((.+)\)',network)]
#         stop = navig[0][map[n]]
#         match = stop
#         count += 1
# print('part1:',count)

count_lst = []
for str in match:
    count = 0
    end = False
    while end != True:
        for n in range(len(map)):
            navig = [x.split(', ') for x in re.findall(str +'\s\=\s\((.+)\)',network)]
            stop = navig[0][map[n]]
            str = stop
            count += 1
            if str[-1] == 'Z':
                end = True
    count_lst.append(count)

lcm = 1 
for num in count_lst:
    lcm = lcm*num//math.gcd(lcm,num)

print('part2:',lcm)