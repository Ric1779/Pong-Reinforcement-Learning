import random

sample = random.sample([[1,1.1],[2,2.1],[3,3.1],[4,4.1],[5,5.1],[6,6.1]], 2)
print(sample)
w = tuple(zip(*sample))
print(w[1])