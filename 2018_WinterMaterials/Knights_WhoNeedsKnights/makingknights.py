import numpy as np

def solve_knights(A,B,n=8):
	"""Given the starting position of two bishops, find and print the minimum number of moves"""
	row_A,col_A = A // n, A % n
	row_B,col_B = B // n, B % n
	#print(row_A,col_A)
	#print(row_B,col_B)
	d_row = abs(row_B - row_A)
	d_col = abs(col_B - col_A)
	
	if (d_row % 2) != (d_col % 2):
		return -1
	else:
		if d_row == d_col:
			return 1
		else:
			return 2
			
def make_testcases(T,name):
	"""Make a test case with T rows"""
	fstream = open("input{}.txt".format(name), 'x')
	out1 = str(T) + "\n"
	out2 = ""
	all_bishops = []
	all_sols = []
	for _ in range(T):
		bishops = np.random.choice(list(range(64)), size=2, replace=False)
		all_bishops.append(bishops)
		solution = solve_knights(bishops[0], bishops[1])
		all_sols.append(solution)

	for bish,sol in zip(all_bishops, all_sols):
		out1 += str(bish[0]) + " " + str(bish[1]) + "\n"
		out2 += str(sol)
		out1 = out1.strip() + "\n"
		out2 = out2.strip() + "\n"
	fstream.write(out1.strip())
	fstream.close()

	fstream = open("output{}.txt".format(name), 'x')
	fstream.write(out2.strip())
	fstream.close()

# Make 10 test cases
for names in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]:
	make_testcases(100,names)
	break