import math
def dist(p1, p2):
    s = 0
    for i in range(len(p1)):
        s += (p1[i]-p2[i])**2
    return math.sqrt(s)

def closest_distance(points):
    points.sort()
    return closest_points(points)

def closest_points(points):
    if len(points) == 1:
        return float('inf')
    elif len(points) == 2:
        return dist(*points)
    mid_index = len(points) // 2
    # current min distance is smallest of subdistances
    current_min = min(closest_points(points[:mid_index]), closest_points(points[mid_index:]))
    # but it's now possible that the current smallest distance is being split
    # up
    mid_x = points[mid_index][0]
    # find indexes for within current_min of mid_x
    min_index, max_index = mid_index, mid_index
    while points[min_index][0] > mid_x - current_min:
        min_index += -1
        if min_index == 0:
            break
    while points[max_index][0] < mid_x + current_min:
        max_index += 1
        if max_index == len(points) - 1:
            break
    # make sure this checks all appropriate pairs
    for i in range(min_index, max_index+1):
        for j in range(i+1, max_index+1):
            current_min = min(current_min, dist(points[i], points[j]))
    return current_min

# p = [(0, 1), (1, 1), (2, 1), (1, 1.3), (3, 1), (.5, 1)]
# p = [(1, 1), (1, 1), (1, 1), (1, 1.3), (1, 1), (1, 1)]
# p = [(1, 1, 1), (4, 5, 6), (10, 3, 9)]
# p = [(1, 0), (1, 1), (0, 3), (1.5, 0)]
# print(sort_closest_points(p))
# p = [(5, 3), (6, 10), (4, 7), (1, 3)]
