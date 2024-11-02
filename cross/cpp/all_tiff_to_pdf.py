import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def tiff_to_pdf_with_title(input_folder, output_pdf):
    # Register a font (you may need to change the path to a font file you have)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

    # Create a new PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)
    
    # Get all TIFF files in the input folder
    tiff_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.tif', '.tiff'))]
    
    for tiff_file in tiff_files:
        # Open the TIFF image
        img_path = os.path.join(input_folder, tiff_file)
        img = Image.open(img_path)
        
        # Convert TIFF to RGB if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Get image dimensions
        width, height = img.size
        
        # Calculate scaling factor to fit on the page
        scale = min(letter[0] / width, letter[1] / height)
        
        # Calculate new dimensions
        new_width = width * scale
        new_height = height * scale
        
        # Calculate position to center the image
        x = (letter[0] - new_width) / 2
        y = (letter[1] - new_height) / 2
        
        # Draw black background
        c.setFillColorRGB(0, 0, 0)  # Black
        c.rect(0, 0, letter[0], letter[1], fill=1)
        
        # Draw the image
        c.drawInlineImage(img, x, y, width=new_width, height=new_height)
        
        # Add the filename as title
        c.setFillColorRGB(1, 1, 1)  # White
        c.setFont("Arial", 14)
        c.drawString(inch, letter[1] - inch, tiff_file)
        
        c.showPage()
    
    c.save()

# Usage
#input_folder = "/path/to/your/tiff/files"
#output_pdf = "/path/to/output.pdf"
#tiff_to_pdf_with_title(input_folder, output_pdf)

def tiff_to_pdf(directory, output_filename):
    # Get all TIFF files in the directory
    tiff_files = [f for f in os.listdir(directory) if f.lower().endswith(('.tiff', '.tif'))]
    tiff_files.sort()  # Sort files to ensure consistent order

    # Create a new PDF
    c = canvas.Canvas(output_filename)

    for tiff_file in tiff_files:
        img_path = os.path.join(directory, tiff_file)
        img = Image.open(img_path)
        
        # Convert RGBA to RGB if necessary
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # Get image size
        width, height = img.size

        # Add a page to the PDF
        c.setPageSize((width, height))
        c.drawInlineImage(img, 0, 0, width, height)
        c.showPage()

    # Save the PDF
    c.save()

# Usage
if __name__=="__main__":
    directory = 'output'
    output_filename = 'output.pdf'
    tiff_to_pdf_with_title(directory, output_filename)
