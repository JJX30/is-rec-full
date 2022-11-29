import cv2 as cv
from cv2 import GaussianBlur

img1 = cv.imread("cam8-10.jpeg")

img2 = cv.imread("cam8-11.jpeg")

person_count = 0

# rectangle to block windows
cv.rectangle(img1, (30, 0), (300, 350), (0, 0, 0), thickness=-1)
cv.rectangle(img2, (30, 0), (300, 350), (0, 0, 0), thickness=-1)

cv.rectangle(img1, (80, 350), (300, 500), (0, 0, 0), thickness=-1)
cv.rectangle(img2, (80, 350), (300, 500), (0, 0, 0), thickness=-1)

cv.rectangle(img1, (500, 0), (1800, 200), (0, 0, 0), thickness=-1)
cv.rectangle(img2, (500, 0), (1800, 200), (0, 0, 0), thickness=-1)


diff = cv.absdiff(img1, img2)
gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
blur = GaussianBlur(gray, (5, 5), 0)

_, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
dialated = cv.dilate(thresh, None, iterations=3)
contours, _ = cv.findContours(dialated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    (x, y, w, h) = cv.boundingRect(contour)

    if cv.contourArea(contour) < 2000:
        continue
    cv.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), 2)
    person_count = person_count + 1


cv.imshow("result", img1)
print(person_count)


cv.destroyAllWindows()
