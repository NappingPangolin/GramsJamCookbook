import qrcode
import os

def make_qrcode(filename, input, qr_size):
    if qr_size > 0:
        qr = qrcode.QRCode(box_size = qr_size)
    else:
        qr = qrcode.QRCode()
    qr.add_data(input)
    img = qr.make_image()
    img.save(filename)

qr_path = os.path.dirname(__file__) +'/'

#Simple Classics
make_qrcode(qr_path+'QR_FeedTheMachine.png','https://drive.google.com/file/d/1Db6Ug0zLC6MYR0MDvbHU-q7UPug2lBHZ/view?usp=sharing',177)
make_qrcode(qr_path+'QR_SixteenTons_Chords.png','https://drive.google.com/file/d/1Umn86kdy6vKL7eu00424nV5WImphKJd6/view?usp=sharing',177)
make_qrcode(qr_path+'QR_HitTheRoadJack_Chords.png','https://drive.google.com/file/d/1_DVB0jdnRM9bB043iI_6aLIJ1hE3N0GM/view?usp=sharing',177)

#Blues
make_qrcode(qr_path+'QR_12BarBlues.png','https://drive.google.com/file/d/1OHr9iwjNYFbsxZHoa1RS-AfROFuDm8Ch/view?usp=sharing',177)

#Rock songs
make_qrcode(qr_path+'QR_SultansOfSwing_BassChords.png','https://drive.google.com/file/d/14Mgmnunz_iVf0pWnBqPTu4IfZM3BnELL/view?usp=sharing',177)

#Movie and Games
make_qrcode(qr_path+'QR_LuxAeterna_CheatSheet.png','https://drive.google.com/file/d/1AvHzKg3lPEnnRlelcVWPcTGUGytP3JMC/view?usp=sharing',177)
make_qrcode(qr_path+'QR_LuxAeterna_Chords.png','https://drive.google.com/file/d/1spoS4tFDuOX45NCh1EDfrDmjujJ_5gaF/view?usp=sharing',177)

