import random

cj1 = [random.randint(1, 20) for _ in range(10)]
cj2 = [random.randint(1, 20) for _ in range(10)]

union = set(cj1) | set(cj2)
intersection = set(cj1) & set(cj2)
dif = set(cj1) - set(cj2)
subconjunto = set(cj1) <= set(cj2)

print(cj1)
print(cj2)
print(union)
print(intersection)
print(dif)
print(subconjunto)
