from PyPDF2 import PdfReader, PdfWriter

# Load the uploaded PDF
reader = PdfReader("/mnt/data/KyleCV.pdf")#alter file path to get PDF
writer = PdfWriter()

# Only keep the first page
#for page_num in [0, 2, 4]:  # (page numbers start at 0)
#    writer.add_page(reader.pages[page_num])
writer.add_page(reader.pages[0])

# Save the new PDF
output_path = "/mnt/data/KyleCV_1page.pdf"
with open(output_path, "wb") as f:
    writer.write(f)

output_path