# https://school.programmers.co.kr/learn/courses/30/lessons/17685
class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0


def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        node.prefix_count += 1


def count_prefixes(root, word):
    node = root
    count = 0
    for char in word:
        if char in node.children:
            node = node.children[char]
            count += 1
            if node.prefix_count == 1:
                break
        else:
            break
    return count


def solution(words):
    answer = 0
    root = TrieNode()
    for word in words:
        insert_word(root, word)
    for word in words:
        answer += count_prefixes(root, word)
    return answer
