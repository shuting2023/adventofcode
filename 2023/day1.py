import re

filepath = 'assets/day1.txt'
f = open(filepath, 'r')
lines = f.readlines()

cali = [int(re.findall('\d',line)[0]+re.findall('\d',line)[-1]) for line in lines]

num_str = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']
num_tuple = [x for x in enumerate(num_str)]
num_dict = dict((y,x) for x,y in num_tuple)

pattern = '|'.join(num_str) 

new_cali = []
for line in lines:
    num_join = ''
    for x in [re.findall('(?=('+pattern+'|\d))',line)[0],re.findall('(?=('+pattern+'|\d))',line)[-1]]:
        if x in num_dict.keys():
            num_join += str(num_dict[x])
        else:
            num_join += (x)
    new_cali.append(int(''.join(num_join)))

print('part1:', sum(cali),'part2:', sum(new_cali))
