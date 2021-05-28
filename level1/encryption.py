

def solution(s): 
    decrypted = [
        chr(ord('z')-(ord(c)-ord('a'))) 
        if ord('a')<=ord(c) and ord(c)<=ord('z') 
        else c 
        for c in s
    ]
    return "".join(decrypted)

print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))

