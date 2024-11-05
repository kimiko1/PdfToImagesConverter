# 🖼️ PDF to Images Converter

This project converts each page of a PDF file into individual PNG images. It is useful in several contexts:

- Generating visual previews of PDF pages for display on websites.
- Processing documents for image recognition or OCR (Optical Character Recognition) operations.
- Facilitating PDF document browsing in an image format, such as a flipbook.

## 📋 Project Overview

This Python script leverages the `pdf2image` library to convert PDFs into high-resolution images. Each page of the PDF is saved as a separate PNG file, and the images are stored in a dedicated output folder, named after the PDF file.

## 🚀 How It Works

### 1. Extract the File Name for Output Folder
The script extracts the PDF file name (without the extension) and creates a folder with this name to store the converted images.

### 2. Create the Output Folder
A folder named after the PDF is created (if it doesn't exist already) to store the generated images.

### 3. Convert the PDF to Images
- The PDF is converted into a list of images using the `convert_from_path` function from `pdf2image`.
- The image resolution is set to 400 DPI (dots per inch) to ensure high quality.
- The output format for the images is PNG.

### 4. Save the Images with Formatted Filenames
- Each PDF page is saved as a distinct image, with a filename formatted to 3 digits (e.g., `001.png`, `002.png`, etc.).
- The images are saved in the newly created output folder.

### 5. Measure the Execution Time
The total time taken to convert the PDF is measured and displayed for performance tracking.

### 6. Error Handling
If an error occurs (e.g., a corrupted PDF file), the exception is caught, and an error message is displayed.

### 7. Pre-check for PDF File Existence
Before starting the conversion, the script checks if the specified PDF file exists. If not, an error message is shown.

## 📂 Example Usage

In this example, the PDF file `SSV.pdf` is converted into images, and each image is saved with a sequential number (e.g., `001.png`, `002.png`, etc.) in a folder named `SSV`.

```python
from pdf2image import convert_from_path
import os
import time

def convert_pdf_to_images(pdf_path):
    # Extract filename without extension for output folder name
    base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = f"{base_filename}"
    
    # Create output folder
    os.makedirs(output_folder, exist_ok=True)
    print(f"Output folder: {output_folder}")

    try:
        # Start timer
        start_time = time.time()
        
        # Convert PDF to a list of images
        print(f"Converting PDF: {pdf_path}")
        images = convert_from_path(pdf_path, dpi=400, fmt="png")
        print(f"Number of pages converted: {len(images)}")

        # Save each image with formatted filename (3 digits)
        image_paths = []
        for i, image in enumerate(images, start=1):
            image_name = f"{i:03}.png"
            image_path = os.path.join(output_folder, image_name)
            image.save(image_path, "PNG")
            image_paths.append(image_path)
            print(f"Image saved: {image_path}")
        
        # Display total elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total conversion time: {elapsed_time:.2f} seconds")

        return image_paths
    except Exception as e:
        print(f"Error during conversion: {e}")
        return []

# Example: Converting the PDF file
pdf_path = "pdf/SSV.pdf"

# Check if the PDF file exists before converting
if os.path.exists(pdf_path):
    images = convert_pdf_to_images(pdf_path)
    if images:
        print("Images converted:", images)
    else:
        print("No images were converted.")
else:
    print(f"Error: PDF file not found -> {pdf_path}")
```

## 🔧 Potential Use Cases

- Thumbnail generation for a quick preview of PDF pages.
- Image usage in interactive interfaces, such as flipbooks or galleries.
- Extracting visual elements from PDF documents for further processing.

## 📑 Requirements

- pdf2image
- Pillow
- poppler-utils (required for pdf2image to work)
