import math

def polar_angle(p0, p1):
    """
    Returns the polar angle (in radians) of the point p1 relative to the point p0.
    """
    px, py = p1[0] - p0[0], p1[1] - p0[1]
    angle = math.atan2(py, px)
    return angle

def ccw(p1, p2, p3):
    """
    Returns the direction of the cross product of the vectors (p2 - p1) and (p3 - p1).
    A positive value indicates a counterclockwise turn, negative indicates a clockwise turn,
    and zero indicates that the points are collinear.
    """
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def graham_scan(points):
    """
    Implements the Graham Scan algorithm for finding the convex hull of a set of points.
    
    Args:
        points: A list of points, where each point is a tuple (x, y).
    
    Returns:
        A list of points representing the vertices of the convex hull in counterclockwise order.
    """
    # Step 1: Find the point with the minimum y-coordinate (or leftmost point in case of a tie)
    p0 = min(points, key=lambda p: (p[1], p[0]))
    
    # Step 2: Sort the remaining points by polar angle around p0
    sorted_points = sorted(points[:], key=lambda p: (polar_angle(p0, p), -math.hypot(p[0] - p0[0], p[1] - p0[1])))
    
    # Step 3: Initialize an empty stack
    stack = []
    
    # Step 4 & 5: Push the first two points onto the stack
    stack.append(sorted_points[0])
    stack.append(sorted_points[1])
    
    # Steps 6-10: Process the remaining points
    for i in range(2, len(sorted_points)):
        while len(stack) > 1 and ccw(stack[-2], stack[-1], sorted_points[i]) <= 0:
            stack.pop()
        stack.append(sorted_points[i])
    
    # Step 11: Return the stack
    return stack




# points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
# points = [(0,0),(7,0),(3,1),(5,2),(9,6),(3,3),(5,5),(1,4)] 
points = [(1,10),(1,4),(4,1),(4,5),(8,7)] 

# Find the convex hull using Graham Scan
convex_hull = graham_scan(points)

# Print the convex hull points
print("Convex Hull Points:")
for point in convex_hull:
    print(point)
    
    
###########################################################################

def polar_angle(p0, p1):
    px, py = p1[0]-p0[0], p1[1]-p0[1]
    angle = math.atan2(py, px)
    return angle

def ccw(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

def graham(points):
    p0 = min(points, key = lambda p: (p[1], p[0]))
    
    sorted_points = sorted(points[:], key = lambda p:(polar_angle(p0, p), -math.hypot(p[0]-p0[0], p[1]-p[1])))
    
    stack = []
    stack.append(sorted_points[0])
    stack.append(sorted_points[1])
    
    for i in range(2, len(sorted_points)):
        while len(stack)>1 and ccw(stack[-2], stack[-1], sorted_points[i]) <=0:
            stack.pop()
        
        stack.append(sorted_points[i])


    return stack

points = [(1,10),(1,4),(4,1),(4,5),(8,7)] 

convex_hull = graham(points)

# Print the convex hull points
print("Convex Hull Points:")
for point in convex_hull:
    print(point)