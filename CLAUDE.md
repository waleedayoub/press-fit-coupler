# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a parametric 3D CAD library for generating press-fit couplers and joints for 16mm ID × 1mm wall hollow steel dowels. The system generates ASCII STL files for 3D printing garden stake connectors.

## Architecture & Structure

### Core Components
- **`common.py`**: Shared geometry primitives and STL writer functions. Contains the fundamental `cylinder()`, `cube()`, `write_ascii_stl()`, and `shift_facets()` functions used by all generators.
- **Generator Scripts**: Individual Python files that create specific connector types by combining primitives from `common.py`

### Standard Parameters
All generators use consistent parameters:
- **Plug radius**: 8.078 mm (calibrated for 16mm ID tubes)
- **Insert length**: 25mm (except straight coupler: 50mm)
- **Hub size**: 12mm (corner joint uses 18mm for strength)
- **Segments**: 64-96 for circle resolution

### Generator Patterns
Each generator follows the same structure:
1. Import geometry functions from `common.py`
2. Define USER-TWEAKABLE PARAMETERS section
3. Build geometry by combining `cube()` hub with `cylinder()` plugs using `shift_facets()`
4. Export using `write_ascii_stl()` with filename matching script name

## Common Development Commands

### Generate STL Files
```bash
python cross_joint.py                  # 4-way lattice "+" connector (±X, ±Y)
python elbow_joint_90.py               # 90° elbow joint
python joint_45deg.py                  # 45° angled connector
python corner_joint_3way.py            # 3-way corner (X+, Y+, Z+)
python corner_joint_4way_vertical.py   # 4-way vertical corner (Z+, Z-, X-, Y+)
python corner_joint_5way_vertical.py   # 5-way vertical corner (Z+, Z-, Y+, Y-, X-)
python corner_joint_6way_full.py       # 6-way full hub (Z+, Z-, Y+, Y-, X+, X-)
python pressfit_coupler.py             # Straight sleeve connector
```

### Testing Changes
Run individual generators to verify geometry modifications. Each script outputs an STL file with the same base name.

## Key Design Constraints
- All connectors designed for 16mm ID × 1mm wall steel tubing
- Press-fit tolerance built into 8.078mm plug radius
- Hub-and-spoke architecture: central cube with cylindrical plugs
- ASCII STL output for maximum compatibility

## File Modifications
When modifying generators:
- Adjust parameters in the USER-TWEAKABLE PARAMETERS section
- Maintain the hub + shifted cylinders pattern
- Preserve the consistent naming convention (script_name.stl output)
- Test geometry changes by running the generator and inspecting STL output