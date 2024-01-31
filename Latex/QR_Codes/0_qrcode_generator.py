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

#Simple Ones
make_qrcode(qr_path+'QR_FeedTheMachine.png','https://drive.google.com/file/d/1Db6Ug0zLC6MYR0MDvbHU-q7UPug2lBHZ/view?usp=sharing',177)
make_qrcode(qr_path+'QR_SixteenTons_Chords.png','https://drive.google.com/file/d/1Umn86kdy6vKL7eu00424nV5WImphKJd6/view?usp=sharing',177)
make_qrcode(qr_path+'QR_HitTheRoadJack_Chords.png','https://drive.google.com/file/d/1_DVB0jdnRM9bB043iI_6aLIJ1hE3N0GM/view?usp=sharing',177)
make_qrcode(qr_path+'QR_OverTheRainbow_Chords.png','https://drive.google.com/file/d/1SXx1NqfWU1IdkkgBVRZP13PF4S6gko7s/view?usp=sharing',177)

#QuadroNuevo
#Die Reise nach Batumi
make_qrcode(qr_path+'QR_DieReiseNachBatumi_Bass.png','https://drive.google.com/file/d/1iSPA3IWUr3DmcvPvOctcOn4WfdtGQP4Z/view?usp=sharing',177)
make_qrcode(qr_path+'QR_DieReiseNachBatumi_Bb.png','https://drive.google.com/file/d/1rASvsrUgx3EBAj1N7LMI1qmXL2UYrubA/view?usp=sharing',177)
make_qrcode(qr_path+'QR_DieReiseNachBatumi_C.png','https://drive.google.com/file/d/1D_k33fDc33COZpwks44NaWvmHYAaPVT6/view?usp=sharing',177)
make_qrcode(qr_path+'QR_DieReiseNachBatumi_Eb.png','https://drive.google.com/file/d/1tpFxzmsTi53R2wHkUVC1OTuY7By3ak0C/view?usp=sharing',177)
make_qrcode(qr_path+'QR_DieReiseNachBatumi_F.png','https://drive.google.com/file/d/1-MLL2wg1osBzP2BaQFoCK1E5Jd_CgVrL/view?usp=sharing',177)
#GuivanniTranquillo
make_qrcode(qr_path+'QR_Giovanni_C.png','https://drive.google.com/file/d/1hkG54EgBcGDzLP4YKOpTGujYhhCZ0EWp/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Giovanni_Bb.png','https://drive.google.com/file/d/1Wn0209d814Ri0VOJyZlCMGyY8qXDxqBG/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Giovanni_Eb.png','https://drive.google.com/file/d/1QjIGCt3kNdb_phTWbco1vt-CXWf-wkKO/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Giovanni_Guitar.png','https://drive.google.com/file/d/1WeABTaSMxqlkYZVZSXkP8XICyvWqJ4Se/view?usp=sharing',177)
#Miserlou
make_qrcode(qr_path+'QR_Miserlou_Guitar.png','https://drive.google.com/file/d/1H6C4imIAFR5RDEAvFUR_seTwaDMfQhJe/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Miserlou_Bass.png','https://drive.google.com/file/d/1WGed6tFyTwMy8WtXOr7eB71EPMcmDOPV/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Miserlou_Bb.png','https://drive.google.com/file/d/1MhCpruL0cBYIy997bOSDp7rx90e9D28t/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Miserlou_Eb.png','https://drive.google.com/file/d/1_poakHOK-kTEjhrTHTzZtVFLQFt2HW0m/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Miserlou_Accordion.png','https://drive.google.com/file/d/1r6LNl-CmLw2LltPrg16bazdWPUmVQDP4/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Miserlou_C.png','https://drive.google.com/file/d/1lipl-Ak1Ie3_m1F-BV99DX8v8aNfx-dr/view?usp=sharing',177)
#Mohn
make_qrcode(qr_path+'QR_Mohn_AltSax.png','https://drive.google.com/file/d/1FYYsz12cOjk8kFyqCJ9ibBfKXE_m-i9E/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Mohn_Klar_2_B.png','https://drive.google.com/file/d/1t8hEQhKvrV-V4PSbIWbAQMSOg3BdOu6Y/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Mohn_Klar_1_B.png','https://drive.google.com/file/d/1FKO-u3B5_NqeZrsrdV26nOAiBBeYrLYl/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Mohn_Klavier.png','https://drive.google.com/file/d/1bycAD2f8wYfU0EuVWYc3qwjrG_y0SiHB/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Mohn_TenSax_2.png','https://drive.google.com/file/d/1xaw-oQiuNXWcXwX3eJS8xPMewCeF5H9x/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Mohn_TenSax_1.png','https://drive.google.com/file/d/1MXJHmco-EpWZN3GGu6LBI31jbya3BxaL/view?usp=sharing',177)


#Blues
make_qrcode(qr_path+'QR_12BarBlues.png','https://drive.google.com/file/d/1OHr9iwjNYFbsxZHoa1RS-AfROFuDm8Ch/view?usp=sharing',177)

#Rock songs
make_qrcode(qr_path+'QR_SultansOfSwing_BassChords.png','https://drive.google.com/file/d/14Mgmnunz_iVf0pWnBqPTu4IfZM3BnELL/view?usp=sharing',177)

#Movie and Games
make_qrcode(qr_path+'QR_LuxAeterna_CheatSheet.png','https://drive.google.com/file/d/1AvHzKg3lPEnnRlelcVWPcTGUGytP3JMC/view?usp=sharing',177)
make_qrcode(qr_path+'QR_LuxAeterna_Chords.png','https://drive.google.com/file/d/1spoS4tFDuOX45NCh1EDfrDmjujJ_5gaF/view?usp=sharing',177)


make_qrcode(qr_path+'QR_SpotifyPlaylist.png','https://open.spotify.com/playlist/29o5CLQWelLBBaHMstmTTg?si=cf957ec2a51848a2',177)
