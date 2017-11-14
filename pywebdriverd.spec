# -*- mode: python -*-

block_cipher = None


a = Analysis(['pywebdriverd'],
             pathex=['C:\\flo\\pywebdriver'],
             binaries=[],
             datas=[('config/config.ini', 'config')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += Tree('pywebdriver/templates', prefix='templates')
a.datas += Tree('pywebdriver/translations', prefix='translations')
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pywebdriverd',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
