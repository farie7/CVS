from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from models import Student


def print_document(student: Student) -> None:
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFillColorRGB(0, 0, 0)
    can.setFont("Times-Roman", 32)
    can.drawString(x=145, y=520, text=student.full_name)
    can.drawString(x=130, y=200, text=str(student.graduation_year))
    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("certificate-templates-for-word1.pdf", "rb"))
    output = PdfFileWriter()

    page = existing_pdf.getPage(0)

    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    # And finally, write "output" to a real file:
    file = student.reg_number + '.pdf'
    output_stream = open("instance/verified_students/"+file, "wb")
    output.write(output_stream)
    output_stream.close()
