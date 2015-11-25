# -*- mode: python -*-
a = Analysis(['wxpy.py'],
             pathex=['E:\\Python\\Webpy\\src'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='wxpy.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='images\\icon.ico')
