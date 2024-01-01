filepath = 'assets/Q6.txt'
import re

def question6(filepath):
    f = open(filepath,'r')
    lines = f.readlines()
    lst = [[int(y) for y in re.findall('\d+',x)] for x in lines]
    race_lst = [x for x in zip(lst[0],lst[1])]

    multiply = 1
    for race in race_lst:
        count = 0
        (time,distance) = race
        for t in range(time + 1):
            result = (time - t)*t 
            if result > distance:
                count += 1
        multiply *= count

    print('part1:',multiply)
    
    update_lst = [[int(y.replace(' ','')) for y in re.findall('\d.+\d',x)] for x in lines]
    # use (quadrtic) equation to calculate the time when its result = distance
    a, b, c = 1, -update_lst[0][0], update_lst[1][0]
    print('part2:',int((-b +(b**2 - 4*a*c)**0.5)/2*a) - int((-b - (b**2 - 4*a*c)**0.5)/2*a))
    