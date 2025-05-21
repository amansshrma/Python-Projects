# PDF Merger Tool

This is a simple command-line Python tool that merges multiple PDF files into a single PDF. It ensures only valid PDF files are merged and provides user-friendly prompts and feedback.

## Features

- User-defined number of PDFs to merge.
- Validates file existence and extension.
- Automatically appends `.pdf` extension if missing.
- Skips invalid or non-existent files.
- Provides progress updates for merging.
- Lets the user name the output file.

## Usage

1. Clone this repository:

```bash
git clone https://github.com/amansshrma/Python-Projects.git
cd Python-Projects/03_PDF_merge
```

2. Make sure you have `PyPDF2` installed:

```bash
pip install PyPDF2
```

3. Run the script:

```bash
python pdf_merger.py
```

4. Follow the prompts to merge your PDF files.

## Example

```bash
How many PDFs you want to merge: 3
Enter the file name #1: file1.pdf
Enter the file name #2: file2
Enter the file name #3: invalidfile.pdf
File 'invalidfile.pdf' not found. Skipping.
Enter the name of merged file: combined
```

Result:
```
Merged: file1.pdf (1/2)
Merged: file2.pdf (2/2)
Done Merged file saved as 'combined.pdf.'
```

## Author

[amansshrma](https://github.com/amansshrma)

## License

This project is licensed under the MIT License.
