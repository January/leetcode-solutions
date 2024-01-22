from typing import List
def findArray(pref: List[int]) -> List[int]:
    if(len(pref) <= 1):
        return pref
    answer = [pref[0]]
    for i in range(1, len(pref)):
        answer.append(pref[i - 1] ^ pref[i])
    return answer

print(findArray([5,2,0,3,1]))