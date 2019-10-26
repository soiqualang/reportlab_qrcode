from reportlab.lib import colors
from reportlab.lib.pagesizes import QRCode,letter,QRCodeInch,inch,mm
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
 
doc = SimpleDocTemplate("complex_cell_values.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []
 
styleSheet = getSampleStyleSheet()
 
I = Image('qr1.png')
I.drawHeight = 0.787401575*inch*I.drawHeight / I.drawWidth
I.drawWidth = 0.787401575*inch
P0 = Paragraph('''
               <b>A pa<font color=red>r</font>a<i>graph</i></b>
               <super><font color=yellow>1</font></super>''',
               styleSheet["BodyText"])
P = Paragraph('''
    <para align=center spaceb=3>The <b>ReportLab Left
    <font color=red>Logo</font></b>
    Image</para>''',
    styleSheet["BodyText"])
data= [['02', [I], '04'],
       ['12', [I], '14']]


t=Table(data,3*[1.44094488*inch], 2*[0.984251969*inch])
t.setStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black)
            ])
#t._argW[1]=1.5*inch


t2_style=[('GRID',(1,1),(-2,-2),1,colors.green),
                    ('BOX',(0,0),(1,-1),2,colors.red),
                    ('LINEABOVE',(1,2),(-2,2),1,colors.blue),
                    ('LINEBEFORE',(2,1),(2,-2),1,colors.pink),
                    ('BACKGROUND', (0, 0), (0, 1), colors.pink),
                    ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
                    ('BACKGROUND', (2, 2), (2, 3), colors.orange),
                    ('BOX',(0,0),(-1,-1),2,colors.black),
                    ('GRID',(0,0),(-1,-1),0.5,colors.black),
                    ('VALIGN',(3,0),(3,0),'BOTTOM'),
                    ('BACKGROUND',(3,0),(3,0),colors.limegreen),
                    ('BACKGROUND',(3,1),(3,1),colors.khaki),
                    ('ALIGN',(3,1),(3,1),'CENTER'),
                    ('BACKGROUND',(3,2),(3,2),colors.beige),
                    ('ALIGN',(3,2),(3,2),'LEFT'),
]

data2=[['02', 'haha', '04'],
       ['12', 'haha', '14']]
#t2=Table(data2,3*[1.44094488*inch], 2*[0.984251969*inch])
#t2=Table(data2)
#_argW dung de resize column to content
#t2._argW[1]=1.5*inch

""" Thong tin 1 tem
size: 25 mm to 0.984251969 inch """

t2=Table(data2, colWidths=0.984251969*inch, rowHeights=0.984251969*inch, style=t2_style, splitByRow=1,
repeatRows=2, repeatCols=3, rowSplitRange=None, spaceBefore=None,
spaceAfter=None)
 
elements.append(t2)
# write the document to disk
doc.build(elements)