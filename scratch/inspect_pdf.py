import os

pdf_path = "docs/Gonzales_Suyo_Franz_Reinaldo-ActividadNº3.pdf"
print("File exists:", os.path.exists(pdf_path))
if os.path.exists(pdf_path):
    print("File size:", os.path.getsize(pdf_path), "bytes")

cepi_path = "docs/GUIA-CEPI-ver2.0.pdf"
print("CEPI exists:", os.path.exists(cepi_path))
if os.path.exists(cepi_path):
    print("CEPI size:", os.path.getsize(cepi_path), "bytes")

try:
    import pypdf
    print("pypdf available")
    reader = pypdf.PdfReader(pdf_path)
    print(f"Total pages in Actividad 3 PDF: {len(reader.pages)}")
    cepi_reader = pypdf.PdfReader(cepi_path)
    print(f"Total pages in GUIA CEPI PDF: {len(cepi_reader.pages)}")
except Exception as e:
    print("pypdf error:", e)

