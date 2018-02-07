# This solves the custom problem Knights? who needs knights.
# Available in the vat: https://www.hackerrank.com/contests/the-vat/challenges/knights-who-needs-knights/problem
# This problem can be solved by recognizing first that it will never take bishops more than 2 moves to reach each other
# Regardless of their starting position (if they are even possible)
# So the only need to check if the d_row and d_col are the same, if so they are on the same diagonal, if not it will take two
# moves for them to reach each other.

def solve_knights(A,B,n=8):
	"""Given the starting position of two bishops, find and print the minimum number of moves"""
	row_A,col_A = A // n, A % n
	row_B,col_B = B // n, B % n
	d_row = abs(row_B - row_A)
	d_col = abs(col_B - col_A)
	
	if (d_row % 2) != (d_col % 2):
		return -1
	else:
		if d_row == d_col:
			return 1
		else:
			return 2
			
for _ in range(int(input())):
    A, B = [int(x) for x in input().split()]
    print(solve_knights(A,B))