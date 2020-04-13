
def gen(n):
    return generate_parens(n, "", n, n)

def generate_parens(n, s = "", lefts = None, rights = None):
    if lefts is None or rights is None:
        return generate_parens(n, s, lefts = n, rights = n)
   
    if lefts == 0 and rights == 0:
        return [s]

    ret = []
    if lefts > 0:
        ret += generate_parens(n, s + "(", lefts - 1, rights)

    if n - rights < n - lefts:
        ret += generate_parens(n, s + ")", lefts, rights - 1)

    return ret

print(len(gen(4)))
