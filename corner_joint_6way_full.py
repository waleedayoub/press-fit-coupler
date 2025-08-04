"""
Generate a 6-way full corner joint (Z+, Z-, Y+, Y-, X+, X-) for 16 mm ID steel tubing.
This creates a complete 3D hub with connectors in all six cardinal directions.

Run:
    python corner_joint_6way_full.py    # writes corner_joint_6way_full.stl
"""

import numpy as np, math, pathlib
from common import cylinder, cube, write_ascii_stl, Vec, shift_facets

# -------- USER-TWEAKABLE PARAMETERS --------
RADIUS        = 8.078    # plug radius   (mm)
INSERT_LEN    = 25.0     # plug length   (mm)  
HUB_SIZE      = 22.0     # cube hub size (mm) - enlarged for 6-way strength
SEGMENTS      = 96       # circle resolution (>= 64 looks smooth)

# -------- BUILD GEOMETRY ----------
facets = cube(HUB_SIZE)
shift  = HUB_SIZE/2 + INSERT_LEN/2

# Create cylinders for all six cardinal directions
for axis, offset in [('z', np.array([0, 0, +shift])),   # Z+ (upward)
                     ('z', np.array([0, 0, -shift])),   # Z- (downward)
                     ('y', np.array([0, +shift, 0])),   # Y+ (forward)
                     ('y', np.array([0, -shift, 0])),   # Y- (backward)
                     ('x', np.array([+shift, 0, 0])),   # X+ (rightward)
                     ('x', np.array([-shift, 0, 0]))]:  # X- (leftward)
    cyl = cylinder(RADIUS, INSERT_LEN, axis, SEGMENTS)
    facets += shift_facets(cyl, offset)

# -------- EXPORT ----------
outfile = pathlib.Path(__file__).with_suffix('.stl')
write_ascii_stl(facets, outfile, name='corner_6way_full')
print(f'Wrote {outfile}')