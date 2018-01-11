import inspect
#print(inspect.getsource(read_grid_ints))

def show_contents(filename):
    fstream = open(filename)
    for line in fstream.readlines():
        print(line)

show_contents('small_grid_ints.txt')

def read_grid_ints():
    fstream = open('small_grid_ints.txt')
    R,C = [int(x) for x in fstream.readline().strip().split()]
    grid = [[int(x) for x in fstream.readline().strip().split()] for x in range(R)]
    return grid

def read_grid_chars():
    fstream = open('small_grid_chars.txt')
    R,C = [int(x) for x in fstream.readline().strip().split()]
    grid = [fstream.readline().strip().split() for x in range(R)]
    return grid

def read_grid_strs():
    fstream = open('small_grid_str.txt')
    R,C = [int(x) for x in fstream.readline().strip().split()]
    grid = [fstream.readline().strip() for x in range(R)]
    #grid[i][j] is now accessible...but what if you try and change grid[i][j]?
    return grid
read_grid_ints()

def check_bounds(i,j,R,C):
    """Returns the coords for each spot around grid[i][j], if its a valid spot"""
    spots = []
    for a in [-1,0,1]:
        for b in [-1,0,1]:
            if abs(a) + abs(b) == 2:
                continue
            if a == b == 0:
                continue
            if a + i < 0 or a + i >= R:
                continue
            elif b + j < 0 or b + j >= C:
                continue
            else:
                spots.append((a+i,b+j))
    return spots

def print_grid(grid,i=None,j=None,i2=None,j2=None):
    for a,row in enumerate(grid):
        for b,char in enumerate(row):
            if a == i and b == j:
                print('\x1b[1;37;41m' + str(char) + '\x1b[0m', sep=" ", end=" ")
            elif a == i2 and b == j2:
                print('\x1b[3;30;44m' + str(char) + '\x1b[0m', sep=" ", end=" ")
            else:
                print(char, end=" ")
        print(end='\n')
    c = input("\nPress Enter to Iterate:")

def iterate_grid(grid,R,C):
    for i in range(R):
        for j in range(C):
            print_grid(grid,i,j)

            avail_spots = check_bounds(i,j,R,C)
            possible_peak = True
            for a,b in avail_spots:
                print_grid(grid,i,j,a,b)
                if grid[a][b] == 'X':
                    print("This spot being a peak means that it WAS greater than current spot before we changed it, moving ahead")
                    possible_peak = False
                    break
                elif grid[a][b] >= grid[i][j]:
                    print("{} is larger than or equal to our current spot: {}, moving ahead".format(grid[a][b], grid[i][j]))
                    possible_peak = False
                    break
                else:
                    pass
            if possible_peak is True:
                print("{} was larger than all other spots, it was a peak!".format(grid[i][j]))
                grid[i][j] = 'X'
                print_grid(grid,i,j)
    print_grid(grid)
