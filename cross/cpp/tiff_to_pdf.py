import os
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.backends.backend_pdf import PdfPages

def tiff_to_pdf_with_title(input_folder, output_pdf):
    # Get all TIFF files in the input folder
    tiff_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.tif', '.tiff'))]
    
    # Create a PDF
    with PdfPages(output_pdf) as pdf:
        for tiff_file in tiff_files:
            # Open the TIFF image
            img_path = os.path.join(input_folder, tiff_file)
            img = Image.open(img_path)
            
            # Create a new figure
            fig, ax = plt.subplots(figsize=(8.5, 11))  # Letter size
            
            # Display the image
            ax.imshow(img)
            
            # Remove axes
            ax.axis('off')
            
            # Set the title (filename)
            plt.title(tiff_file, fontsize=12)
            
            # Adjust layout to make room for the title
            plt.tight_layout()
            
            # Save the page
            pdf.savefig(fig)
            
            # Close the figure to free up memory
            plt.close(fig)

# Usage
input_folder = "output"
output_pdf = "output.pdf"
tiff_to_pdf_with_title(input_folder, output_pdf)
