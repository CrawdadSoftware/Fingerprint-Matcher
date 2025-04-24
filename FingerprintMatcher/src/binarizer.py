import cv2

class Binarizer:
    """Binaryzacja przy pomocy progu Otsu."""
    @staticmethod
    def binarize(image):
        _, binary = cv2.threshold(
            image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        return binary
