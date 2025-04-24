import cv2

class ImageLoader:
    """Wczytuje obraz do skali szarości."""
    @staticmethod
    def load_image(path: str):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError(f"Nie można wczytać obrazu: {path}")
        return img
