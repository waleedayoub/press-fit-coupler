"""
Generate a 45 ° lattice connector (+X arm, +45 ° XY arm).
"""

import numpy as np, math, pathlib
from common import cylinder, cube, write_ascii_stl, Mat4, Vec, shift_facets

RADIUS, INSERT_LEN, HUB_SIZE, SEGS = 8.078, 25.0, 12.0, 96
facets = cube(HUB_SIZE)
shift  = HUB_SIZE/2 + INSERT_LEN/2

# +X arm
facets += shift_facets(cylinder(RADIUS, INSERT_LEN, 'x', SEGS), Vec(shift, 0, 0))

# 45 ° arm
rot45 = Mat4.rotation_z(45)
vec45 = Vec.from_angle_deg(45) * shift
facets += shift_facets(cylinder(RADIUS, INSERT_LEN, 'x', SEGS), rot45 @ vec45, rot45)

outfile = pathlib.Path(__file__).with_suffix('.stl')
write_ascii_stl(facets, outfile, 'joint_45deg')
print(f'Wrote {outfile}')