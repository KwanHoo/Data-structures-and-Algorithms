# 삼총사

from itertools import combinations, permutations

def solution(number):
    answer = 0

    combi = list(combinations(number, 3))
    for i in range(len(combi)):
        # print(combi[i])
        if sum(list(combi[i])) == 0:
            answer += 1

    return answer