from PIL import Image
import os

def resolution_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    files = os.listdir(input_folder)
    
    for file in files:
        # Open the image
        image_path = os.path.join(input_folder, file)
        try:
            image = Image.open(image_path)
            fileName = file.split('.')[0]
            
            # Save the image with the specified DPI
            output_path = os.path.join(output_folder, f"{fileName}.png")
            image.save(output_path, format='PNG', dpi=(600, 600))
            print(f"{file} processed and saved as {output_path}")
        except Exception as e:
            print(f"Error processing {file}: {e}")

input_folder = "input_images"
output_folder = "resoluted_images"
resolution_images(input_folder, output_folder)
