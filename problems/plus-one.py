# https://leetcode.com/problems/plus-one/

digits = [1, 2, 3]
number = 0

for i in range(len(digits)):
    number += digits[i] * pow(10, len(digits) - i - 1)

number += 1
print(list(map(int, str(number))))

# -----