# https://leetcode.com/problems/find-words-containing-character/

words = ["abc","bcd","aaaa","cbc"]
x = "a"
indices = []

for i in range(len(words)):
    if x in words[i]:
        indices.append(i)

print(indices)