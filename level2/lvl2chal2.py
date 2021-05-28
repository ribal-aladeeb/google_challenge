from itertools import combinations

def solution(l):
    digits = sorted(l)
    target = []
    target_found = False

    for size in reversed(range(len(digits)+1)):
        if target_found:
            break

        def sortbysum(x): return x[1]

        comb = sorted([(c, sum(c)) for c in combinations(digits, size)], key=sortbysum, reverse=True)
        for combi, summ in comb:
            if summ % 3 == 0:
                target = combi
                target_found = True
                break

    largest = 0
    for exponent, coefficient in list(enumerate(target)):
        largest += coefficient * 10**exponent

    return largest


print(solution([3, 1, 4, 1, 5, 9]))
