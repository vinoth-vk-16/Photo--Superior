# Image Colorization with Python and Gradio

This project implements a deep learning-based image colorization technique inspired by the model developed by Zhang et al. (2016). The model uses a Convolutional Neural Network (CNN) to predict the color components of grayscale images. It takes grayscale images as input and outputs fully colorized versions.

## Table of Contents

- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [Setup](#setup)
- [Usage](#usage)
- [Model Files](#model-files)
- [Acknowledgments](#acknowledgments)

## Introduction

Colorization involves converting grayscale images to RGB format by predicting the missing color information. This project utilizes a pre-trained model to achieve high-quality colorization results. Gradio is integrated for an intuitive web-based interface that allows users to upload black-and-white images and view the colorized outputs.

## How It Works

The process involves the following steps:

1. **RGB to LAB Conversion**: Convert the input image from RGB format to LAB format.
    - L: Lightness (intensity)
    - A: Green-Red color components
    - B: Blue-Yellow color components
2. **Input Preparation**: Use only the L channel (lightness) as input to the model.
3. **Model Prediction**: The model predicts the A and B channels.
4. **LAB to RGB Conversion**: Append the predicted A and B channels to the original L channel and convert the LAB image back to RGB format.

### Summary of Steps

1. **RGB to LAB**
2. **Extract L Channel**
3. **Predict A and B Channels**
4. **Combine L, A, B Channels**
5. **LAB to RGB**
![image](https://github.com/user-attachments/assets/d068cf68-1cea-4fab-9cdb-967fd527005a)

## Setup

### Prerequisites

- Python 3.8 or later
- Required Python libraries:
  - `opencv-python`
  - `numpy`
  - `gradio`

Install the required libraries using:

```bash
pip install opencv-python numpy gradio
```

### Model Files

Download the following model files and place them in the `model` directory:

- `colorization_deploy_v2.prototxt`
- `colorization_release_v2.caffemodel`
- `pts_in_hull.npy`

**Note**: 

[Download Model Files](#)
[https://drive.google.com/drive/folders/1hpOC_1mPtVoLZdIP54GR3ZyBYu4cvjqM?usp=sharing]

Ensure the directory structure looks like this:

```
project-directory/
    colorizer.py
    app.py
    model/
        colorization_deploy_v2.prototxt
        colorization_release_v2.caffemodel
        pts_in_hull.npy
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/vinoth-vk-16/Photo--Superior.git
```

2. Run the script:

```bash
python app.py
```

3. Open the Gradio interface in your browser. Upload a black-and-white image and get the colorized output instantly.


![image](https://github.com/user-attachments/assets/aa83ce07-a93f-443b-89c7-1b5fa379e043)

## Example

Input:
- A grayscale image (e.g., black-and-white photo)

Output:
- A colorized version of the image

## Acknowledgments

- The model is based on the work by Zhang et al., 2016.
  - Paper: [Colorful Image Colorization](https://arxiv.org/abs/1603.08511)

Special thanks to the authors for making their work and models publicly available.

---

Feel free to contribute by opening issues or submitting pull requests!

