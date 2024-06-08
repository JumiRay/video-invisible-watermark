import unittest
import cv2
import os

from video_invisible_watermark import (
    video_to_frames,
    frames_to_video,
    embed_message_to_frames,
    extract_message_from_frames
)


class TestVideoWatermark(unittest.TestCase):
    def setUp(self):
        self.video_path = "./test_video.mp4"
        self.output_path = "./output_video.mp4"
        self.hidden_message = "Hello World"
        self.frames = video_to_frames(self.video_path)
        self.fps = 30
        self.size = (self.frames[0].shape[1], self.frames[0].shape[0])

    def test_embed_and_extract_message(self):
        frames_with_message = embed_message_to_frames(self.frames, self.hidden_message)
        extracted_messages = extract_message_from_frames(frames_with_message)
        print(extracted_messages)
        self.assertIn(self.hidden_message, extracted_messages)

    def test_video_output(self):
        frames_with_message = embed_message_to_frames(self.frames, self.hidden_message)
        frames_to_video(frames_with_message, self.output_path, self.fps, self.size)
        self.assertTrue(os.path.exists(self.output_path))

if __name__ == '__main__':
    unittest.main()
