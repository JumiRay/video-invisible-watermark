from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='video_invisible_watermark',
    version='0.1.1',
    description='A Python library to embed invisible watermarks into video frames',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='MingLei Zhou',
    author_email='jumiray620@gmail.com',
    url='https://github.com/JumiRay/video-invisible-watermark',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'stegano',
        'Pillow'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
