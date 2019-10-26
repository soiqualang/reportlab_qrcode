#from reportlab.graphics.barcode import code39, code128, code93
#from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing 
from reportlab.lib.pagesizes import QRCode
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF

#table
from reportlab.lib import colors
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
 
#----------------------------------------------------------------------
def createBarCodes():
    """
    Create barcode examples and embed in a PDF
    """
    """ c = canvas.Canvas("barcodes.pdf", pagesize=QRCode) """

    doc = SimpleDocTemplate("complex_cell_values.pdf", pagesize=QRCode)

    elements = []
 
    styleSheet = getSampleStyleSheet()

    barcode_value = "1234567890"    
 
    # draw a QR code
    qr_code = qr.QrCodeWidget(barcode_value)
    d = Drawing(20*mm, 20*mm)
    d.add(qr_code)

    data= [[d, d, d],
       ['00', '01', '02'],
       ['10', '11', '12']]

    # 3 hang*chieu rong hang, 3 cot * chieu dai 1 cot
    t=Table(data,3*[36.6*mm], 3*[2.5*mm])

    t.setStyle(TableStyle([
                       ('ALIGN',(0,0),(-1,-1),'CENTER'),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))

    elements.append(t)
    # write the document to disk
    doc.build(elements)


 
    
    #Vi tri left-bottom
    #renderPDF.draw(d, c, 0, 0) 
    #c.save()
 
if __name__ == "__main__":
    createBarCodes()