#!/usr/bin/env python

import cv2
import numpy as np

# Read Image
im = cv2.imread("MF_30deg.png")
size = im.shape

# 2D image points. If you change the image, you need to change vector
image_points = np.array([
    (740, 313),  # Nose tip
#    (709, 395),  # Chin
    (682, 265),  # Left eye left corner
    (752, 274),  # Right eye right corner
    (687, 347),  # Left Mouth corner
    (730, 352)  # Right mouth corner
], dtype="double")

# 3D model points.
model_points = np.array([
    (0.0, 0.0, 0.0),  # Nose tip
    (-225.0, 170.0, -135.0),  # Left eye left corner
    (225.0, 170.0, -135.0),  # Right eye right corne
    (-150.0, -150.0, -125.0),  # Left Mouth corner
    (150.0, -150.0, -125.0)  # Right mouth corner
])

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
    cv2.solvePnP(model_points[0:4], image_points[0:4], camera_matrix, dist_coeffs)
    #cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

print("Rotation Vector:\n {0}".format(rotation_vector))
print("Translation Vector:\n {0}".format(translation_vector))

rotation_matrix = np.zeros((3, 3))
cv2.Rodrigues(rotation_vector, rotation_matrix)
print("rotation_matrix:\n {0}".format(rotation_matrix))

# verfication
xv = np.array([rotation_matrix[0][0], rotation_matrix[1][0], rotation_matrix[2][0]])
print(np.transpose(xv).dot(xv))


# draw axes
axis_length = 1000.0

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
print('Z_pnt:%d,%d' % (p2[0], p2[1]))
cv2.line(im, p1, p2, (255, 0, 0), 2)
p1 = (int(Org_pnt[0][0][0]), int(Org_pnt[0][0][1]))
p2 = (int(Y_pnt[0][0][0]), int(Y_pnt[0][0][1]))
print('Y_pnt:%d,%d' % (p2[0], p2[1]))
cv2.line(im, p1, p2, (0, 255, 0), 2)
p1 = (int(Org_pnt[0][0][0]), int(Org_pnt[0][0][1]))
p2 = (int(X_pnt[0][0][0]), int(X_pnt[0][0][1]))
print('X_pnt:%d,%d' % (p2[0], p2[1]))
cv2.line(im, p1, p2, (0, 255, 255), 2)
# Display image
cv2.imshow("Output", im)
cv2.waitKey(0)
