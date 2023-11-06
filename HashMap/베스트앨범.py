from collections import defaultdict
def solution(genres, plays):
    answer = []
    acc = defaultdict(list)
    for i in range(len(genres)):
        if genres[i] in acc.keys():
            a,b = acc[genres[i]]
            b.append([plays[i],i])
            acc[genres[i]] = [a+plays[i],b]
        else:
            acc[genres[i]] = [plays[i],[[plays[i],i]]]
    acc = sorted(acc.values(),key  = lambda x:-x[0])
    for _,v in acc:
        v.sort(key = lambda x: (-x[0],x[1]))        
        for i in range(len(v)):
            answer.append(v[i][1])
            if i>=1:
                break
    return answer
