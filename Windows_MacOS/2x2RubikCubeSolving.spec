# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['../main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('../instant_solution.db', '.'),
        ('../animations/*', 'animations')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='2x2RubikCubeSolving',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='../imgs/2x2RubikCube.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='2x2RubikCubeSolving',
    icon='../imgs/2x2RubikCube.ico',
)
app = BUNDLE(
    coll,
    name='2x2RubikCubeSolving.app',
    icon='../imgs/2x2RubikCube.ico',
    bundle_identifier=None,
)
