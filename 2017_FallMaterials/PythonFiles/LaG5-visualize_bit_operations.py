# Talk first about binary operations:
def show_binary_operation(a,b, op):
    bin_a = [x for x in bin(a).lstrip('0b')]
    bin_b = [y for y in bin(b).lstrip('0b')]
    if op == '&':
        op = ' &'
        result = a & b
    elif op == '^':
        result = a ^ b
        op = ' ^'
    elif op == '|':
        op = ' |'
        result = a | b
    elif op == '<<':
        result = a << b
    elif op == '>>':
        result = a >> b
    result_l = [z for z in bin(result).lstrip('0b')]
    while len(bin_a) < len(bin_b) or len(bin_a) < len(result_l):
        bin_a.insert(0,'0')
    while len(bin_b) < len(bin_a) or len(bin_b) < len(result_l):
        bin_b.insert(0,'0')
    print("  ", *bin_a, "= {}".format(a), sep=" ")
    print(str(op), *bin_b, "= {}".format(b), sep= " ")
    print('--'*(2 + len(bin(a))), sep=" ")
    while len(result_l) < len(bin_b) or len(result_l) < len(bin_a):
        result_l.insert(0,'0')
    print("  ", *result_l, "= {}".format(result), sep=" ")

show_binary_operation(13, 15, '^')
