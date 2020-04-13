# https://www.hackerrank.com/contests/math-495r-strings/challenges/no-prefix-set/submissions/code/1319608037

trie = {}
def add_word(word, node):
    ''' Updates trie by adding a word '''
    if not word:
        node['count'] = node.get('count', 0) + 1
        return
    if word[0] not in node:
        node[word[0]] = {}
    add_word(word[1:], node[word[0]])

def has_substring(word, node):
    ''' Returns boolean for if substring is in trie or has substring in trie'''
    if 'count' in node:
        return True
    if not word:
        return True
    if word[0] not in node:
        return False
    return has_substring(word[1:], node[word[0]])

n = int(input())
is_good = True
for _ in range(n):
    string = input()
    if has_substring(string, trie):
        print('BAD SET')
        print(string)
        is_good = False
        break
    add_word(string, trie)
if is_good:
    print('GOOD SET')
