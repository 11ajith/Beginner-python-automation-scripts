# QR CODE generator for given data 

import qrcode
import cv2
import numpy

def generate_qrcode(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(data.strip())
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    imcv = numpy.asarray(img.convert('L'))
    cv2.imwrite('qrcode.png', imcv)
    
generate_qrcode("enter the data to be encoded as qr code")