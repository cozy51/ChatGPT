# ChatGPT

This repository includes a small script for merging multiple PDF files into a single PDF.

## Requirements

- Python 3
- The `PyPDF2` package. Install with:

```bash
python3 -m pip install PyPDF2
```

(You may need internet access or a local package repository to install.)

## Usage

Run the script from the command line, providing the name of the output PDF followed by the input PDF files:

```bash
python merge_pdfs.py merged.pdf file1.pdf file2.pdf [file3.pdf ...]
```

This will combine all the input files in the given order and create `merged.pdf`.
