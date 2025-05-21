from PyPDF2 import PdfWriter
import os 


merger = PdfWriter()  # Creating a PdfWriter object to handle merging


# Asking the user how many PDFs they want to merge
try:
    n = int(input("How many PDFs you want to merge: "))
except ValueError:
    print("Please enter a valid number.")
    exit()


# List to store valid PDF filenames
pdfs = []  


# Loop to collect each PDF filename from the user
for i in range(n):
    name = input(f"Enter the file name #{i + 1}: ").strip()  # Get filename and remove extra spaces

    if name == "":
        print("Empty filename. Skipping this entry.")  # Skip if input is empty
        continue

    if not name.endswith(".pdf"):
        name += ".pdf"  # Automatically add '.pdf' if not provided

    if not os.path.isfile(name):
        print(f"File '{name}' not found. Skipping.")  # Check if file exists
        continue

    pdfs.append(name)  # Add valid file to the list


# If no valid PDFs were collected, exit the program
if not pdfs:
    print("No valid PDFs to merge. Exiting.")
    exit()


# Append each valid PDF to the merger object
for i, pdf in enumerate(pdfs):
    try:
        merger.append(pdf)
        print(f"Merged: {pdf} ({i + 1}/{len(pdfs)})")  # Show progress
    except Exception as e:
        print(f"Failed to merge '{pdf}': {e}")  # Handle merging errors
        exit()


# Ask user for output filename
pdf_output_name = input("Enter the name of merged file: ")


# Use default name if none is given
if not pdf_output_name or pdf_output_name == "":
    pdf_output_name = "merged-pdf"


# Ensure output filename ends with '.pdf'
if not pdf_output_name.endswith(".pdf"):
    pdf_output_name += ".pdf"


# Write all merged content to the output file
merger.write(f"{pdf_output_name}")
merger.close()
print(f"\nDone Merged file saved as '{pdf_output_name}.'\n")  # Final confirmation message
