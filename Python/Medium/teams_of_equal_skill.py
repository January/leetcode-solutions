from typing import List

def dividePlayers(skill: List[int]) -> int:
    skill = sorted(skill)
    teams = []
    idx_start = 0
    idx_end = len(skill) - 1
    skill_level = skill[idx_start] + skill[idx_end]
    while(idx_start < idx_end):
        if(skill[idx_start] + skill[idx_end] != skill_level):
            return -1
        teams.append([skill[idx_start], skill[idx_end]])
        idx_start += 1
        idx_end -= 1
    chemistry = 0
    for team in teams:
        chemistry = chemistry + (team[0] * team[1])
    return chemistry


print(dividePlayers([3,2,5,1,3,4]))