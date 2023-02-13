import pyqrcode
import png
from pyqrcode import QRCode

name = input('''Enter if you want a qr code of google or discord: ''').lower()
link = ""

if name == "google":
  link = "www.google.com"
elif name == "discord":
  link = "www.discord.com"
else:
  print("you have inserted an invalid statement")

url = pyqrcode.create(link)

url.png("mycode.png",scale = 10)