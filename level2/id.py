

def convert_base10(number: str, base: int) -> int:
    '''
    convert the number to base 10. Assuming that 2<=base<=10
    '''
    if base == 10:
        return int(number)

    base10 = 0
    for i in range(len(number)):
        coeff = number[i]
        power = len(number) - 1 - i
        base10 += int(coeff) * (base ** power)

    return base10


def revert_base(number10: int, base: int) -> str:
    '''
    Convert a number base10 to the argument base. Assume 2<=base<=10
    '''
    current = number10
    reverted = ''
    i = 0
    powers = [base**i]
    while powers[-1] <= current:
        i += 1
        powers.append(base**i)

    powers = powers[:-1]
    for p in reversed(powers):
        divisor = current//p
        reverted += str(divisor)
        current -= divisor*p

    return reverted


def solution(n, b):
    k = len(n)
    z = n
    i = 0

    indices = {}
    found_cycle = False
    marker = ''

    while not found_cycle:

        y = ''.join(sorted(z))
        x = ''.join(list(reversed(y)))
        zprime = convert_base10(x, b) - convert_base10(y, b)
        z = revert_base(zprime, b)
        z = '0'*(k-len(z)) + z          #pad with 0s

        idx = indices.get(z, [])
        idx.append(i)
        indices[z] = idx
        if len(indices[z]) > 1:
            found_cycle = True
            marker = z
        i += 1

    cycle_size = indices[marker][1] - indices[marker][0]

    return cycle_size

print(solution('210022', 3))

