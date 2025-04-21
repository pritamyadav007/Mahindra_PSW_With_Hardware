# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_data_files

project_root = os.path.abspath('.')

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        (os.path.join(project_root, 'templates'), 'templates'),
        (os.path.join(project_root, 'static'), 'static'),
    ],
    hiddenimports=[
        'jinja2.ext',
        'pyvisa.resources.serial',
        'pyvisa_py',
        'zeroconf',
        'serial.tools.list_ports',
                # ✅ correct import name for backend
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PSW_Controller',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(project_root, 'icon.ico')  # ✅ Absolute path to avoid FileNotFoundError
)
