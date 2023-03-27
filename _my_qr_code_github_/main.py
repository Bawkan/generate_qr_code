import qrcode

img = qrcode.make(
    'https://github.com/Bawkan'
)
img.save('myQRcode.png')
