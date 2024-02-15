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
#HitTheRoadJack
make_qrcode(qr_path+'QR_HitTheRoadJack_Chords.png','https://drive.google.com/file/d/1_DVB0jdnRM9bB043iI_6aLIJ1hE3N0GM/view?usp=sharing',177)
make_qrcode(qr_path+'QR_HitTheRoadJack_Piano.png','https://drive.google.com/file/d/1EjQ24Ns8cO_YMZj0sXjmJdEExPuxKgfe/view?usp=sharing',177)
make_qrcode(qr_path+'QR_HitTheRoadJack_Bb.png','https://drive.google.com/file/d/1DlDMc2Ez0BVMABByr4j-6d2qF_yomMpJ/view?usp=sharing',177)
make_qrcode(qr_path+'QR_HitTheRoadJack_Eb.png','https://drive.google.com/file/d/1nXsma-5nFJoybw7rrgSSX6S2OgCxmNbd/view?usp=sharing',177)



#Pop
#Billie Jean
make_qrcode(qr_path+'QR_BillieJean_C.png','https://drive.google.com/file/d/1rDaPzEzP3Rv0SlOV0sjytDD_A0gnCRK3/view?usp=sharing',177)
make_qrcode(qr_path+'QR_BillieJean_Eb.png','https://drive.google.com/file/d/1652P_ydqHeLwL8bpmBjK258P50WBfyj6/view?usp=sharing',177)
make_qrcode(qr_path+'QR_BillieJean_Bb.png','https://drive.google.com/file/d/13w8zDBYhQnN0QGPTI-ZnAXbwQRi2Kjke/view?usp=sharing',177)
#FuerMichSollsRoteRosenRegnen
make_qrcode(qr_path+'QR_RoteRosenRegnen_C.png','https://drive.google.com/file/d/1USPjPHN5qE2BbEhuDVMcH0oZOgt7_hn7/view?usp=sharing',177)
make_qrcode(qr_path+'QR_RoteRosenRegnen_Bb.png','https://drive.google.com/file/d/1Fzi6QT2e78Y9HTl6tjKLdjYImgDMNxgh/view?usp=sharing',177)
make_qrcode(qr_path+'QR_RoteRosenRegnen_Eb.png','https://drive.google.com/file/d/1JBm830-YOsqzlykb7-GoCZs3grpMC6m0/view?usp=sharing',177)
#Over the Rainbow
make_qrcode(qr_path+'QR_OverTheRainbow_C.png','https://drive.google.com/file/d/1X1lVpF9FyxTtUqpCXFjjx1x3LmwioKdk/view?usp=sharing',177)
make_qrcode(qr_path+'QR_OverTheRainbow_Bb_Clar.png','https://drive.google.com/file/d/1tEPCe0QCipldWiNespmuZperSIXcM06W/view?usp=sharing',177)
make_qrcode(qr_path+'QR_OverTheRainbow_Bb_Trumpet.png','https://drive.google.com/file/d/1FdPv_AEZncQPWME1PjwnKliEiSq0WtqQ/view?usp=sharing',177)
make_qrcode(qr_path+'QR_OverTheRainbow_Eb.png','https://drive.google.com/file/d/1rigT586D1jy-CIs1u8deoEuTpjjHxAt9/view?usp=sharing',177)



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
#Yorkers Guitar
make_qrcode(qr_path+'QR_Yorkers_C.png','https://drive.google.com/file/d/1cpq13ie8mZ8jweh23KzJphahwE79rBV_/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Yorkers_Bb_Clar.png','https://drive.google.com/file/d/192KkyVI1op3xQeeSl79NbRI7XU7RLdKN/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Yorkers_Bb_TenSax.png','https://drive.google.com/file/d/1AyyYxG47Pawg77roHWLO6C_e7vDMWtFw/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Yorkers_Eb.png','https://drive.google.com/file/d/1BkZW8RrArcACnMg5gM0vbkTPNRSUbaUl/view?usp=sharing',177)



