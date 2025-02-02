# 📑 **Table Extraction from PDF Using OCR**  
_A robust solution for extracting tables from PDF documents with a focus on accuracy and preserving table structures._

## 🚀 **Project Overview**  
This project provides a **solution for extracting tables** from PDF documents using **Optical Character Recognition (OCR)**.

Due to the complexity of table formatting, some tools like `pdfplumber` or `camelot` may fail to handle edge cases or correctly maintain the layout. Our solution combines **OCR technology** with **OpenCV image processing** to achieve better accuracy and preserve original table formatting.

---

## 🔧 **What We Have Done**
### **1. Extracted Tables Using OCR**  
- We utilized **OCR** technology to extract text from scanned or image-based PDFs.  
- Tables were extracted from specific pages within the PDFs, ensuring correct structure, column names, and rows were captured.
  
### **2. Used OpenCV for Table Detection**  
- We applied **OpenCV** for accurate **table detection** by identifying the boundaries and structure of the tables before applying OCR. This step ensured we didn’t extract irrelevant text or modify table formatting.

### **3. Addressed OCR Limitations**  
- **Mathematical expressions, superscripts, and subscripts** were preserved as per the original document layout.
- Certain limitations were encountered, but we explored various techniques to **enhance accuracy**, such as fine-tuning the OCR process and handling page layout issues.

### **4. Saved Data in Excel Format**  
- The final extracted table data was saved into **Excel files**, preserving the structure and data integrity. This allows easy usage for further analysis and reporting.

---

## 📦 **How to Run the Project**

### **1. Install Required Dependencies**
Before you start, make sure to install all the necessary dependencies using the following command:
```bash
pip install -r requirements.txt

Tesseract Installation
You’ll need to install Tesseract OCR to extract text from PDF images. Follow these steps:

Download and install Tesseract OCR:
Windows : https://github.com/UB-Mannheim/tesseract/wiki
Linux/MacOS : https://tesseract-ocr.github.io/tessdoc/Installation.html

Once installed, add the Tesseract installation path to your system’s environment variables or specify the path in the script like so:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Cloning the Repository
To get started, clone the repository to your local system:

git clone https://github.com/Karthik0704/Mayora_OCR.git
cd pdf-table-extraction

Run the Extraction Script
To extract tables from a PDF, run the following command:

python extract_tables.py --input "path_to_your_pdf.pdf" --output "output.xlsx" --page <page_number>

Where:

--input: Path to the PDF file from which you want to extract tables.
--output: The name of the Excel file where the extracted tables will be saved.
--page: The page number containing the table you want to extract.

Example:

python extract_tables.py --input "cardio_structured.pdf" --output "output_cardio.xlsx" --page 6


4. Handling Multiple Pages:
If your table spans multiple pages, you can adjust the page range in the command as needed:

python extract_tables.py --input "prot_sap_102.pdf" --output "output_prot_sap_102.xlsx" --page_range 50-60

📌 Project Structure:
📁 pdf-table-extraction
│── 📄 README.md           # Project overview and instructions
│── 📄 requirements.txt    # Python dependencies
│── 📂 data/               # Folder containing input PDF files
│── 📂 output/             # Folder to store output Excel files
│── 📜 extract_tables.py   # Python script for table extraction

📝 Future Work & Improvements
While the current methodology gives excellent results for most PDFs, some complex cases may still result in slightly imperfect extractions. Future work may include:

Improving OCR accuracy for complex expressions and formulas.
Supporting batch extraction for multiple PDFs or pages.
Enhancing GUI-based interaction for easier use by non-technical users.

📜 License
This project is licensed under the MIT License. Feel free to modify and use it as per your requirements. 😊

🤝 Contributing
Contributions to improve the project are welcome! Feel free to open an issue or submit a pull request to help make this tool even more powerful.

🔥 Ready to extract accurate tables from PDFs? Let’s go! 🚀