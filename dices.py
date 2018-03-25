import random
min = 1
max = 6

crit = 0

for i in range(1000):

    a = random.randint(min, max)
    b = random.randint(min, max)
    c = random.randint(min, max)

    if a == b == c:
        print('critical hit!')
        crit += 1

print(crit)
