# https://www.hackerrank.com/contests/math-495r-strings/challenges/contacts/submissions/code/1319607945

#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#
def contacts(queries):
    #
    # Write your code here.
    #
    trie = {}
    def add_word(word, node):
        ''' Updates trie by adding a word '''
        if not word:
            node['count'] = node.get('count', 0) + 1
            return
        if word[0] not in node:
            node[word[0]] = {}
        node['count'] = node.get('count', 0) + 1
        add_word(word[1:], node[word[0]])

    def count_words_start_with(substr, node):
        if not substr:
            return node.get('count', 0)
        if substr[0] not in node:
            return 0
        else:
            return count_words_start_with(substr[1:], node[substr[0]])

    outputs = []
    for query_type, name in queries:
        if query_type == 'add':
            add_word(name, trie)
        else:
            outputs.append(count_words_start_with(name, trie))

    return outputs



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


