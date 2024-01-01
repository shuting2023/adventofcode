import re
def open_file(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    return lines

def question_one_p1(filepath):
    num_lst = []
    for line in open_file(filepath):
        try:
            num = re.search('[0-9]+\S+[0-9]+',line).group(0)
        except:
            num = re.search('[0-9]+',line).group(0)
        num = num[0] + num[-1]
        num_lst.append(int(num))
            
    return sum(num_lst)


def question_one_p2(filepath):
    num_dic = {'one':'1', 'two':'2', 'three':'3',
               'four': '4', 'five': '5', 'six':'6',
               'seven': '7','eight': '8', 'nine':'9', 'zero':'0'}
    pattern = '(?=(one|two|three|four|five|six|seven|eight|nine|zero))' # overlapping 'oneight' situation

    num_lst = []
    for line in open_file(filepath):
        head = ''
        tail = ''

        head = re.findall('[0-9]|[a-z]+[0-9]',line)[0]
        try:
            num_str = re.findall(pattern, head)[0]
            head = num_dic[num_str]
        except:
            head = head[-1]

        tail = re.findall('[0-9][a-z]+|[0-9]',line)[-1]
        try:
            num_str = re.findall(pattern,tail)[-1]
            tail = num_dic[num_str]
        except:
            tail = tail[0]


        num = int(head + tail)
        num_lst.append(num)

    return sum(num_lst)

filepath = 'assets/Q1_2023.txt'