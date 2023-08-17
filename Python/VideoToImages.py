import cv2
import os

# 视频文件路径
video_path = '视频源.mp4'

# 输出帧保存的文件夹路径
output_folder = 'output/'

# 创建保存帧的文件夹
os.makedirs(output_folder, exist_ok=True)

# 打开视频文件
cap = cv2.VideoCapture(video_path)

frame_count = 0

while True:
    # 读取一帧
    ret, frame = cap.read()

    if not ret:
        break

    # 构造帧文件名
    frame_filename = os.path.join(output_folder, f'frame_{frame_count:04d}.png')

    # 保存帧到文件夹
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

    # 显示当前处理的帧数
    print(f"Processed frame {frame_count}")

# 释放视频对象
cap.release()
