import re
filepath = 'assets/Q5.txt'

def question5_part1(filepath):
    with open(filepath, 'r') as f:
        joinlines = ''.join(f.readlines()).split('\n\n')
        num = [int(x) for x in re.findall('\d+',joinlines[0])]           

    location = []
    for n in num:
        for line in joinlines[1:]:
            convert_range = [[int(item) for item in re.findall('\d+',x)] for x in re.findall('\d+\s\d+\s\d+',line)]
            for ran in convert_range:
                if (n >= ran[1]) and ((n-ran[1]) <= ran[2]):
                    n = ran[0] + (n - ran[1])
                    break
        location.append(n)
    print(min(location))

question5_part1(filepath)