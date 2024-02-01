import sys
from PyPDF2 import PdfReader, PdfWriter
import os.path as op

def merge_pdfs(output_path, input_paths):
    pdf_writer = PdfWriter()

    for path in input_paths:
        pdf_reader = PdfReader(path)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3:
        print("Usage: python merge_pdfs.py input1.pdf input2.pdf ...")
        input("Press enter to exit...")
        sys.exit(1)

    # Get the output path and input paths from command-line arguments
    output_path = op.dirname(sys.argv[1]) + "/merged_pdfs.pdf"
    input_paths = sys.argv[1:]

    # Merge the PDFs
    merge_pdfs(output_path, input_paths)

    print(f"PDFs merged successfully. Output saved to {output_path}")
