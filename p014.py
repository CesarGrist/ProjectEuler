chain_len = 0
chain_num = 0

for x in range(2, 1000000):
    seed = x
    length = 0
    
    while seed != 1:
        length += 1
        if seed%2 == 0:
            seed = seed/2
        else:
            seed = 3*seed + 1

    
    if length >= chain_len:
        chain_len = length
        chain_num = x

print(chain_num)
