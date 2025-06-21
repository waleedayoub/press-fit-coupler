# 3-D Printed Garden-Stake Couplers

This folder holds **parametric Python generators** that write ASCII STL
files for a set of press-fit connectors that work with  
*16 mm-ID × 1 mm-wall* hollow steel dowels (8.078 mm plug radius).

| File | Shape | Default params |
|------|-------|----------------|
| `pressfit_coupler.py` | Straight sleeve (two arms) | R = 8.078 mm, L = 50 mm |
| `cross_joint.py` | 4-way lattice “+” | R = 8.078 mm, L = 25 mm, hub = 12 mm |
| `elbow_joint_90.py` | 90 ° elbow | same |
| `joint_45deg.py` | 45 ° connector | same |
| `corner_joint_3way.py` | 3-way corner (X,Y,Z) | hub = **18 mm** for extra strength |

All scripts import **`common.py`** for shared geometry helpers.

## How to export an STL

```bash
python cross_joint.py        # writes cross_joint.stl
python elbow_joint_90.py     # writes elbow_joint_90.stl