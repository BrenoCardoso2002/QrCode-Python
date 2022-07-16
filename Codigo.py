import pyqrcode

link = "https://github.com/BrenoCardoso2002"

url = pyqrcode.create(link)

url.png('QrCode.png', scale=6)
