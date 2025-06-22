import sys
from PyPDF2 import PdfMerger


def merge_pdfs(output_path, input_paths):
    merger = PdfMerger()
    for path in input_paths:
        with open(path, 'rb') as f:
            merger.append(f)
    with open(output_path, 'wb') as f:
        merger.write(f)


def main(args):
    if len(args) < 3:
        print("Usage: python merge_pdfs.py output.pdf input1.pdf input2.pdf [input3.pdf ...]")
        return 1
    output = args[1]
    inputs = args[2:]
    merge_pdfs(output, inputs)
    print(f"Merged {len(inputs)} files into {output}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
