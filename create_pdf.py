from PyPDF2 import PdfFileWriter, PdfFileReader
import io

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from models import Student

templates = {
    'hit': 'HIT.pdf',
    'uz': "UZ.pdf",
    'nust': 'NUST.pdf'
}


def print_document(student: Student, institution) -> None:
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFillColorRGB(0, 0, 0)
    pdfmetrics.registerFont(TTFont('Ubuntu', 'dev_test/Fonts/Ubuntu-Bold.ttf'))
    can.setFont("Ubuntu", 15,)
    print("this is record id : " + str(student.id))
    can.drawString(x=250, y=596, text=student.name)
    can.drawString(x=250, y=566, text=student.surname)
    can.drawString(x=250, y=536, text=student.reg_number)
    can.drawString(x=241, y=506, text=student.programme)
    can.drawString(x=250, y=476, text=student.degree_class)
    can.drawString(x=280, y=140, text=str(student.graduation_year))
    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    existing_pdf = PdfFileReader(open(templates[institution], "rb"))
    output = PdfFileWriter()

    page = existing_pdf.getPage(0)

    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    # And finally, write "output" to a real file:
    file = student.reg_number + student.programme + '.pdf'
    output_stream = open("instance/verified_students/" + file, "wb")
    output.write(output_stream)
    output_stream.close()
