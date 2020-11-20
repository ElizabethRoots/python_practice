# find lesser value between two numbers
def find_min(x, y):
    if x < y:
        min_xy = x
    else:
        min_xy = y
    print(min_xy)
    return min_xy


# test values of x, y
x = 3
y = 4
min_xy = find_min(x, y)

# test values of a, b
a = 12.3
b = 13.7
min_ab = find_min(a, b)

# test values of w, z
w = -3.9
z = -4.7
min_wz = find_min(w, z)

# find max value between two inputs


def find_max(x, y):
    if x > y:
        max_xy = x
    else:
        max_xy = y
    print(max_xy)
    return max_xy


# test values of x, y / reusing the x, y values
max_xy = find_max(x, y)
