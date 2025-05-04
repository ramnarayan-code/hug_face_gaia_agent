import base64

def encode_image(image_file):
    """
    Encodes an image file to base64 string.

    Args:
        image_file (bytes): Binary image data to be encoded.

    Returns:
        str: Base64 encoded string representation of the image.

    Example:
        >>> with open('image.jpg', 'rb') as f:
        ...     image_data = f.read()
        >>> encoded = encode_image(image_data)
    """
    return base64.b64encode(image_file).decode("utf-8")
