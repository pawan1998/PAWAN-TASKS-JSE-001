from django.conf import settings
from django_endesive import pdf
from endesive.pdf import fpdf
import datetime
from django.conf import settings
# Generate a pdf file (this could be any file already generated by your app)
doc = fpdf.FPDF()
doc.add_page()
doc.set_font('helvetica', '', 13.0)
doc.cell(w=75.0, h=22.0, align='C',
              txt='Hello, world page=1.', border=0, ln=0)
doc.output('./pdf.pdf', "F")

# Open file and feed bytes to the sign function
pdf_bytes = open('./pdf.pdf', 'rb').read()

signed_pdf = pdf.sign(pdf_bytes=pdf_bytes)
print('signed_pdf')