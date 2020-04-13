from max_subarray import max_subarray, naive
import numpy as np
import time
in_file = open('max_in.txt', 'w')
out_file = open('max_out.txt', 'w')

arr = np.random.randint(-1000, 1000, size=500000).tolist()
# arr = np.array([1 for _ in range(10000)])
str_arr = [str(a) for a in arr]
print(' '.join(str_arr), file=in_file)

start = time.time()
sol = max_subarray(arr)
print(sol)
print(sol, file=out_file)
print(time.time() - start)

# start = time.time()
# print(naive(arr))
# print(time.time() - start)

