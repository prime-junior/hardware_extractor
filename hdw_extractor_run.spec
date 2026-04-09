from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

import sys
sys.setrecursionlimit(sys.getrecursionlimit() * 5)

block_cipher = None

a = Analysis(
    ['hdw_extractor_run.py'], 
    pathex=['.'],
    binaries=[],
    datas=[
        # ALTAIR (para gráficos Streamlit)
        (
            r".venv\Lib\site-packages\altair\vegalite\v6\schema",
            r".\altair\vegalite\v6\schema"
        ),
        # STREAMLIT (arquivos estáticos)
        (
            r".venv\Lib\site-packages\streamlit\static",
            r".\streamlit\static"
        ),
        
        # MAIN FILE (CHANGE THE NAME HERE)
        ('main.py', '.'),
        # UTILS MODULE
        ('utils.py', '.'),
        
        # STREAMLIT SETTINGS
        ('.streamlit/config.toml', '.streamlit')
    ] + copy_metadata('streamlit') + copy_metadata('pandas') + copy_metadata('gspread'),
    hiddenimports=[
        'streamlit', 
        'pandas',
        'gspread',
        'streamlit.web.cli',
        'streamlit.runtime.scriptrunner.magic_funcs',
        'streamlit.runtime.caching.cache_data_api',
        'streamlit.runtime.legacy_caching',
        'importlib.metadata',
        'importlib_metadata'
    ],
    hookspath=['./hooks'],                  
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='hdw_extractor_run',                       # MUDE O NOME AQUI
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)