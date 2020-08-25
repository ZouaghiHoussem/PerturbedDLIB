import numpy as np
import cv2
import argparse
import os
import sys
from utils import *


def main(args):
    input_path = os.path.abspath(args.imagePath)
    output_path = os.path.abspath(args.output_path)

    # test inputs
    if not os.path.isfile(input_path):
        print("Error loading the image, image not found")
        sys.exit()

    fname = os.path.basename(input_path).split('.')[0]

    # if the input is an image
    if is_image(input_path):
        if os.path.basename(output_path).find('.') == -1:
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            output_name = "{}_landmarks.{}".format(fname, os.path.basename(input_path).split('.')[1])
        else:
            output_name = os.path.basename(output_path)
            output_path = os.path.dirname(output_path)

        img = cv2.imread(input_path)
        _, _, perturbed_kpt = perturb_bbox(img)
        cv2.imwrite(os.path.join(output_path, output_name), plot_kpt(img, perturbed_kpt))
        np.save(os.path.join(output_path, "{}_landmarks.npy".format(output_name)), perturbed_kpt)

    # if the input is a video
    elif is_video(input_path):
        # check existence of the output folder
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        # landmarks data
        landmarks = np.empty(shape=(68, 2, 0))

        # extract the frames
        input_video = cv2.VideoCapture(input_path)
        success, image = input_video.read()
        count = 0
        if not success:
            print('Error: unable to read {} with OpenCV'.format(input_path))
        while success:
            # compute the perturbed landmarks
            _, _, perturbed_kpt = perturb_bbox(image)
            landmarks = np.append(landmarks, perturbed_kpt[:, :, np.newaxis], axis=2)

            # saving file
            cv2.imwrite(os.path.join(output_path, "frame-%04d.jpg" % count), plot_kpt(image, perturbed_kpt))

            # next frame
            success, image = input_video.read()
            print('Written frame %d' % count)
            count += 1
            if count > 5:
                break
        np.save(os.path.join(output_path, "{}_landmarks.npy".format(fname)), landmarks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='realign the reenacted')
    parser.add_argument('-i', '--imagePath', required=True, type=str, help='the input image')
    parser.add_argument('-o', '--output_path', required=True, type=str, help='the output path')

    main(parser.parse_args())



