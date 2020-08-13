import numpy as np
import cv2
import argparse
import os
import sys

from utils import *

def main(args):
    img_path = os.path.abspath(args.imagePath)
    output_path = os.path.abspath(args.output_path)

    if not os.path.isfile(img_path):
        print("Error loading the image, image not found")
        sys.exit()

    if not output_path[-4] == ".":
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        fname = os.path.basename(img_path).split('.')[0]
        output_path = os.path.join(output_path, "{}_landmarks.jpg".format(fname))


    img = cv2.imread(img_path)
    bbox, original_kpt, perturbed_kpt = perturb_bbox(img)
    print(output_path)
    cv2.imwrite(output_path, plot_kpt(img, perturbed_kpt))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='realign the reenacted')
    parser.add_argument('-i', '--imagePath', required=True, type=str, help='the input image')
    parser.add_argument('-o', '--output_path', required=True, type=str, help='the output path')

    main(parser.parse_args())



