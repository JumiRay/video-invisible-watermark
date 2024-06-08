from setuptools import setup, find_packages

setup(
    name='video_invisible_watermark',
    version='0.1.0',
    description='A Python library to embed invisible watermarks into video frames',
    author='MingLei Zhou',
    author_email='jumiray620@gmail.com',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'stegano',
        'Pillow'
    ],
)
