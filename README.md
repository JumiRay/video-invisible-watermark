### README

# Video Watermarking with DCT

This project provides a simple way to embed and extract watermarks from video frames using the Discrete Cosine Transform (DCT). The watermark image is embedded in the luminance component (Y) of the YUV color space of each video frame.

## Requirements

To install the required packages, use the following command:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```plaintext
opencv-python
Pillow
scipy
```

## Usage

### Embedding a Watermark in a Video

To embed a watermark in a video, use the `embed_watermark_to_video` function. This function takes the input video path, output video path, watermark image path, duration in seconds, and frames per second (fps) as arguments.

Example:

```python
embed_watermark_to_video('input_video.mp4', 'output_video_with_watermark.mp4', 'watermark.png', duration=10, fps=30)
```

### Extracting a Watermark from a Video

To extract a watermark from a video, use the `extract_watermark_from_video` function. This function takes the output video path, the prefix for the directory where extracted images will be saved, and the duration in seconds as arguments.

Example:

```python
extract_watermark_from_video('output_video_with_watermark.mp4', prefix='result/post_compression', duration=10)
```

## Functions

### load_image(image_path, size=(100, 100))

Loads an image and resizes it to the specified size.

### embed_watermark_to_frame(frame, img)

Embeds a watermark image into a video frame using DCT.

### extract_watermark_from_frame(frame, img_size=(100, 100))

Extracts the embedded watermark image from a video frame using DCT.

### video_to_frames(video_path, duration=10, fps=30)

Splits a video into frames for the specified duration and frames per second (fps).

### frames_to_video(frames, output_path, fps, size)

Combines frames into a video with the specified frames per second (fps) and output size.

### save_images(images, prefix='result/pre_compression')

Saves images to the specified directory with a given prefix.

### embed_watermark_to_video(input_video_path, output_video_path, watermark_path, duration=10, fps=30)

Embeds a watermark into a video for the specified duration and frames per second (fps).

### extract_watermark_from_video(output_video_path, prefix='compression', duration=10)

Extracts the watermark from a video for the specified duration and saves the extracted images to the specified directory.

## Example Workflow

1. **Embed a watermark into a video**:

    ```python
    embed_watermark_to_video('input_video.mp4', 'output_video_with_watermark.mp4', 'watermark.png', duration=10, fps=30)
    ```

2. **Extract the watermark from the video**:

    ```python
    extract_watermark_from_video('output_video_with_watermark.mp4', prefix='result/post_compression', duration=10)
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [OpenCV](https://opencv.org/)
- [Pillow](https://python-pillow.org/)
- [SciPy](https://www.scipy.org/)

Feel free to customize this README further based on your specific needs and usage of the project.