#Blues
make_qrcode(qr_path+'QR_12BarBlues.png','https://drive.google.com/file/d/1OHr9iwjNYFbsxZHoa1RS-AfROFuDm8Ch/view?usp=sharing',177)
#Aint No Sunshine
make_qrcode(qr_path+'QR_AintNoSunshine_C.png','https://drive.google.com/file/d/1J_ZdZNUzUseTFA3Mi_fjkeeTvPVIrYqT/view?usp=sharing',177)
make_qrcode(qr_path+'QR_AintNoSunshine_Bb.png','https://drive.google.com/file/d/13f2lNUz1C247Ogn2C5tAnVGWg88JS_gu/view?usp=sharing',177)
make_qrcode(qr_path+'QR_AintNoSunshine_Eb.png','https://drive.google.com/file/d/1dTvrf3A48ORShqTAbUJTz7ogntp70PrM/view?usp=sharing',177)



#Rock songs
make_qrcode(qr_path+'QR_SultansOfSwing_BassChords.png','https://drive.google.com/file/d/14Mgmnunz_iVf0pWnBqPTu4IfZM3BnELL/view?usp=sharing',177)
make_qrcode(qr_path+'QR_SultansOfSwing_LyricsChords.png','https://drive.google.com/file/d/12ey8yiDbB8bjwqNiFY8qKywqtbjeWyLv/view?usp=sharing',177)
#Nothing Else Matters
make_qrcode(qr_path+'QR_NothingElseMatters_C.png','https://drive.google.com/file/d/1QV1lAMdvw9MQjaJry_E1cfQB_R1GMIM5/view?usp=sharing',177)
make_qrcode(qr_path+'QR_NothingElseMatters_Bb_TenSax.png','https://drive.google.com/file/d/1FUrmalJmJsJ6YSIuoJ39RbBjvwQIzJvW/view?usp=sharing',177)
make_qrcode(qr_path+'QR_NothingElseMatters_Bb_Clar.png','https://drive.google.com/file/d/1M0lCglMcjoq9CazwwvrmcfK8G2shlN8h/view?usp=sharing',177)
make_qrcode(qr_path+'QR_NothingElseMatters_Eb.png','https://drive.google.com/file/d/1uVsQ0sEYltGi3-CQphSvynD7fugo4Fnu/view?usp=sharing',177)



#Movie and Games
make_qrcode(qr_path+'QR_LuxAeterna_C.png','https://drive.google.com/file/d/1AvHzKg3lPEnnRlelcVWPcTGUGytP3JMC/view?usp=sharing',177)
make_qrcode(qr_path+'QR_LuxAeterna_Bb.png','https://drive.google.com/file/d/1NPdjVjOLweDTzEvUCHCUMQDK6Kw2JQt_/view?usp=sharing',177)
make_qrcode(qr_path+'QR_LuxAeterna_Eb.png','https://drive.google.com/file/d/1Taa9JOiNix9KWtuwoB_Kr5P-veFFs4QZ/view?usp=sharing',177)
make_qrcode(qr_path+'QR_LuxAeterna_Chords.png','https://drive.google.com/file/d/1spoS4tFDuOX45NCh1EDfrDmjujJ_5gaF/view?usp=sharing',177)



#Jazz Songs
#Misty
make_qrcode(qr_path+'QR_Misty_C.png','https://drive.google.com/file/d/1nLj0BwRtym9ie3egvLstCqjHEMf_yrA1/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Misty_Bb_Clar.png','https://drive.google.com/file/d/1sf52akUNpAVC8uPWPksu18OX_avubJjw/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Misty_Bb_TenSax.png','https://drive.google.com/file/d/1sSc9oblveNQpBqP6l1PVO2BylH9cLXBa/view?usp=sharing',177)
make_qrcode(qr_path+'QR_Misty_Eb.png','https://drive.google.com/file/d/1fwpVEigX2G3tcp1w7ifO-OB95wqQvS33/view?usp=sharing',177)
#FlyMeToTheMoon
make_qrcode(qr_path+'QR_FlyMeToTheMoon_C.png','https://drive.google.com/file/d/1YMtMuhKj-PoPnjcN4u2KdUhypH2COYJi/view?usp=sharing',177)
make_qrcode(qr_path+'QR_FlyMeToTheMoon_Bb.png','https://drive.google.com/file/d/1rZrEwCUua2juT37dwWSJBNo477wUh3Sc/view?usp=sharing',177)
make_qrcode(qr_path+'QR_FlyMeToTheMoon_Eb.png','https://drive.google.com/file/d/1afSnEV9t1xQP1n7V8YeKE1U-yoNJQm1s/view?usp=sharing',177)


make_qrcode(qr_path+'QR_SpotifyPlaylist.png','https://open.spotify.com/playlist/29o5CLQWelLBBaHMstmTTg?si=cf957ec2a51848a2',177)
