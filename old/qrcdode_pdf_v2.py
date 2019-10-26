from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Frame, PageTemplate
from reportlab.lib.units import cm,mm
from reportlab.platypus import (Table, TableStyle, BaseDocTemplate)
from reportlab.platypus.flowables import TopPadder

def create_pdf():
    """
    Create a pdf
    """

    # Create a frame
    CatBox_frame = Frame(
        x1=14.00 * cm,  # From left
        y1=1.5 * cm,  # From bottom
        height=9.60 * cm,
        width=5.90 * cm,
        leftPadding=0 * cm,
        bottomPadding=0 * cm,
        rightPadding=0 * cm,
        topPadding=0 * cm,
        showBoundary=1,
        id='CatBox_frame')

    # Create a table
    CatBox = Table([
        ['', '', '', 'A'],
        ['', '', '', 'B'],
        ['', '', '', 'C'],
        ['AA', 'BB', 'CC', '']], 1.2 * cm, 1.2 * cm, vAlign='BOTTOM')

    # Style the table
    CatBox.setStyle(TableStyle([
        ('SIZE', (0, 0), (-1, -1), 7),
        ('SIZE', (0, 0), (0, 0), 5.5),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
    ]))

    # Trying to tell the table to be a bottom align object (when later put in frame)
    CatBox.Align = 'BOTTOM'
    CatBox.vAlign = 'BOTTOM'

    # Building the story
    #story = [CatBox] # adding CatBox table (alternative, story.add(CatBox))
    story = [TopPadder(CatBox)]

    # Establish a document
    doc = BaseDocTemplate("BottomAlignTable.pdf", pagesize=letter)

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