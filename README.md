# AI Capstone - Sign Language Recognition
# work in progress
## Introduction
This project aims to use AI to recognize Sign Language gestures from the American Sign Language. We have trained 26 classes(alphabets), with each class containing 200 images.

# Getting Started
We first run the `collecting_data.py` to collect the data.
**Note:**
- `cv.VideoCapture(0)` is set to `0`
- In `DATA_DIR` object, the path is set to `./data`
- The number of classes is set to 26 to accomadate the English Alpahbet
- The object `dataset_size` is set to `100` (100 pictures are taken for each class)
- Press `Q` to start collecting data for a class
