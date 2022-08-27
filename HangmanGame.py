import random

with open('sowpods.txt', 'r') as sowpods:
    lines = sowpods.readlines()
    rand_int = random.randint(0, len(lines))

    print(lines[rand_int])
