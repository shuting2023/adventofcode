import re
filepath = 'assets/day2.txt'

f = open(filepath,'r')
lines = f.readlines()

sum_possible = 0
sum_power = 0
for line in lines:
    line = line.split(':')
    game,subsets = line
    game_num = int(re.findall('\d+',game)[0])

    if max([int(x) for x in re.findall('(\d+)\sred',subsets)]) <= 12 and max([int(x) for x in re.findall('(\d+)\sgreen',subsets)]) <= 13 and max([int(x) for x in re.findall('(\d+)\sblue',subsets)]) <= 14:
        sum_possible += game_num

    power = max([int(x) for x in re.findall('(\d+)\sred',subsets)]) * max([int(x) for x in re.findall('(\d+)\sgreen',subsets)])* max([int(x) for x in re.findall('(\d+)\sblue',subsets)])
    sum_power += power


print('part1:',sum_possible)
print('part2:',sum_power)
