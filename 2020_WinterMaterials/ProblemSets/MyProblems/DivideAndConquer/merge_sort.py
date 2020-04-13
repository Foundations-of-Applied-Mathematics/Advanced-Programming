import numpy as np
test_case = open('test.txt', 'w')
test_input = open('test_input.txt', 'w')

def merge_sort(l):
    print(l, file=test_case)
    if len(l) == 1:
        return l
    mid = len(l) // 2
    def stitch(l1, l2):
        new = []
        done = False
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                new.append(l1[i])
                i += 1
            else:
                new.append(l2[j])
                j += 1
        while i < len(l1):
            new.append(l1[i])
            i += 1
        while j < len(l2):
            new.append(l2[j])
            j += 1
        return new
    return stitch(merge_sort(l[:mid]), merge_sort(l[mid:]))


def print_list(l):
    temp = [str(i) for i in l]
    print(' '.join(temp), file = test_input)

l = np.random.randint(10000, size=10000).tolist()
print_list(l)
print(merge_sort(l), file=test_case)
print('done')
