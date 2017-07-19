# -*- mode: python -*-

block_cipher = None


a = Analysis(['MetCalculator.py'],
             pathex=['/Users/mbaker/Documents/Projects/PycharmProjects/metcalculator'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='MetCalculator',
          debug=False,
          strip=None,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='MetCalculator.app',
             icon=None,
             bundle_identifier=None)
