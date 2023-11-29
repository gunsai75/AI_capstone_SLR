# Documentation
**Welcome to the documentation of the ASL - Sign Language recognition project**

## Setting up the code
### Acquiring the code
- Clone the repository
```bash
git clone https://github.com/gunsai75/AI_capstone_SLR.git
```
- Installing the required modules
> Note: This will install the above mentioned modules in the [Prerequsites] section in `README.md`; Considering that you have installed [Python3](https://www.python.org/downloads/) already.
```bash
pip install -r requirements.txt
```
### Collecting the Data
- Running the script to collect data from the webcam.

> Note: In the file `collecting_data.py`, the `cv.VideoCapture()` function's parameter is set to `0`. It is the index of the camera device that you want to capture video from. In this case, we're capturing from the first camera device (index 0).
```sh
py collecting_data.py
```
### Creating the Dataset
- Running the `creating_dataset.py` to create a dataset from the data present in the `/data` directory. Running this file also creates a binary file called `data.pickle` that stores the data points obtained from the images we collected in the previous step.

```sh
py creating_datatset.py
```

### Training the Model
- Running the `train_classifier_modfel.py` will use the data points stored in the `data.pickle` file to train the model.
- For this project, we are using a Random Forest Classifier algorithm to train our model.
- A new file, `model.p` is created that contains the parameters that can be then later used for testing the model.

```sh
py train_classifier_model.py
```

### Testing
- Running the `test_classifier.py` file will start testing the model.
- A window is displayed for the user to interact with the device camera. In this window, the predictions are shown.

```sh
py test_classifier.py
```