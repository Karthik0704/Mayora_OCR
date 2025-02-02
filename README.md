# 📑 Table Extraction from PDF Using OCR

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A robust solution for extracting tables from PDF documents with a focus on accuracy and preserving table structures.

## 🚀 Project Overview
This project provides a solution for extracting tables from PDF documents using Optical Character Recognition (OCR).

Due to the complexity of table formatting, some tools like `pdfplumber` or `camelot` may fail to handle edge cases or correctly maintain the layout. Our solution combines OCR technology with OpenCV image processing to achieve better accuracy and preserve original table formatting.

## 🔧 What I Have Done

### 1. Extracted Tables Using OCR
- Utilized OCR technology to extract text from scanned or image-based PDFs
- Tables were extracted from specific pages within the PDFs, ensuring correct structure, column names, and rows were captured

### 2. Used OpenCV for Table Detection
- Applied OpenCV for accurate table detection by identifying the boundaries and structure of the tables before applying OCR
- This step ensured we didn't extract irrelevant text or modify table formatting

### 3. Addressed OCR Limitations
- Mathematical expressions, superscripts, and subscripts were preserved as per the original document layout
- Enhanced accuracy through fine-tuning the OCR process and handling page layout issues

### 4. Saved Data in Excel Format
- The final extracted table data was saved into Excel files, preserving the structure and data integrity
- This allows easy usage for further analysis and reporting

## 📦 How to Run the Project

### 1. Install Required Dependencies

```pip install -r requirements.txt```
2. Tesseract Installation
You'll need to install Tesseract OCR to extract text from PDF images:

Windows: ```https://github.com/UB-Mannheim/tesseract/wiki```
Linux/MacOS: ```https://tesseract-ocr.github.io/tessdoc/Installation.html```

Add Tesseract to your system's environment variables or specify the path in the script:

```pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"```

3. Clone the Repository

```git clone https://github.com/Karthik0704/Mayora_OCR.git```
```cd pdf-table-extraction```

4. Run the Extraction Script

```python extract_tables.py --input "path_to_your_pdf.pdf" --output "output.xlsx" --page <page_number>```

Parameters:

--input: Path to the PDF file
--output: Name of the output Excel file
--page: Page number containing the table
Example:

```python extract_tables.py --input "cardio_structured.pdf" --output "output_cardio.xlsx" --page 6```

5. Handling Multiple Pages
```python extract_tables.py --input "prot_sap_102.pdf" --output "output_prot_sap_102.xlsx" --page_range 50-60```

📂 Project Structure

📁 pdf-table-extraction
│── 📄 README.md           # Project overview and instructions
│── 📄 requirements.txt    # Python dependencies
│── 📂 data/               # Folder containing input PDF files
│── 📂 output/             # Folder to store output Excel files
│── 📜 extract_tables.py   # Python script for table extraction

📝 Future Work & Improvements
Improving OCR accuracy for complex expressions and formulas
Supporting batch extraction for multiple PDFs or pages
Enhancing GUI-based interaction for easier use by non-technical users
📜 License
This project is licensed under the MIT License.

🤝 Contributing
Contributions to improve the project are welcome! Feel free to open an issue or submit a pull request.
