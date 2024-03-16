from PIL import Image
import os

def mirror_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    files = os.listdir(input_folder)
    
    for file in files:
        # Open the image
        image_path = os.path.join(input_folder, file)
        try:
            image = Image.open(image_path)
            
            # Mirror the image horizontally
            mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            
            # Save the mirrored image to the output folder
            output_path = os.path.join(output_folder, file)
            mirrored_image.save(output_path)
            print(f"Mirrored {file} and saved as {output_path}")
        except Exception as e:
            print(f"Error processing {file}: {e}")

input_folder = "input_images"
output_folder = "mirrored_images"
mirror_images(input_folder, output_folder)