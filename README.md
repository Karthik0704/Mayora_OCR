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
```bash
pip install -r requirements.txt
