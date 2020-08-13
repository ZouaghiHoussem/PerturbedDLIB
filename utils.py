import numpy as np
import dlib
from dlib import rectangle
import cv2
from imutils import face_utils


def plot_kpt(image, kpt, dot_color=(255, 0, 0)):
    image = image.copy()
    kpt = np.round(kpt).astype(np.int32)
    for i in range(kpt.shape[0]):
        st = kpt[i, :2]
        image = cv2.circle(image,(st[0], st[1]), 1, dot_color, 2)
    return image


def rect_to_bbox(rect):
    return np.array([rect.left(), rect.top(), rect.right(), rect.bottom()]).reshape(1, 4)


def perturb_bbox(image, nb_transformation=9, beta=0.05):

    landmarks = np.empty(shape=(68, 2, 0))

    # prepare the detector
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("./data/shapePredictor.dat")

    # recuperate the original bounding box
    original_rect = detector(image, 1)[0]

    original_width = original_rect.width()

    # get landmarks
    shape = predictor(image, original_rect)
    original_landmarks = face_utils.shape_to_np(shape)
    landmarks = np.append(landmarks, original_landmarks[:, :, np.newaxis], axis=2)

    # compute the transformation scale
    transformation_scale = beta * original_width
    for index in range(0, nb_transformation):
        new_left = original_rect.left() + int(np.random.uniform(-transformation_scale, transformation_scale))
        new_top = original_rect.top() + int(np.random.uniform(-transformation_scale, transformation_scale))
        new_rect = rectangle(new_left, new_top, new_left + original_width, new_top + original_width)

        shape_p = predictor(image, new_rect)
        landmarks_p = face_utils.shape_to_np(shape_p)
        landmarks = np.append(landmarks, landmarks_p[:, :, np.newaxis], axis=2)

    av_landmarks = np.average(landmarks, axis=2)

    return rect_to_bbox(original_rect), original_landmarks, av_landmarks
