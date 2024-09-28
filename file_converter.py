import pdf2docx as p2d
import docx2pdf as d2p
import os
from pdf2image import convert_from_path


# CONVERT PDF TO DOC

def pdf_to_docx(path):
    
    pdf_file = os.path.abspath(path) 
    docx_file = os.path.abspath(f"{path}.docx")  
    
    if not os.path.isfile(pdf_file):
        print(f"Error: File {pdf_file} not found.")
        return 0
    
   
    cv = p2d.Converter(pdf_file)
    cv.convert(docx_file)  
    cv.close() 

# CONVERT DOC TO PDF

def docx_to_pdf(path):
    
    docx_file = os.path.abspath(path) 
    pdf_file = os.path.abspath(f"{path}.pdf")      
   
    if not os.path.isfile(docx_file):
        print(f"Error: File {docx_file} not found.")
        return 0
    
    d2p.convert(docx_file, pdf_file) 


# MAIN BODY  

print("Select the type of conversion: ")
print("1. PDF TO DOCX")
print("2. DOCX TO PDF")


choice = [1, 2]

user_input = int(input("Enter your choice: "))
if user_input in choice:
    file = input("Enter the path of the file: ")
    if user_input == 1:
        pdf_to_docx(file)
    elif user_input == 2:
        docx_to_pdf(file)
else:
    print("Invalid Input")
