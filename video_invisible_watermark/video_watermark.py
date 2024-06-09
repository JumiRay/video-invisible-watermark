import cv2
import numpy as np
from scipy.fftpack import dct, idct
from PIL import Image
import os


def load_image(image_path, size=(100, 100)):
    """加载并调整图像大小"""
    img = Image.open(image_path).convert('L')
    img = img.resize(size, Image.LANCZOS)
    return np.array(img)


def embed_watermark_to_frame(frame, img):
    """将图像嵌入到整个帧（使用DCT）"""
    rows, cols, _ = frame.shape
    yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(yuv_frame)

    # 对 Y 组件进行 DCT 变换
    dct_y = dct(dct(y.T, norm='ortho').T, norm='ortho')

    # 将图像嵌入 DCT 系数中
    img_rows, img_cols = img.shape
    y_start, x_start = (rows - img_rows) // 2, (cols - img_cols) // 2
    dct_y[y_start:y_start + img_rows, x_start:x_start + img_cols] = img

    # 对 Y 组件进行逆 DCT 变换
    idct_y = idct(idct(dct_y.T, norm='ortho').T, norm='ortho')
    y = np.clip(idct_y, 0, 255).astype(np.uint8)  # 确保像素值在0-255之间

    # 合并 Y, U, V 组件
    yuv_frame = cv2.merge((y, u, v))
    frame_with_message = cv2.cvtColor(yuv_frame, cv2.COLOR_YUV2BGR)
    return frame_with_message


def extract_watermark_from_frame(frame, img_size=(100, 100)):
    """从整个帧提取图像（使用DCT）"""
    rows, cols, _ = frame.shape
    yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(yuv_frame)

    # 对 Y 组件进行 DCT 变换
    dct_y = dct(dct(y.T, norm='ortho').T, norm='ortho')

    # 提取 DCT 系数中的图像
    img_rows, img_cols = img_size
    y_start, x_start = (rows - img_rows) // 2, (cols - img_cols) // 2
    extracted_img = dct_y[y_start:y_start + img_rows, x_start:x_start + img_cols]
    extracted_img = np.round(extracted_img).astype(np.uint8)

    return extracted_img


def video_to_frames(video_path, duration=10, fps=30):
    """将视频分解为帧"""
    vidcap = cv2.VideoCapture(video_path)
    frames = []
    total_frames = int(fps * duration)
    for _ in range(total_frames):
        success, image = vidcap.read()
        if not success:
            break
        frames.append(image)
    vidcap.release()
    return frames


def frames_to_video(frames, output_path, fps, size):
    """将帧重组为视频"""
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for frame in frames:
        out.write(frame)
    out.release()


def save_images(images, prefix='result/pre_compression'):
    """保存图像到指定目录"""
    if not os.path.exists(prefix):
        os.makedirs(prefix)
    for i, img in enumerate(images):
        img_path = os.path.join(prefix, f'{i}.jpg')
        img.save(img_path)


def embed_watermark_to_video(input_video_path, output_video_path, watermark_path, duration=10, fps=30):
    watermark_img = load_image(watermark_path)
    frames = video_to_frames(input_video_path, duration)
    frames_with_message = [embed_watermark_to_frame(frame, watermark_img) for frame in frames]
    size = (frames[0].shape[1], frames[0].shape[0])
    frames_to_video(frames_with_message, output_video_path, fps, size)


def extract_watermark_from_video(output_video_path, prefix='compression', duration=10):
    output_frames = video_to_frames(output_video_path, duration)  # 解析前2秒
    post_compression_imgs = [extract_watermark_from_frame(frame) for frame in output_frames]
    post_compression_texts = [Image.fromarray(img) for img in post_compression_imgs]
    save_images(post_compression_texts, prefix)
