# PyInstaller spec: 아이콘 클릭으로 실행되는 단일 .exe 빌드
# 빌드: pyinstaller match_bom_top_bot.spec
# 결과: dist/BOM_TOP_BOT_Match.exe (이 파일만 복사해도 실행 가능)

# 아이콘을 쓰려면 프로젝트 폴더에 icon.ico를 두고 아래 주석을 해제하세요.
# icon_path = 'icon.ico'

a = Analysis(
    ['match_bom_top_bot.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
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
    name='BOM_TOP_BOT_Match',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # GUI만 표시, 검은 창 숨김
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='icon.ico',  # icon.ico 있으면 주석 해제
)
