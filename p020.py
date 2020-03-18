import math

n = math.factorial(100)
n_str = str(n)
digit_sum = 0

for i in range(0, len(n_str)):
   digit_sum += int(n_str[i])

print(digit_sum)
