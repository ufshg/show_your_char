# Show Your Character!

## 당신의 영상에 좋아하는 문자를 띄워봅시다.

이 레포지토리에 포함된 파일들은 다음과 같습니다.

- camera_calibration.py - 현재 경로의 chessboard.mp4 영상을 기반으로 카메라 캘리브레이션을 수행합니다.

- data.pkl - 캘리브레이션 결과값이 저장됩니다.

- calibration_result.py - data.pkl에 저장된 데이터를 보여줍니다.

- pose_estimation_chessboard.py - data.pkl의 데이터를 토대로 chessboard.mp4에 AR을 수행합니다.

- sample.gif - pose_estimation-chessboard.py 실행 예시

## 사용 방법

1. 파이썬 라이브러리 다운로드

   ```
   pip install numpy
   pip install opencv-python opencv-contrib-python
   ```

2. chessboard.mp4 파일 준비 및 캘리브레이션 수행

   현재 경로에 체스보드를 촬영한 chessboard.mp4를 준비하고, camera_calibration.py를 실행합니다.

   새 창에 영상이 표시되면, 스페이스바를 눌러 영상이 일시정지되고 체스보드에 마커가 표시되는 것을 확인합니다.

   마커가 표시되면 엔터 키를 눌러 해당 일시정지 화면을 저장합니다. 이 과정을 3번 이상 반복합니다.

   데이터는 data.pkl에 저장되며 제 환경에서의 캘리브레이션 값은 다음과 같습니다.

   ```
   K : [[1.69095036e+03 0.00000000e+00 9.60819324e+02]
        [0.00000000e+00 1.69416247e+03 5.75458768e+02]
        [0.00000000e+00 0.00000000e+00 1.00000000e+00]]

   dist_coeff : [ 7.81799444e-02 -7.80905658e-01  6.37339889e-04  3.16518348e-03 3.13525086e+00]
   ```

3. AR 수행

   pose_estimation_chessboard.py를 실행해 AR 수행 결과를 확인합니다.

   ![ex_screenshot](https://github.com/ufshg/show_your_char/blob/main/smaple.gif?raw=true)
