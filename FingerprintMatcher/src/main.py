import argparse
from loader import ImageLoader
from binarizer import Binarizer
from skeletonizer import Skeletonizer
from extractor import MinutiaeExtractor
from filter import MinutiaeFilter
from verifier import Verifier

def process(path):
    img = ImageLoader.load_image(path)
    bin_img = Binarizer.binarize(img)
    skel = Skeletonizer.skeletonize(bin_img)
    mins = MinutiaeExtractor.extract_minutiae(skel)
    return MinutiaeFilter.remove_false_minutiae(mins, skel.shape)

def main():
    p = argparse.ArgumentParser("Porównanie odcisków palców")
    p.add_argument("img1", help="pierwszy plik")
    p.add_argument("img2", help="drugi plik")
    args = p.parse_args()

    m1 = process(args.img1)
    m2 = process(args.img2)

    sim, dec = Verifier().verify(m1, m2)
    print(f"Podobieństwo: {sim:.2f}%")
    print(f"Czy ta sama osoba? {dec}")

if __name__ == "__main__":
    main()
