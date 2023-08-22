import os
import cv2

# 设置输入图片文件夹路径、输出视频文件名和帧率
input_images_folder = 'D'
output_video_name = 'D.mp4'
frame_rate = 24  # 帧率，每秒钟播放的图片数

# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(input_images_folder) if f.endswith('.jpg') or f.endswith('.png')]

# 获取第一张图片的尺寸，用于设置视频的宽高
first_image_path = os.path.join(input_images_folder, image_files[0])
first_image = cv2.imread(first_image_path)
height, width, layers = first_image.shape

# 初始化VideoWriter对象，用于创建视频文件
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 设置视频编码器
out = cv2.VideoWriter(output_video_name, fourcc, frame_rate, (width, height))

# 遍历所有图片，将它们写入视频
for image_file in image_files:
    image_path = os.path.join(input_images_folder, image_file)
    image = cv2.imread(image_path)
    out.write(image)

# 释放VideoWriter对象和关闭窗口
out.release()
cv2.destroyAllWindows()

print("视频已创建：", output_video_name)
