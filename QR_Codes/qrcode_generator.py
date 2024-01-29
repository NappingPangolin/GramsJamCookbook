import qrcode

def make_qrcode(filename, input, qr_size):
    if qr_size > 0:
        qr = qrcode.QRCode(box_size = qr_size)
    else:
        qr = qrcode.QRCode()
    qr.add_data(input)
    img = qr.make_image()
    img.save(filename)


make_qrcode('QR_FeedTheMachine.png','https://tabs.ultimate-guitar.com/tab/poor-mans-poison/feed-the-machine-chords-3349439',177)
