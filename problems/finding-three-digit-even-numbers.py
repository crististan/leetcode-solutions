from itertools import permutations

digits = [2,1,3,0]
results = set()

for perm in permutations(digits, 3):
    if perm[0] == 0:
        continue

    num = int(''.join(map(str, perm)))
    if num % 2 == 0: results.add(num)

print(sorted(results))