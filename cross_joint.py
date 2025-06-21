"""
Generate a 4-way cross coupler (plugs ±X, ±Y) for 16 mm ID steel tubing.
Default plug radius matches your calibrated 8.078 mm.

Run:
    python cross_joint.py         # writes cross_joint.stl in same folder
"""

import numpy as np, math, pathlib
from common import cylinder, cube, write_ascii_stl, Vec, shift_facets

# -------- USER-TWEAKABLE PARAMETERS --------
RADIUS        = 8.078    # plug radius   (mm)
INSERT_LEN    = 25.0     # plug length   (mm)
HUB_SIZE      = 12.0     # cube hub size (mm) – increase for more strength
SEGMENTS      = 96       # circle resolution (>= 64 looks smooth)

# -------- BUILD GEOMETRY ----------
facets = cube(HUB_SIZE)
shift  = HUB_SIZE/2 + INSERT_LEN/2

for axis, dx, dy in [('x',+shift,0), ('x',-shift,0),
                     ('y',0,+shift), ('y',0,-shift)]:
    cyl = cylinder(RADIUS, INSERT_LEN, axis, SEGMENTS)
    facets += shift_facets(cyl, Vec(dx, dy, 0))

# -------- EXPORT ----------
outfile = pathlib.Path(__file__).with_suffix('.stl')
write_ascii_stl(facets, outfile, name='cross_joint')
print(f'Wrote {outfile}')