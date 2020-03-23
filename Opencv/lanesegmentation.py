#!/usr/bin/python3.7
import matplotlib.pyplot as plt
import cv2
import numpy as np
from matplotlib import rcParams

image = cv2.imread('road.jpg', cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    lower_yellow = np.array([20, 100, 100], dtype="uint8")
    upper_yellow = np.array([30, 255, 255], dtype="uint8")

    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    white_mask = cv2.inRange(gray, 215, 255)
    final_mask = cv2.bitwise_or(yellow_mask, white_mask)

    mask_image = cv2.bitwise_and(gray, final_mask)

    gaussian = cv2.GaussianBlur(mask_image, (1, 1), 0)
    canny = cv2.Canny(gaussian, 15, 200)
    print(canny.shape)
    return canny


def region_of_interest(img, canny):
    width = img.shape[1]
    height = img.shape[0]
    vertices = [
        (0, height), (width / 2, height / 2), (width, 350), (width, height)
    ]

    mask = np.zeros_like(canny)
    white = 255
    mask = cv2.fillPoly(mask, np.int32([vertices]), white)
    masked_image = cv2.bitwise_and(canny, mask)
    return masked_image


def lines(img):
    line_points = cv2.HoughLinesP(img, 1, np.pi / 360, 50, np.array([]), 2, 50)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in line_points:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), (255, 0, 0), thickness=3)
    return line_img


if __name__ == '__main__':
    canny_edge = edge(image)
    roi = region_of_interest(image, canny_edge)
    line_drawn = lines(roi)

    final_image = cv2.add(image, line_drawn)

    rcParams['figure.figsize'] = 11, 8

    grid = plt.figure()
    grid.add_subplot(2,2, 1)
    plt.imshow(image)
    grid.add_subplot(2, 2, 2)
    plt.imshow(final_image)
    grid.add_subplot(2,2,3)
    plt.imshow(canny_edge)
    grid.add_subplot(2,2,4)
    plt.imshow(line_drawn)
    plt.show(block=True)
