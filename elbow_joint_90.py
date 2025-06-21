"""
Generate a 90 ° elbow connector (+X, +Y arms).
"""

import numpy as np, math, pathlib
from common import cylinder, cube, write_ascii_stl, Vec, shift_facets

RADIUS     = 8.078
INSERT_LEN = 25.0
HUB_SIZE   = 12.0
SEGS       = 96

facets = cube(HUB_SIZE)
shift  = HUB_SIZE/2 + INSERT_LEN/2

facets += shift_facets(cylinder(RADIUS, INSERT_LEN, 'x', SEGS), Vec( shift, 0, 0))
facets += shift_facets(cylinder(RADIUS, INSERT_LEN, 'y', SEGS), Vec( 0, shift, 0))

outfile = pathlib.Path(__file__).with_suffix('.stl')
write_ascii_stl(facets, outfile, 'elbow_joint_90')
print(f'Wrote {outfile}')