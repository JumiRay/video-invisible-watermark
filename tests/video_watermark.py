import unittest
import cv2
import os

from video_invisible_watermark import (
    video_to_frames,
    frames_to_video,
    embed_watermark_to_frame,
    extract_watermark_from_frame,
    embed_watermark_to_video,
    extract_watermark_from_video
)


class TestVideoWatermark(unittest.TestCase):
    def setUp(self):
        # 示例用法
        input_video_path = 'input_video.mp4'
        output_video_path = 'output_video_with_hidden_message.mp4'
        watermark_path = 'markma.jpeg'
        embed_watermark_to_video(input_video_path, output_video_path,watermark_path, 1)
        extract_watermark_from_video(output_video_path, 'results', 1)
if __name__ == '__main__':
    unittest.main()
