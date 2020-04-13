import math

# L2 dist for Rn
def dist(p1, p2):
    s = 0
    for i in range(len(p1)):
        s += (p1[i]-p2[i])**2
    return math.sqrt(s)

# sort points, then find closest points
def sort_closest_points(points):
    points.sort()
    return closest_points(points)

# recursive function
def closest_points(points):
    if len(points) == 1:
        return float('inf')
    elif len(points) == 2:
        return dist(*points)
    mid_index = len(points) // 2
    # current min distance is smallest of subdistances
    current_min = min(closest_points(points[:mid_index]), closest_points(points[mid_index:]))
    # but it's now possible that the current smallest distance is being split
    mid_x = points[mid_index][0]
    # find indexes for within current_min of mid_x
    min_index, max_index = mid_index, mid_index
    # find all points within current_min to mid on left
    while points[min_index][0] > mid_x - current_min:
        min_index += -1
        if min_index == 0:
            break
    # find all points within current_min to mid on right
    while points[max_index][0] < mid_x + current_min:
        max_index += 1
        if max_index == len(points) - 1:
            break
    # compare points in this neighborhood to see if there is closer distance
    for i in range(min_index, max_index+1):
        for j in range(i+1, max_index+1):
            current_min = min(current_min, dist(points[i], points[j]))
    return current_min

if __name__ == '__main__':
    points = []
    k = int(input())
    for _ in range(k):
        p = list(map(float, input().rstrip().split()))
        points.append(p)
    print(sort_closest_points(points))
