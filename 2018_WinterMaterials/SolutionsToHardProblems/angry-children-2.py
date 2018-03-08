# This solves all test cases for https://www.hackerrank.com/challenges/angry-children-2/problem
# The naive solution for this problem is too slow.
# We can instead build a "sliding window" that is capable of calculating the "unfairness" at each level in relation to what the unfairness was at the previous level.
# Key ideas involve recognizing that consecutive elements of a sorted list will certainly minimize unfairness
# The second idea is that once the list is sorted, |X_i - X_j| is known to be either X_i - X_j or X_j - X_i (depending on if you sort ascending or descending). Once the absolute value signs are gone, you can combine like terms to find a closed form solution for unfairness at any stage. It is O(K) to find unfairness at any state, which would be [N-K]*K total operations. Still too slow.
# The last idea is recognizing that each window only changes by 4 values, the new values being added, and the "middle" terms that get bumped in/out. So instead of spending K operations to calculate unfairness at each step, you can calculate initial unfairness (K operations), and then only do ~4 operations at each successive step to find the new unfairness.

N = int(input())
K = int(input())
candies = []
for _ in range(N):
    candies.append(int(input()))
scandies = sorted(candies)
this_error = 0
midsum = 0
for i in range(0,K-1):
    midsum += -2*scandies[i]
    this_error += (i-K+1)*scandies[i]
    this_error += (K-1-i)*scandies[K-1-i]
min_error = this_error
for i in range(1,N-K+1):
    midsum -= scandies[i-1]*-2
    midsum += scandies[i+K-2]*-2
    this_error += (K-1)*scandies[i+K-1]
    this_error += (K-1)*scandies[i-1]
    this_error += midsum
    if this_error < min_error:
        min_error = this_error
print(min_error)