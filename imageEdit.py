from PIL import Image
import os

# Define the source and destination directories
source_folder = "/Users/ariel/Desktop/lab/CCDL/LFM2/LFM2day2/LFM2_new/originalimg"
destination_folder = "/Users/ariel/Desktop/lab/CCDL/LFM2/LFM2day2/LFM2_new/croppedimg"

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Iterate over each image file in the source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        img_path = os.path.join(source_folder, filename)
        
        # Open the image
        with Image.open(img_path) as img:
            width, height = img.size
            
            # Calculate the cropping box centered on the original image
            left = (width - 1000) // 2
            top = (height - 1000) // 2
            right = left + 1000
            bottom = top + 1000
            
            # Ensure the crop size doesn't exceed the image dimensions
            if width >= 600 and height >= 600:
                cropped_img = img.crop((left, top, right, bottom))
                
                # Save the cropped image to the destination folder
                cropped_img.save(os.path.join(destination_folder, filename))
                print(f"Cropped and saved {filename}")
            else:
                print(f"Skipped {filename}: Image is smaller than 600x600")
