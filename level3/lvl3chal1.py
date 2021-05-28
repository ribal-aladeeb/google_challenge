from math import factorial
from tqdm import tqdm


def cubesolution(l):
    triples = 0
    for i in tqdm(range(len(l)-2)):
        for j in range(i+1, len(l)-1):
            for k in range(j+1, len(l)):
                if l[k] % l[j] == 0 and l[j] % l[i] == 0:
                    triples += 1
    return triples


'''
The obvious cube solution is way too slow. It seems like some of the 5th
test case times out. Let's try to find something more interesting.
'''


def divides(divisor, dividend):
    return dividend >= divisor and dividend % divisor == 0


def old_solution(l):
    '''
    This solution should be in the order of NlogN.
    Uncomment the print statements to see the trace of the algo.
    '''
    triples = 0
    mapping = {}
    for index, value in enumerate(l):
        indices = mapping.get(value, [])
        indices.append(index)
        mapping[value] = indices

    for key in mapping:
        indices = mapping[key]
        if indices > 1:
            for i in range(1, len(indices)):
                l[i] = -1  # if this number appears already make it negative to filter in the comprehension.
        if len(indices) >= 3:
            n = len(indices)
            r = 3
            triples += factorial(n) / (factorial(n-r) * factorial(r))   # combinations without repitition of triples containing (key, key, key)

    '''
    Maybe removing the consecutive duplicates would reduce the worst case
    runtime to NlogN.
    '''

    for i in range(len(l)-2):                   # this i is the actual i in the input list
        if i < 1:
            continue
        dividends = [index+i+1 for (index, _) in enumerate(l[i+1:]) if l[i] > 0 and l[index+i+1] > 0 and divides(l[i], l[index+i+1])]
        # print(f'i: {i}, {dividends}')

        for pos, j in enumerate(dividends):     # j is the actual j, and pos is the position of j in dividends

            second_dividends = [index for index in dividends[pos+1:] if l[j] > 0 and l[index] > 0 and divides(l[j], l[index])]
            # for a given pair (i,j), second_dividends are all the possible k indices that make a triple
            # print(f'\tj: {j}, {second_dividends}')

            '''
            Now that duplicates have been remove, for each triple (i,j,k) we
            have to count the additional triples for which we removed
            duplicate values while still satisfying i < j < k
            '''

            for k in second_dividends:
                Is = mapping[l[i]]
                Js = mapping[l[j]]
                Ks = mapping[l[k]]
                for i_s in Is:
                    for js in [x for x in Js if x > i_s]:
                        triples += len([x for x in Ks if x > js])

    return triples


def dup_solution(l):  # so this doesnt seem to work

    triples = 0

    duplicates = {}
    offset = 1
    i = 0
    while i+offset < len(l):
        if l[i] == l[i+offset]:
            duplicates[i] = duplicates.get(i, [i]) + [i+offset]
            l[i+offset] = -1
            offset += 1
        else:
            i += 1
            offset = i+1

    for index in duplicates:
        indices = duplicates[index]
        if len(indices) >= 3:
            n = len(indices)
            r = 3
            triples += factorial(n) / (factorial(n-r)*factorial(r))
    print(duplicates)
    print(l)
    '''
    Now, consecutive duplicates should be removed so that
    l = [1, 1, 2, 3, 1, 5, 1, 1]
    becomes
    l = [1, -1, 2, 3, 1, 5, 1, -1]
    '''

    for i in range(len(l)-2):
        dividends = [
            index+i+1
            for index in range(len(l[i+1:]))
            if l[i] > 0 and l[index+i+1] > 0
            and divides(l[i], l[index+i+1])
        ]

        for pos, j in enumerate(dividends):     # j is the actual j, and pos is the position of j in dividends
            second_dividends = [
                index
                for index in dividends[pos+1:]
                if l[j] > 0 and l[index] > 0
                and divides(l[j], l[index])
            ]
            i_multiplier = len(duplicates[i])
            j_multiplier = len(duplicates[j])
            for k in second_dividends:
                triples += i_multiplier * j_multiplier * len(duplicates[k])

    return triples


def combinations_without_rep(n, r):
    '''
    Count the combinations of size r taken from n distinct objects without
    repitition.
    '''
    f = factorial
    return f(n) / (f(n-r)*f(r))


def unfinished_solution(l):
    triples = 0
    mapping = {}  # maps a value in the array to all the indices where that value exists
    for q in range(l):  # using q as the default iterator to differenciate from i (which has a meaning in this question's context)
        indices = mapping.get(l[q], [])
        indices.append(q)
        mapping[l[q]] = indices

    for element in mapping:
        '''First, any element present 3+ times can create its own triples'''
        if len(mapping[element]) >= 3:
            n = len(mapping[element])
            r = 3
            triples += combinations_without_rep(n, r)

        possible_j_elements = {el: indices for (el, indices) in mapping if divides(element, el)}


def solution(l):
    triples = 0
    for j in range(1, len(l)-1):
        possible_i = [i for i in range(0, j) if divides(l[i], l[j])]
        possible_k = [k for k in range(j+1, len(l)) if divides(l[j], l[k])]
        triples += len(possible_i) * len(possible_k)
    return triples


x = list(range(1,2000))
print(solution(x))
print(cubesolution(x))
