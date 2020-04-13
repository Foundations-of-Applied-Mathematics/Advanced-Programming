import numpy as np
from closest_points import closest_distance
n = 10
k = 2500
print('Generating points')
points = 1000 * np.random.rand(k, n)
points = np.round(points, 3)

in_file = open('closest_in.txt', 'w')
out_file = open('closest_out.txt', 'w')

print('Writing to input file')
print(k, file=in_file)
for row in points:
    row_str = [str(i) for i in row.tolist()]
    print(' '.join(row_str), file=in_file)

print('Finding solution')
print(closest_distance(points.tolist()), file=out_file)
print('Done!')
