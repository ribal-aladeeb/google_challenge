
def generous(lambs):
    '''
    The requirement: 

    "A henchman will revolt if the person who ranks immediately above them gets
    more than double the number of LAMBs they do." 

    implies a power function of 2**x as the upper bound with 0<=x until the sum
    of all 2**xi is <= the number of lambs.
    '''
    distributed = 0
    henchmen = []
    while distributed < lambs:
        i = len(henchmen)
        if distributed + 2**i <= lambs:
            henchmen.append(2**i)
        distributed += 2**i
    return henchmen


def stingy(lambs):
    '''
    The requirement:

    "A henchman will revolt if the amount of LAMBs given to their next two
    subordinates combined is more than the number of LAMBs they get.  (Note that
    the two most junior henchmen won't have two subordinates, so this rule
    doesn't apply to them.  The 2nd most junior henchman would require at least
    as many LAMBs as the most junior henchman.)"

    implies a distribution of lambs following the fibonacci sequence as the lower bound
    '''
    distributed = 0
    henchmen = []
    while distributed < lambs:
        i = len(henchmen)
        if i == 0 or i == 1:
            henchmen.append(1)
            distributed += 1
        else:
            sum_of_2subs = henchmen[-1] + henchmen[-2]
            if distributed + sum_of_2subs <= lambs:
                henchmen.append(sum_of_2subs)
            distributed += sum_of_2subs

    return henchmen


def solution(lambs):
    g, s = generous(lambs), stingy(lambs)
    print(g)
    print(s)
    return len(s) - len(g) 


if __name__ == '__main__':
    correct_input = False
    while not correct_input:
        try:
            lambs = int(input('Enter the number of lambs:'))
            if 1 <= lambs <= 10e9:
                correct_input = True
        except ValueError:
            print("Please enter an interger between 1 and 1 Billion")
    
    print(solution(lambs))
