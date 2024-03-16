import numpy as np
from PIL import Image

# Load your image
image_path = "x.png"
image = Image.open(image_path)

# Resize the image to 144x144 pixels
image = image.resize((144, 144))

# Convert the image to a NumPy array
image_array = np.array(image)

# Normalize the pixel values to range [0, 1]
normalized_image = image_array / 255.0

# Optionally, if your image has multiple channels (e.g., RGB), you can normalize each channel independently:
# for i in range(normalized_image.shape[2]):
#     channel_mean = normalized_image[:, :, i].mean()
#     channel_std = normalized_image[:, :, i].std()
#     normalized_image[:, :, i] = (normalized_image[:, :, i] - channel_mean) / channel_std

# Print the shape and normalized pixel values of the image array
print("Shape of normalized image array:", normalized_image.shape)
print("Normalized pixel values:\n", normalized_image)
