import cv2 as cv

img = cv.imread('Photos/illustr.png')
cv.imshow('Illustration', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Illustration_gray', gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)


cv.waitKey(0)