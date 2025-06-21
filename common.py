"""
Geometry primitives + simple STL writer shared by all generator scripts.
"""
import numpy as np, math, pathlib, typing as T

Vec = np.ndarray

def cylinder(r: float, L: float, axis: str, seg: int = 64) -> list[list[Vec]]:
    th = np.linspace(0, 2*math.pi, seg, endpoint=False)
    if axis == 'x':
        p0 = np.column_stack([np.full_like(th,-L/2), r*np.cos(th), r*np.sin(th)])
        p1 = np.column_stack([np.full_like(th, L/2), r*np.cos(th), r*np.sin(th)])
    elif axis == 'y':
        p0 = np.column_stack([r*np.cos(th), np.full_like(th,-L/2), r*np.sin(th)])
        p1 = np.column_stack([r*np.cos(th), np.full_like(th, L/2), r*np.sin(th)])
    else:
        p0 = np.column_stack([r*np.cos(th), r*np.sin(th), np.full_like(th,-L/2)])
        p1 = np.column_stack([r*np.cos(th), r*np.sin(th), np.full_like(th, L/2)])

    facets: list[list[Vec]] = []
    n = seg
    for i in range(n):
        j = (i+1)%n
        facets += [[p0[i], p0[j], p1[i]],
                   [p1[i], p0[j], p1[j]]]
    cb, ct = p0.mean(0), p1.mean(0)
    for i in range(n):
        j = (i+1)%n
        facets += [[cb, p0[j], p0[i]],
                   [ct, p1[i], p1[j]]]
    return facets

def cube(a: float) -> list[list[Vec]]:
    h = a/2
    v = [(-h,-h,-h),( h,-h,-h),( h, h,-h),(-h, h,-h),
         (-h,-h, h),( h,-h, h),( h, h, h),(-h, h, h)]
    q = [(0,1,2,3),(4,5,6,7),(0,1,5,4),
         (1,2,6,5),(2,3,7,6),(3,0,4,7)]
    f=[]
    for a,b,c,d in q:
        f += [[v[a],v[b],v[c]],[v[a],v[c],v[d]]]
    return f

def write_ascii_stl(facets: list[list[Vec]], path: pathlib.Path, name='part'):
    with path.open('w') as f:
        f.write(f'solid {name}\n')
        for tri in facets:
            n = np.cross(tri[1]-tri[0], tri[2]-tri[0])
            n /= (np.linalg.norm(n) or 1.0)
            f.write(f'  facet normal {n[0]} {n[1]} {n[2]}\n')
            f.write('    outer loop\n')
            for v in tri:
                f.write(f'      vertex {v[0]} {v[1]} {v[2]}\n')
            f.write('    endloop\n  endfacet\n')
        f.write(f'endsolid {name}\n')

def shift_facets(facets: list[list[Vec]], vec: Vec, M: np.ndarray | None = None):
    """Translate then optionally rotate a list of triangles."""
    if M is None: M = np.eye(3)
    shifted=[]
    for tri in facets:
        shifted.append([(M @ v) + vec for v in tri])
    return shifted

class Mat4:
    @staticmethod
    def rotation_z(deg: float):
        a = math.radians(deg); c,s = math.cos(a), math.sin(a)
        return np.array([[c,-s,0.0],[s,c,0.0],[0.0,0.0,1.0]])