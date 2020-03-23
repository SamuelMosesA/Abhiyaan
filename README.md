# Abhiyaan
Submission for Team Abhiyaan
============================

## Name:
A Samuel Moses

## Roll Number:
CS19B003

## Previous Experience:
not much apart from small personal projects.

## Current PORs:
None

## Why I want to join
To get to work on useful products so that stuff I learn actually gets used

## Relevant Courses:
In Institute
CS1111
CS1200

Passed
Doing

## Online
Doing Andrew NG Machine Learning 

### References
- publisher and subscriber : ROS Tutorial
- turtle exercise : http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal
- lane segmentation : CVI club assignment

# Approach to problem
### B.3  1.Lane segmentation
- Select the road using a mask
- Select the yellow and white colors using a mask
- Use gaussian blur to smoothen and apply Canny edge detection
- Use Probabilistic Hough lines to draw lines and overlay it on the original image

### B.2 Bot controller
- we can use bot velocity to calculate current position from start
- select an obstacle/wall or any reference which can be detected by sensor 
- we can use calculated position and position from sensor to find the deviation and use it for correction at regular intervals

### B.3 2a 
- use contours to find circles on the grayscale image
- use moments to find the centre of circle
- check the point colors on the oringinal pic converted to hsv and check the color
- then the color apart from grey can be found and given as answer
