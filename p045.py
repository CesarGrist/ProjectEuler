import math

found = 0
pent_val = 0
pent_n = 166

while found == 0:
    pent_val = (pent_n*(3*pent_n-1))/2
    tester = int(math.floor(math.sqrt(2*pent_val)))

    if int(tester*(tester+1)/2) == int(pent_val):
        found = int(pent_val)

    pent_n += 1
print(found) 