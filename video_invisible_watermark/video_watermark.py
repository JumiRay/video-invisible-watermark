import cv2
import numpy as np
from stegano import lsb
from PIL import Image

def video_to_frames(video_path):
    """ Convert video to frames """
    vidcap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        success, image = vidcap.read()
        if not success:
            break
        frames.append(image)
    vidcap.release()
    return frames

def frames_to_video(frames, output_path, fps, size):
    """ Combine frames into video """
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for frame in frames:
        out.write(frame)
    out.release()

def embed_message_to_frame(frame, message):
    """ Embed message into the center 100x100 region of the frame """
    h, w, _ = frame.shape
    y, x = h // 2 - 50, w // 2 - 50
    center_frame = frame[y:y+100, x:x+100]
    pil_image = Image.fromarray(center_frame)
    encoded_image = lsb.hide(pil_image, message)
    frame[y:y+100, x:x+100] = np.array(encoded_image)
    return frame

def extract_message_from_frame(frame):
    """ Extract message from the center 100x100 region of the frame """
    h, w, _ = frame.shape
    y, x = h // 2 - 50, w // 2 - 50
    center_frame = frame[y:y+100, x:x+100]
    pil_image = Image.fromarray(center_frame)
    message = lsb.reveal(pil_image)
    return message

def embed_message_to_frames(frames, message, interval=30):
    """ Embed message into the center 100x100 region of every interval frame """
    for i in range(0, len(frames), interval):
        frames[i] = embed_message_to_frame(frames[i], message)
    return frames

def extract_message_from_frames(frames, interval=30):
    """ Extract message from the center 100x100 region of every interval frame """
    messages = []
    for i in range(0, len(frames), interval):
        message = extract_message_from_frame(frames[i])
        messages.append(message)
    return messages
