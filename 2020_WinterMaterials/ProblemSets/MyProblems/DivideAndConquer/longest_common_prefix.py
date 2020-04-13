import pdb
def longest_common_prefix(strings):
    def recur(start, end):
        if end-start == 1:
            return strings[start]
        elif end-start == 2:
            i = 0
            while strings[start][i] == strings[end][i]:
                i += 1
                if i == len(strings[start]) or i == len(strings[end]):
                    break
            return i
        mid = (end-start) // 2
        return min(recur(start, mid), recur(mid, end))
    return strings[0][:recur(0,len(strings))

# def longest_common_prefix(strings):
#     if len(strings) == 1:
#         return strings[0]
#     elif len(strings) == 2:
#         i = 0
#         while strings[0][i] == strings[1][i]:
#             i += 1
#             if i == len(strings[0]) or i == len(strings[1]):
#                 break
#         return strings[0][:i]
#     mid = len(strings) // 2
#     return longest_common_prefix([longest_common_prefix(strings[:mid]),
#                                   longest_common_prefix(strings[mid:])])

def naive(strings):
    i = 0
    c = strings[0][i]
    while all([c == st[i] for st in strings]):
        i += 1
        print([i == len(st) for st in strings])
        if any([i == len(st) for st in strings]):
            break
        c = strings[0][i]
    return strings[0][:i]
