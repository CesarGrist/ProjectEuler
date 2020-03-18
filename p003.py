import math

x = 600851475143

for i in range(int(math.sqrt(x)), 1, -1):
    if x%i == 0:
        x = i

print(x)
