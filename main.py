import numpy as np
import cv2 as cv

# 체스보드의 2D 좌표 xs1, xs2
xs1 = np.array([[320, 240], [324, 244], [328, 248], [332, 252], [336, 256], [340, 260],
               [320, 260], [324, 256], [328, 252], [332, 248], [336, 244], [340, 240],
               [320, 280], [324, 276], [328, 272], [332, 268], [336, 264], [340, 260]], dtype=np.float32)
xs2 = np.array([[520, 340], [524, 344], [528, 348], [532, 352], [536, 356], [540, 360],
               [520, 360], [524, 356], [528, 352], [532, 348], [536, 344], [540, 340],
               [520, 380], [524, 376], [528, 372], [532, 368], [536, 364], [540, 360]], dtype=np.float32)

# 체스보드 3D 좌표 생성
rows, cols = 5, 6
square_size = 0.03  # m
world_points = np.zeros((rows*cols, 3), np.float32)
world_points[:, :2] = np.mgrid[0:cols, 0:rows].T.reshape(-1, 2) * square_size

image_points = [xs1, xs2]

# 카메라 행렬 계산
_, K, dist, _, _ = cv.calibrateCamera(world_points, image_points, (640, 480))
print("K = ")
print(K)