import os
import PyPDF2

# Set the path to the folder containing the PDF files
folder_path = "//////////"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        # Open the PDF file in read-binary mode
        with open(os.path.join(folder_path, filename), "rb") as pdf_file:
            # Create a PyPDF2 PdfFileReader object from the file
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            # Loop through each page in the PDF
            for page in range(len(pdf_reader.pages)):
                # Get the page object
                pdf_page = pdf_reader.pages[page]
                
                # Check if the page has a watermark
                if "/Watermark" in pdf_page["/Resources"].get_object():
                    # Remove the watermark from the page
                    pdf_page["/Resources"].get_object().pop("/Watermark", None)
                    
            # Create a PyPDF2 PdfFileWriter object to write the modified PDF
            pdf_writer = PyPDF2.PdfWriter()
            
            # Add each modified page to the writer object
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])
                
            # Save the modified PDF file
            with open(os.path.join(folder_path, "modified_" + filename), "wb") as output_pdf:
                pdf_writer.write(output_pdf)
