import pdfplumber
import pandas as pd
import pytesseract
import cv2
import numpy as np
import camelot
from pdf2image import convert_from_path
import os

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
if os.name == 'nt':
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

pdf_files = {
    "cardio_structured.pdf": 6,
    "prot_sap_102.pdf": 50,
    "prot_sap_1.pdf": 14
}

os.makedirs("output", exist_ok=True)

def extract_with_pdfplumber(pdf_path, page_number):
    """Extract tables using pdfplumber."""
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number - 1]  
        tables = page.extract_tables()
        return tables

def extract_with_camelot(pdf_path, page_number):
    """Extract tables using Camelot (for text-based PDFs)."""
    tables = camelot.read_pdf(pdf_path, pages=str(page_number))
    return tables if tables.n > 0 else None

def extract_with_ocr(pdf_path, page_number):
    """Extract tables using OCR + OpenCV (for scanned PDFs)."""
    images = convert_from_path(pdf_path, first_page=page_number, last_page=page_number)
    for img in images:
        img.save("temp_page.png", "PNG")  
        
        image = cv2.imread("temp_page.png", cv2.IMREAD_GRAYSCALE)
        _, binary = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
        kernel = np.ones((2,2), np.uint8)
        processed = cv2.dilate(binary, kernel, iterations=1)

       
        text = pytesseract.image_to_string(processed, config="--psm 6")

        
        with open(f"output/{os.path.basename(pdf_path)}_page_{page_number}.txt", "w", encoding="utf-8") as f:
            f.write(text)

        return text  

def save_to_excel(data, output_excel, sheet_name="Sheet1"):
    """Save extracted data to Excel format."""
    with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
        if isinstance(data, list):  
            for i, table in enumerate(data):
                df = pd.DataFrame(table)
                df.to_excel(writer, sheet_name=f"{sheet_name}_Table_{i+1}", index=False, header=False)
        elif isinstance(data, camelot.core.TableList):  
            data[0].df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
        else:  
            df = pd.DataFrame([data.split("\n")])
            df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)


for pdf, page in pdf_files.items():
    pdf_path = f"data/{pdf}"
    output_excel = f"output/{pdf.replace('.pdf', '')}_tables.xlsx"

    
    tables = extract_with_pdfplumber(pdf_path, page)
    if tables and any(tables):  
        print(f"✅ Extracted tables using pdfplumber for {pdf} (Page {page})")
        save_to_excel(tables, output_excel, sheet_name=f"Page_{page}")
        continue

    
    tables = extract_with_camelot(pdf_path, page)
    if tables:
        print(f"✅ Extracted tables using Camelot for {pdf} (Page {page})")
        save_to_excel(tables, output_excel, sheet_name=f"Page_{page}")
        continue

    
    print(f"⚠️ No tables found using pdfplumber or Camelot. Using OCR for {pdf} (Page {page})...")
    text = extract_with_ocr(pdf_path, page)
    save_to_excel(text, output_excel, sheet_name=f"Page_{page}_OCR")

print("✅ Extraction Completed with Higher Accuracy!")
