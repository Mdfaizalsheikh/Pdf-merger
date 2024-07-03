import PyPDF2
import os

def merge_pdfs(pdf_list, output):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output, 'wb') as out_file:
        pdf_writer.write(out_file)

    print(f'Merged {len(pdf_list)} files into {output}')

def split_pdf(input_pdf):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])

        output = f'{os.path.splitext(input_pdf)[0]}_page_{page_num + 1}.pdf'
        with open(output, 'wb') as out_file:
            pdf_writer.write(out_file)

        print(f'Created {output}')

if __name__ == '__main__':
    while True:
        print("PDF Tool")
        print("1. Merge PDFs")
        print("2. Split PDF")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            pdf_list = input("Enter the PDF files to merge (comma separated): ").split(',')
            output = input("Enter the output file name: ")
            merge_pdfs(pdf_list, output)
        elif choice == '2':
            input_pdf = input("Enter the PDF file to split: ")
            split_pdf(input_pdf)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
