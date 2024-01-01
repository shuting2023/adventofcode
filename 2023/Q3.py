filepath = "assets/Q3.txt"
import re

def easy_index(line):
    symbol_front = [(d.group(),(d.span()[0]+1,d.span()[1])) for d in re.finditer('\W\d+',line) if '.' not in d.group()]
    symbol_back = [(d.group(),(d.span()[0],d.span()[1]-2)) for d in re.finditer('\d+\W',line) if '.' not in d.group()]
    digits_index = [x[1] for x in symbol_front] + [x[1] for x in symbol_back] 
    sum_lst = [x[0] for x in symbol_front] + [x[0] for x in symbol_back]

    all_digits =  [d.span() for d in re.finditer('\d+',line)]
    for e in digits_index:
        if e in all_digits:
            all_digits.remove(e)

    symbol_index = [d.span()[0] for d in re.finditer('\W',line) if d.group() not in ['.','\n']]
    range_symbol = [(e-1,e+1) for e in symbol_index]

    return sum_lst, all_digits, range_symbol

def adjacent_digits(dind,syrange,dind_line):
    removing_digit_lst = []
    sum_lst = []
    for num_ind in dind:
        for sym_ind in syrange:
            if (sym_ind[0] <= num_ind[0] <=sym_ind[1]) or (num_ind[1]-1>=sym_ind[0] and num_ind[1]-1<=sym_ind[1]):
                sum_lst.append(dind_line[num_ind[0]:num_ind[1]]) 
                removing_digit_lst.append(num_ind)
                
    return sum_lst, removing_digit_lst

def question3_part1(filepath):
    line_sum = []
    total = 0
    with open(filepath,'r') as file:
        prev = None
        curr = next(file)
        for line in file.readlines():
            # special case for line 1
            line = line.replace("\n",'')
            prev = curr        
            curr = line

            try: 
                dind_prev = dind_curr
            except:
                dind_prev = easy_index(prev)[1]
            
            _, _, syrange_prev = easy_index(prev)

            sum_easy_curr, dind_curr, syrange_curr = easy_index(curr)

            # prev no need removing_digit_lst
            sum_lst_prev, _ = adjacent_digits(dind_prev,syrange_curr,prev)

            sum_lst_curr, removing_dind = adjacent_digits(dind_curr,syrange_prev,curr)


            for e in removing_dind:
                if e in dind_curr:
                    dind_curr.remove(e)

            linesum = sum_easy_curr + sum_lst_prev + sum_lst_curr
            line_sum = [(int(re.findall('\d+',x)[0])) for x in linesum]
            total += sum(line_sum)
            

    return total

def question3_part2(filepath):
    with open(filepath,'r') as file:
        lines = [line.replace('\n','') for line in file.readlines()]

    num_postion = [] #(num, (line_index, num_start, num_end))
    star_position = [] #(line_index, star_start, star_end)
    for i,line in enumerate(lines):
        num_postion += [(int(d.group()),(i,d.start(),d.end()-1)) for d in re.finditer('\d+',line)]
        star_position += [(i,d.start()-1,d.end()) for d in re.finditer('\*',line)]
    
    gear_lst = []
    for lj,s_start,s_end in star_position:
        lst = []
        for num,(li, n_start, n_end)in num_postion:
            if lj in (li-1, li, li+1) and n_start <= s_end and n_end >= s_start:
                lst.append(num)
        if len(lst) == 2:
            gear_lst.append(lst)

    gear_ratio = [num1*num2 for num1,num2 in gear_lst]
    
    return sum(gear_ratio)
