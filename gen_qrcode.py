from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import mm
import datetime
import time
import hashlib
from random import randrange

def genQR(barcode_value):
    qr_code = qr.QrCodeWidget(barcode_value)
    #d = Drawing(15*mm, 15*mm)
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    size=55
    d = Drawing(55, 55, transform=[55./width,0,0,55./height,0,0])
    d.add(qr_code)
    return d

def genNum():
    #now = datetime.now()
    #dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    timenow = int(time.time())

    tmparr=[]
    rand=''
    for i in range(0,9):
        rand=randrange(1000)
        if rand not in tmparr:
            t1=str(timenow)+str(rand)
            #t1=hashlib.md5(t1.encode('utf-8')).hexdigest()
            tmparr.append(t1)
    #dt_string=hashlib.md5(dt_string.encode('utf-8')).hexdigest()
    return tmparr
