"""
Generate a heavy-duty 3-way corner (X,Y,Z) with enlarged hub (18 mm) + 25 mm plugs.
"""

import numpy as np, math, pathlib
from common import cylinder, cube, write_ascii_stl, Vec, shift_facets

RADIUS, INSERT_LEN, HUB_SIZE, SEGS = 8.078, 25.0, 18.0, 96
facets = cube(HUB_SIZE)
shift  = HUB_SIZE/2 + INSERT_LEN/2

for axis, d in [('x',Vec(shift,0,0)),
                ('y',Vec(0,shift,0)),
                ('z',Vec(0,0,shift))]:
    facets += shift_facets(cylinder(RADIUS, INSERT_LEN, axis, SEGS), d)

outfile = pathlib.Path(__file__).with_suffix('.stl')
write_ascii_stl(facets, outfile, 'corner_3way')
print(f'Wrote {outfile}')