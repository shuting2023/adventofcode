import re
filepath = 'assets/Q2_2023.txt'

def Q2_p1(filepath):
    dic = {'red':12, 'green':13, 'blue':14}

    impossible = 0
    total = 0
    with open(filepath,'r') as file:
        for line in file.readlines():
            verify = 0
            total += int(re.findall('(\d+):',line)[0])
            for key in dic:
                num_ball = [int(x) for x in re.findall('(\d+)\s'+key,line)]       
                [verify:= verify + 1 for n in num_ball if n > dic[key]]
                if verify > 0:
                    impossible += int(re.findall('(\d+):',line)[0])
                    break
    return total - impossible

def Q2_p2(filepath):
    color_lst = ['blue', 'green', 'red']
    result= 0
    with open(filepath,'r') as file:
        for line in file.readlines():
            power = 1
            for c in color_lst:
                color = max([int(x) for x in re.findall('(\d+)\s'+c,line)])
                power *= color
            result += power 
    return result 

print(Q2_p1(filepath))
print(Q2_p2(filepath))