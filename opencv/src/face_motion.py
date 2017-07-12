#!/usr/bin/env python

import os
import cv2
import numpy as np
import math


# 3D model points.
model_points = np.array([
    (0.0, 0.0, 0.0),  # Nose tip
    (-50.0, -40.0, 20.0),  # Left eye left corner
    (50.0, -40.0, 20.0),  # Right eye right corner
    (-27.5, 30.0, 10.0),  # Left Mouth corner
    (27.5, 30.0, 10.0)  # Right mouth corner
])

index = 4
points_file = "points.txt"
image_file = []
key_points = []
matrix = []
if not os.path.exists(points_file):
    print('do not have file %s' % points_file)
    exit(0)
points_f = open(points_file, 'r')

for line in points_f:
    a = line.split('|')
    b = a[0].split(',')
    image_file.append(b[0])
    key_points.append(b[1:11])
    matrix.append(a[1].split(','))

points_f.close()

image_points = np.array([
    (int(key_points[index][0]), int(key_points[index][5])),  # Nose tip
    (int(key_points[index][1]), int(key_points[index][6])),  # Left eye left corner
    (int(key_points[index][2]), int(key_points[index][7])),  # Right eye right corner
    (int(key_points[index][3]), int(key_points[index][8])),  # Left Mouth corner
    (int(key_points[index][4]), int(key_points[index][9]))  # Right mouth corner
], dtype="double")

# Read Image
im = cv2.imread(image_file[index])
size = im.shape

# 2D image points. If you change the image, you need to change vector

def print_rotation_angle(R):
    V = R.dot(np.array([0, 0, 1]))
    print('\033[92mV:', V)
    print('phi = %f degree' % math.degrees(math.atan(V[0] / V[2])))
    print('theta = %f degree' % math.degrees(math.acos(math.sqrt(V[0]**2 + V[2]**2))))

# Camera internals
focal_length = size[1]
center = (size[1] / 2, size[0] / 2)
camera_matrix = np.array(
    [[focal_length, 0, center[0]],
     [0, focal_length, center[1]],
     [0, 0, 1]], dtype="double"
)

print("Camera Matrix :\n {0}".format(camera_matrix))

dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
(success, rotation_vector, translation_vector) = \
    cv2.solvePnP(model_points[0:4], image_points[0:4], camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

#print("Rotation Vector:\n {0}".format(rotation_vector))
#print("Translation Vector:\n {0}".format(translation_vector))

rotation_matrix = np.zeros((3, 3))
cv2.Rodrigues(rotation_vector, rotation_matrix)
R = np.c_[rotation_matrix, translation_vector]
print("rotation_matrix:\n {0}".format(R))

print_rotation_angle(rotation_matrix)

# draw axes
axis_length = 100.0

(Org_pnt, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 0.0)]), rotation_vector, translation_vector,
                                                 camera_matrix, dist_coeffs)
(Z_pnt, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, axis_length)]), rotation_vector, translation_vector,
                                                 camera_matrix, dist_coeffs)
(Y_pnt, jacobian) = cv2.projectPoints(np.array([(0.0, axis_length, 0.0)]), rotation_vector, translation_vector,
                                                 camera_matrix, dist_coeffs)
(X_pnt, jacobian) = cv2.projectPoints(np.array([(axis_length, 0.0, 0.0)]), rotation_vector, translation_vector,
                                                 camera_matrix, dist_coeffs)
for p in image_points:
    cv2.circle(im, (int(p[0]), int(p[1])), 3, (0, 0, 255), -1)

p1 = (int(Org_pnt[0][0][0]), int(Org_pnt[0][0][1]))
p2 = (int(Z_pnt[0][0][0]), int(Z_pnt[0][0][1]))
#print('Org_pnt:%d,%d' % (p1[0], p1[1]))
#print('Z_pnt:%d,%d' % (p2[0], p2[1]))
cv2.line(im, p1, p2, (255, 0, 0), 2)
p1 = (int(Org_pnt[0][0][0]), int(Org_pnt[0][0][1]))
p2 = (int(Y_pnt[0][0][0]), int(Y_pnt[0][0][1]))
#print('Y_pnt:%d,%d' % (p2[0], p2[1]))
cv2.line(im, p1, p2, (0, 255, 0), 2)
p1 = (int(Org_pnt[0][0][0]), int(Org_pnt[0][0][1]))
p2 = (int(X_pnt[0][0][0]), int(X_pnt[0][0][1]))
#print('X_pnt:%d,%d' % (p2[0], p2[1]))
cv2.line(im, p1, p2, (0, 255, 255), 2)
# Display image
cv2.imshow("Output", im)
cv2.waitKey(0)
