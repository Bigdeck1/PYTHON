import zipfile
import os
import openpyxl
import shutil
import pandas as pd
from lxml import etree

def extract_xlsx_from_zip(zip_path, extract_to_dir):
    """
    Extracts the .xlsx file from the given ZIP archive.
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # List all files inside the ZIP
            file_list = zip_ref.namelist()
            print(f"Files in the ZIP archive: {file_list}")

            # Look for the .xlsx file in the ZIP
            xlsx_files = [f for f in file_list if f.endswith('.xlsx')]
            if not xlsx_files:
                print("No .xlsx file found inside the ZIP archive.")
                return None

            # Extract the first .xlsx file found
            xlsx_file = xlsx_files[0]
            print(f"Extracting {xlsx_file} from ZIP...")
            zip_ref.extract(xlsx_file, extract_to_dir)

            extracted_xlsx_path = os.path.join(extract_to_dir, xlsx_file)
            print(f"Extracted .xlsx file to: {extracted_xlsx_path}")
            return extracted_xlsx_path

    except zipfile.BadZipFile as e:
        print(f"Error opening ZIP file: {e}")
        return None

def recover_excel(file_path):
    """
    Tries to recover a corrupted .xlsx file.
    """
    print(f"Starting recovery for file: {file_path}")

    # Try to open the file with openpyxl
    try:
        workbook = openpyxl.load_workbook(file_path)
        print("File loaded successfully with openpyxl.")
        # Return workbook or first sheet to inspect data
        return workbook
    except Exception as e:
        print(f"Error opening file with openpyxl: {e}")
        print("Proceeding with pandas recovery...")

    # Fallback: Try pandas to recover data
    try:
        data = pd.read_excel(file_path)
        print("File loaded successfully with pandas.")
        print(data.head())  # Display first few rows of the data
        return data
    except Exception as e:
        print(f"Error opening file with pandas: {e}")
        print("File may be too corrupted to recover.")

# Example usage
zip_file_path = r"C:\Users\Clarence\OneDrive\Attachments\Desktop\tryrecover.zip"
extraction_dir = r"C:\Users\Clarence\OneDrive\Attachments\Desktop\recovered_files"

# Step 1: Extract the .xlsx file from the ZIP archive
extracted_xlsx_path = extract_xlsx_from_zip(zip_file_path, extraction_dir)

if extracted_xlsx_path:
    print(f"Extracted .xlsx file path: {extracted_xlsx_path}")
    # Step 2: Attempt to recover the .xlsx file
    recover_excel(extracted_xlsx_path)
else:
    print("No .xlsx file extracted from the ZIP.")
