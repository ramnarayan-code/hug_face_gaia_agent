from PIL import Image
import numpy as np

class ImageAnalysisTool:
    def analyze(self, image_path):
        image = Image.open(image_path)
        image_data = np.array(image)

        # Example analysis: Get image size and mean color
        width, height = image.size
        mean_color = image_data.mean(axis=(0, 1))

        insights = {
            "width": width,
            "height": height,
            "mean_color": mean_color.tolist()  # Convert to list for easier readability
        }

        return insights