def solution(babbling):
    answer = []
    words = ["aya", "ye", "woo", "ma"]

    def check(bab, i, before):
        nonlocal answer
        if len(bab) == 0:
            answer.append(i)
            return
        if len(bab) < 2:
            return
        if i in answer: return
        if bab[:2] in words and bab[:2] != before:
            check(bab[2:], i, bab[:2])

        if len(bab) >= 3 and bab[:3] in words and bab[:3] != before:
            check(bab[3:], i, bab[:3])

    i = 0
    for bab in babbling:
        check(bab, i, '')
        i += 1
    return len(set(answer))


# print(solution(["aya", "yee", "u"]))
# print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
