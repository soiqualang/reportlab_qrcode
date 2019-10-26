from reportlab.lib.pagesizes import letter,QRCode
from reportlab.lib import colors
from reportlab.platypus import Frame, PageTemplate,Image
from reportlab.lib.units import cm,mm
from reportlab.platypus import (Table, TableStyle, BaseDocTemplate)
from reportlab.platypus.flowables import TopPadder

from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
import datetime
import time
import hashlib
from random import randrange


def genQR(barcode_value):
    qr_code = qr.QrCodeWidget(barcode_value)
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    size=55
    d = Drawing(55, 55, transform=[55./width,0,0,55./height,0,0])
    d.add(qr_code)
    return d

def genNum():
    timenow = int(time.time())

    tmparr=[]
    rand=''
    for i in range(0,9):
        rand=randrange(1000)
        if rand not in tmparr:
            t1=str(timenow)+str(rand)
            tmparr.append(t1)
    return tmparr

def create_pdf():

    I = Image('qr1.png')
    I.drawHeight = 18*mm*I.drawHeight / I.drawWidth
    I.drawWidth = 18*mm

    qr1=genQR('hahahahah')

    # Create a frame
    CatBox_frame = Frame(
        x1=0 * mm,  # From left
        y1=0 * mm,  # From bottom
        height=75 * mm,
        width=110 * mm,
        leftPadding=0 * mm,
        bottomPadding=0 * mm,
        rightPadding=0 * mm,
        topPadding=0 * mm,
        showBoundary=1,
        id='CatBox_frame')

    table_data=[[qr1, qr1, qr1],
                [qr1, qr1, qr1],
                [qr1, qr1, qr1]]

    table_data2=[]
    qrcode_valarr=genNum()
    arrindex=0
    for i in range(0,3):
        t1=[]
        for j in range(0,3):
            qr1=genQR(qrcode_valarr[arrindex])
            arrindex=arrindex+1
            t1.append(qr1)
        table_data2.append(t1)

    
    # Create a table
    CatBox = Table(table_data2, 36.6* mm, 25 * mm, vAlign='BOTTOM')

    # Style the table
    CatBox.setStyle(TableStyle(
            [('ALIGN',(0,0),(-1,-1),'CENTER'),
             ('VALIGN',(0,0),(-1,-1),'MIDDLE')
            ]))

    # Trying to tell the table to be a bottom align object (when later put in frame)
    CatBox.Align = 'BOTTOM'
    CatBox.vAlign = 'BOTTOM'

    # Building the story
    #story = [CatBox] # adding CatBox table (alternative, story.add(CatBox))
    story = [TopPadder(CatBox)]

    # Establish a document
    doc = BaseDocTemplate("DanhSach_QRCode.pdf", pagesize=QRCode)

    # Creating a page template 
    frontpage = PageTemplate(id='FrontPage',
                             frames=[CatBox_frame]
                             )
    # Adding the story to the template and template to the document
    doc.addPageTemplates(frontpage)

    # Building doc
    doc.build(story)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    create_pdf() # Printing the pdf