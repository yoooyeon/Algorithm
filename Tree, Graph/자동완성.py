# https://school.programmers.co.kr/learn/courses/30/lessons/17685
# TC 14, 19, 21, 22 실패
from collections import defaultdict


def solution(words):
    answer = 0
    prefix_counter_dict = defaultdict(int)
    for word in words:
        for i in range(len(word)):
            letter = word[:i + 1]
            if letter in prefix_counter_dict.keys():
                prefix_counter_dict[letter] += 1
            else:
                prefix_counter_dict[letter] = 1
    for word in words:
        for i in range(len(word)):
            letter = word[:i + 1]
            if prefix_counter_dict[letter] > 1:
                answer += 1
            else:
                answer += 1
                break

    return answer
