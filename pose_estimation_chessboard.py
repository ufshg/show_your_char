import numpy as np
import pickle
import cv2 as cv
import random as r

def rand():
    return r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)

# The given video and calibration data
input_file = './chessboard.mp4'
with open("data.pkl", 'rb') as f:
    data = pickle.load(f)

K = data["K"]
dist_coeff = data["dist_coeff"]

board_pattern = (10, 7)
board_cellsize = 0.025
board_criteria = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE + cv.CALIB_CB_FAST_CHECK

# Open a video
video = cv.VideoCapture(input_file)
assert video.isOpened(), 'Cannot read the given input, ' + input_file

base = [[7, 2], [7, 1], [6, 0], [3, 0], [2, 1], [2, 2], [3, 3], [6, 4], [5, 5], [4, 5], [3, 4], [2, 4], [2, 5], [3, 6], [6, 6], [7, 5], [7, 4], [6, 3], [3, 2], [4, 1], [5, 1], [6, 2]]

# Prepare a 3D box for simple AR
box_lower = board_cellsize * np.array([(i[0], i[1], 0) for i in base])
box_upper = board_cellsize * np.array([(i[0], i[1], -1) for i in base])

# Prepare 3D points on a chessboard
obj_points = board_cellsize * np.array([[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])])

# Run pose estimation
while True:
    # Read an image from the video
    valid, img = video.read()
    if not valid:
        break

    # Estimate the camera pose
    complete, img_points = cv.findChessboardCorners(img, board_pattern, board_criteria)
    if complete:
        ret, rvec, tvec = cv.solvePnP(obj_points, img_points, K, dist_coeff)

        # Draw the box on the image
        line_lower, _ = cv.projectPoints(box_lower, rvec, tvec, K, dist_coeff)
        line_upper, _ = cv.projectPoints(box_upper, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_lower)], True, rand(), 2)
        cv.polylines(img, [np.int32(line_upper)], True, rand(), 2)
        for b, t in zip(line_lower, line_upper):
            cv.line(img, np.int32(b.flatten()), np.int32(t.flatten()), rand(), 2)

        # Print the camera position
        R, _ = cv.Rodrigues(rvec) # Alternative) scipy.spatial.transform.Rotation
        p = (-R.T @ tvec).flatten()
        info = f'XYZ: [{p[0]:.3f} {p[1]:.3f} {p[2]:.3f}]'
        cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

    # Show the image and process the key event
    cv.imshow('Pose Estimation (Chessboard)', img)
    key = cv.waitKey(10)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27: # ESC
        break

video.release()
cv.destroyAllWindows()
