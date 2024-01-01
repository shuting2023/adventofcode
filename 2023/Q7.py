filepath = 'assets/Q7.txt'

import re

def question7(filepath):
    f = open(filepath, 'r')
    lines = f.readlines()
    lst = [re.findall('\w+',x) for x in lines]

    order_lst = [x for x in enumerate(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1])]
    
    part1_lst = []
    
    for x in lst:
        card,bid = x
        o_lst = []
        for c in card:
            for o,ca in order_lst:
                if c == ca:
                    o_lst.append(o)
        # o_lst = [o for o,ca in order_lst for c in card if c == ca] # if doing this way, it will sort the order automatically (which is not wanted)
        part1_lst.append([card,bid,sorted([card.count(c) for c in set(card)],reverse=True),o_lst])
    
    result = sorted(part1_lst, key = lambda c: (c[2],c[3]))
    result_lst = [(i+1)*int(x[1]) for i,x in enumerate(result)]
    print('part1:',sum(result_lst))


    update_order = [x for x in enumerate(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J'][::-1])]
    part2_lst = []
    for x in lst:
        card,bid = x
        o_lst = []
        for c in card:
            for o,ca in update_order:
                if c == ca:
                    o_lst.append(o)
        card_count = [0]
        if set(card) != {'J'}:
            for x in set(card):
                if x != 'J':
                    card_count.append(card.count(x))

        type_lst = [max(card_count) + card.count('J')]+ sorted([card.count(x) for x in set(card) if x != 'J'],reverse=True)[1:]
        part2_lst.append([card,bid,sorted(type_lst,reverse=True),o_lst])


    result = sorted(part2_lst, key = lambda c: (c[2],c[3]))


    re_lst = [(i+1)*int(x[1]) for i,x in enumerate(result)]
    print('part2:',sum(re_lst)) 



question7(filepath)