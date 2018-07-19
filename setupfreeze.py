from bbfreeze import Freezer

freezer = Freezer(distdir='dist',includes=('qrcode', 'tkinter', 'xlrd', 'textwrap', 'pybel', 'PIL', 'subprocess',))
freezer.addScript('gui.py', gui_only=True)
freezer()
