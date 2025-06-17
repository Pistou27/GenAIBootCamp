import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import rotate
import numpy as np

def rotate_image_90_degrees(image):
    return rotate(image, 90, reshape=False, mode='nearest')

image_path = 'flowers\\19_010.png'
original_image = Image.open(image_path)

plt.imshow(original_image)
plt.axis('off')
plt.show()

image_array = np.array(original_image)

rotated_image = rotate_image_90_degrees(image_array)

plt.imshow(rotated_image)
plt.axis('off')
plt.show()

flip_image = np.flipud(original_image)

plt.imshow(flip_image)
plt.axis('off')
plt.show()

under_image = np.fliplr(original_image)

plt.imshow(under_image)
plt.axis('off')
plt.show()

def zoom_in(image, scale=1.2):
    width, height = image.size
    new_width = int(width * scale)
    new_height = int(height * scale)
    
    # Resize bigger
    resized = image.resize((new_width, new_height), resample=Image.LANCZOS)
    
    # Center crop to original size
    left = (new_width - width) // 2
    top = (new_height - height) // 2
    right = left + width
    bottom = top + height
    
    cropped = resized.crop((left, top, right, bottom))
    return cropped

zoomed_image = zoom_in(original_image)

plt.imshow(zoomed_image)
plt.axis('off')
plt.title("Zoomed In (1.2x)")
plt.show()