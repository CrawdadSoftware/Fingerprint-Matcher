from skimage.morphology import skeletonize
import numpy as np

class Skeletonizer:
    """Redukuje ścieżki do 1-pikselowego szkieletonu."""
    @staticmethod
    def skeletonize(binary_image):
        binary_bool = binary_image == 255
        skel = skeletonize(binary_bool)
        return (skel.astype(np.uint8) * 255)
