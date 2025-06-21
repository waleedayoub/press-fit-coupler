# ==== Defaults ====
DEFAULTS = {
    'tube_ID_mm': 16.0,
    'clearance_mm': 0.20,
    'insert_len_mm': 50.0,
    'rim_thk_mm': 2.0,
    'rim_OD_mm': 19.0
}

def ask_float(ui, title, prompt, default):
    """
    Helper that wraps ui.inputBox and returns a float.
    Cancelling the dialog aborts the whole script cleanly.
    """
    ret = ui.inputBox(title, prompt, str(default))
    if ret[2]:  # user pressed Cancel
        raise RuntimeError('User cancelled')
    try:
        return float(ret[0])
    except ValueError:
        raise RuntimeError(f'“{ret[0]}” is not a number')

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct

        # ---- 1. Ask user for parameters ----
        p = {}
        p['tube_ID_mm']   = ask_float(ui, 'Tube ID',      'Inner diameter of steel tube (mm):', DEFAULTS['tube_ID_mm'])
        p['clearance_mm'] = ask_float(ui, 'Clearance',     'Radial clearance for press-fit (mm):', DEFAULTS['clearance_mm'])
        p['insert_len_mm']= ask_float(ui, 'Insert length', 'Insertion length per side (mm):', DEFAULTS['insert_len_mm'])
        p['rim_thk_mm']   = ask_float(ui, 'Rim thickness', 'Stop-rim thickness (mm):', DEFAULTS['rim_thk_mm'])
        p['rim_OD_mm']    = ask_float(ui, 'Rim OD',        'Outer diameter of stop-rim (mm):', DEFAULTS['rim_OD_mm'])

        # ---- 2. Calc derived sizes ----
        insert_OD = p['tube_ID_mm'] - p['clearance_mm']
        rim_OD    = p['rim_OD_mm']
        half_len  = p['insert_len_mm']

        # ---- 3. Build component ----
        # (everything from here down stays exactly the same)
