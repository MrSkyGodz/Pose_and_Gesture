RIGHT = "RIGHT"
LEFT = "LEFT"

def inside_convex_polygon(point, vertices):
    previous_side = None
    n_vertices = len(vertices)
    for n in range(n_vertices):
        a, b = vertices[n], vertices[(n+1)%n_vertices]
        affine_segment = v_sub(b, a)
        affine_point = v_sub(point, a)
        current_side = get_side(affine_segment, affine_point)
        if current_side is None:
            return False #outside or over an edge
        elif previous_side is None: #first segment
            previous_side = current_side
        elif previous_side != current_side:
            return False
    return True

def get_side(a, b):
    x = cosine_sign(a, b)
    if x < 0:
        return LEFT
    elif x > 0: 
        return RIGHT
    else:
        return None

def v_sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

def cosine_sign(a, b):
    return a[0]*b[1]-a[1]*b[0]

print(inside_convex_polygon((2,3),vertices=[(0,1),(0,0),(1,0),(1,1)]))    