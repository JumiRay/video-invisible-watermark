# Video Invisible Watermark

**Video Invisible Watermark** is a Python library for embedding invisible watermarks into video frames.
The library focuses on embedding messages into the center 100x100 pixel region of video frames, ensuring minimal impact on video quality while maintaining robustness.

## Features

- **Convert Video to Frames**: Extract frames from a video.
- **Combine Frames to Video**: Reassemble frames back into a video.
- **Embed Messages**: Embed hidden messages into the center 100x100 region of video frames.
- **Extract Messages**: Retrieve hidden messages from the center 100x100 region of video frames.
- **Robustness**: Ensures minimal impact on video quality while maintaining message integrity.

## Installation

Install the library using `pip`:

```bash
pip install video_invisible_watermark
```

## Usage

### Basic Usage

#### Convert Video to Frames

```python
from video_invisible_watermark import video_to_frames

video_path = 'input_video.mp4'
frames = video_to_frames(video_path)
```

#### Combine Frames to Video

```python
from video_invisible_watermark import frames_to_video

output_path = 'output_video.mp4'
fps = 30  # Frames per second
size = (frames[0].shape[1], frames[0].shape[0])  # Frame size

frames_to_video(frames, output_path, fps, size)
```

#### Embed Message into Frames

```python
from video_invisible_watermark import embed_message_to_frames

message = 'This is a hidden message'
frames_with_message = embed_message_to_frames(frames, message)
```

#### Extract Message from Frames

```python
from video_invisible_watermark import extract_message_from_frames

extracted_messages = extract_message_from_frames(frames_with_message)
print(extracted_messages)
```

### Complete Example

```python
from video_invisible_watermark import (
    video_to_frames,
    frames_to_video,
    embed_message_to_frames,
    extract_message_from_frames
)

# Convert video to frames
video_path = 'input_video.mp4'
frames = video_to_frames(video_path)

# Embed message into frames
message = 'This is a hidden message'
frames_with_message = embed_message_to_frames(frames, message)

# Combine frames to video
output_path = 'output_video.mp4'
fps = 30  # Frames per second
size = (frames[0].shape[1], frames[0].shape[0])  # Frame size
frames_to_video(frames_with_message, output_path, fps, size)

# Extract message from frames
extracted_messages = extract_message_from_frames(frames_with_message)
print(extracted_messages)
```

## Testing

Run tests to ensure everything is working correctly:

```bash
python -m unittest discover tests
```

## Project Structure

```
video-invisible-watermark/
│
├── video_invisible_watermark/
│   ├── __init__.py
│   ├── video_watermark.py
│
├── tests/
│   ├── __init__.py
│   ├── test_video_watermark.py
│
├── README.md
├── setup.py
├── requirements.txt
├── .gitignore
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---

This README provides an overview of the library, installation instructions, basic usage examples, and details about the project structure and testing. Feel free to customize it further based on your specific requirements and preferences.