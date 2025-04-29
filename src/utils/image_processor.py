from PIL import Image
import numpy as np

def resize_image(image_path, size):
    image = Image.open(image_path)
    resized_image = image.resize(size)
    return resized_image

def filter_image(image_path, filter_type):
    image = Image.open(image_path)
    if filter_type == 'grayscale':
        filtered_image = image.convert('L')
    elif filter_type == 'blur':
        from PIL import ImageFilter
        filtered_image = image.filter(ImageFilter.BLUR)
    else:
        raise ValueError("Unsupported filter type")
    return filtered_image

def prepare_image_for_analysis(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    image_array = np.array(image)
    return image_array