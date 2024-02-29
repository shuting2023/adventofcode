import re
import math
def f():
    f = open('assets/day3.txt')
    lines = [line.replace('\n','') for line in f.readlines()]

    num_lst = [] #line_index, start, end, number
    sym_lst = [] #line_index, range_start, range_end
    for index, line in enumerate(lines):
        num_lst += [(index, x.start(),x.end()-1, int(x.group())) for x in re.finditer('\d+', line)]
        sym_lst += [(index, x.start()-1,x.end()) for x in re.finditer('\W',line) if x.group() != '.']
    
    Q1_lst =[]
    Q2_lst = []
    for sym in sym_lst: # iterate sym_lst, check around, extract num. If the number has been added into result lst, del it
        li, rast,raen = sym
        gear_lst = []
        for num in num_lst: 
            lj,st,en,n =num
            if li == 0: # no need to look up, only same line and below
                if  li <= lj <= li + 1 and st <= raen and en >= rast:
                        gear_lst.append(n)
            else:
                if li - 1 <= lj <= li + 1 and st <= raen and en >= rast:
                        gear_lst.append(n)
        Q1_lst += gear_lst
        
        # for Q2, for each sym, if we append exactly two numbers, then it's gear 
        if len(gear_lst) == 2:
            # print('gear',gear_lst)
            Q2_lst.append(math.prod(gear_lst))
                        
    

    print('result1',sum(Q1_lst))
    print('result2',sum(Q2_lst))

f()