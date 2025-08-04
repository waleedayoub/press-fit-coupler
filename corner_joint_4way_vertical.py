"""
Generate a 4-way vertical corner joint (Z+, Z-, X-, Y-) for 16 mm ID steel tubing.
This creates a vertical hub with upward, downward, leftward, and forward connectors.

Run:
    python corner_joint_4way_vertical.py    # writes corner_joint_4way_vertical.stl
"""

import numpy as np, math, pathlib
from common import cylinder, cube, write_ascii_stl, Vec, shift_facets

# -------- USER-TWEAKABLE PARAMETERS --------
RADIUS        = 8.078    # plug radius   (mm)
INSERT_LEN    = 25.0     # plug length   (mm)  
HUB_SIZE      = 18.0     # cube hub size (mm) - enlarged for 4-way strength
SEGMENTS      = 96       # circle resolution (>= 64 looks smooth)

# -------- BUILD GEOMETRY ----------
facets = cube(HUB_SIZE)
shift  = HUB_SIZE/2 + INSERT_LEN/2

# Create cylinders for Z+, Z-, X-, Y- directions
for axis, offset in [('z', np.array([0, 0, +shift])),   # Z+ (upward)
                     ('z', np.array([0, 0, -shift])),   # Z- (downward)
                     ('x', np.array([-shift, 0, 0])),   # X- (leftward)
                     ('y', np.array([0, +shift, 0]))]:  # Y+ (forward)
    cyl = cylinder(RADIUS, INSERT_LEN, axis, SEGMENTS)
    facets += shift_facets(cyl, offset)

# -------- EXPORT ----------
outfile = pathlib.Path(__file__).with_suffix('.stl')
write_ascii_stl(facets, outfile, name='corner_4way_vertical')
print(f'Wrote {outfile}')