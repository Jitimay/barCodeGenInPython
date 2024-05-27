import barcode
from barcode.writer import ImageWriter
import os

# Ensure the directory for barcodes exists
output_dir = 'barcodes'
os.makedirs(output_dir, exist_ok=True)

# List of data for which barcodes need to be generated
data_list = [f"product{i:04d}" for i in range(1, 1001)]  # Generate data for 1000 products

# Generate and save barcodes
for data in data_list:
    # Create a barcode object
    code128 = barcode.get_barcode_class('code128')
    code = code128(data, writer=ImageWriter())

    # Save the barcode as an image file
    filename = os.path.join(output_dir, f"{data}.png")
    code.save(filename)

print(f"Generated {len(data_list)} barcodes in the '{output_dir}' directory.")
