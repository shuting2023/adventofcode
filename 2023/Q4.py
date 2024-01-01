filepath = 'assets/Q4.txt'
import re

def day4(filepath):

    sum_point = 0
    win_cards = [] # (original_cards, number_of_win)
    copy_cards = [] 
    with open(filepath,'r') as f:
        for line in f.readlines():
            line = line.replace('\n','').split(':')
            card_num = int(re.findall('\d+',line[0])[0])
            num_lst = line[1].split('|')
            win_num = num_lst[0].strip().split(' ')
            num_on_hand = num_lst[1].split(' ')
            match_num = [num for num in num_on_hand if num in win_num and num != '']

            point = 0 if len(match_num) == 0 else 1 * 2 ** (len(match_num)-1)
            sum_point += point

            if len(match_num) > 0:
                win_cards.append((card_num, len(match_num)))

            copy_cards.append([card_num+x for x in range(0,len(match_num)+1)])

    copies = [x[1:] for x in copy_cards]
    
    while True:
        match_lst = []
        for num in copies:
            filter= [n for n in num if n in [x[0] for x in win_cards]]
            if len(filter) > 0:
                match_lst.append(filter)   
        if match_lst == []:
            break
        
        copies= match_lst

        keep_win = [[n+i for i in range(1, x[1]+1)] for num in copies for n in num for x in win_cards if n == x[0]]
        copies = keep_win
        copy_cards += keep_win

    sum_cards = 0
    for n in (copy_cards):
        sum_cards+= len(n)

    return sum_point,sum_cards

