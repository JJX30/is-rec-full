import cv2 as cv
from cv2 import GaussianBlur
from PIL import Image
from io import BytesIO
import requests


def get_person_count(img1, img2, type):
    if type == "student-rec":
        cvimg1 = cv.imread(img1)
        cvimg2 = cv.imread(img2)

        person_count = 0

        # rectangle to block windows
        cv.rectangle(cvimg1, (30, 0), (300, 350), (0, 0, 0), thickness=-1)
        cv.rectangle(cvimg2, (30, 0), (300, 350), (0, 0, 0), thickness=-1)

        cv.rectangle(cvimg1, (80, 350), (300, 500), (0, 0, 0), thickness=-1)
        cv.rectangle(cvimg2, (80, 350), (300, 500), (0, 0, 0), thickness=-1)

        cv.rectangle(cvimg1, (500, 0), (1800, 200), (0, 0, 0), thickness=-1)
        cv.rectangle(cvimg2, (500, 0), (1800, 200), (0, 0, 0), thickness=-1)

        diff = cv.absdiff(cvimg1, cvimg2)
        gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
        blur = GaussianBlur(gray, (5, 5), 0)

        _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
        dialated = cv.dilate(thresh, None, iterations=3)
        contours, _ = cv.findContours(
            dialated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv.boundingRect(contour)

            if cv.contourArea(contour) < 2000:
                continue
            cv.rectangle(cvimg1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            person_count = person_count + 1

        return person_count
    elif type == "southwest-rec":
        # same code as above but for southwest rec and different rectangles
        return 0
