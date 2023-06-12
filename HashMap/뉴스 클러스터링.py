from collections import defaultdict
import math

def preprocess_string(string):
    string = string.upper()
    string = list(string)
    return string

def create_ngram_dict(string):
    ngram_dict = defaultdict(int)
    for i in range(len(string) - 1):
        ngram = string[i] + string[i + 1]
        if 'A' <= ngram[0] <= 'Z' and 'A' <= ngram[1] <= 'Z':
            ngram_dict[ngram] += 1
    return ngram_dict

def calculate_jaccard_similarity(dict1, dict2):
    intersection = 0
    for k, v in dict1.items():
        if k in dict2.keys():
            intersection += min(v, dict2[k])
    union = sum(dict1.values()) + sum(dict2.values()) - intersection
    if union == 0:
        return 65536
    answer = intersection / union
    return math.trunc(answer * 65536)

def solution(str1, str2):
    str1 = preprocess_string(str1)
    str2 = preprocess_string(str2)

    dict1 = create_ngram_dict(str1)
    dict2 = create_ngram_dict(str2)

    return calculate_jaccard_similarity(dict1, dict2)
