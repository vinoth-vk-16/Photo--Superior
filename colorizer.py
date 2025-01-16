# colorizer.py
import cv2
import numpy as np
import os

# Define global variables for the model paths
DIR = r"D:\Image_Colorization"
PROTOTXT = os.path.join(DIR, "model/colorization_deploy_v2.prototxt")
POINTS = os.path.join(DIR, "model/pts_in_hull.npy")
MODEL = os.path.join(DIR, "model/colorization_release_v2.caffemodel")

# Initialize global model variable
net = None

def load_model():
    """
    This function loads the model only once.
    """
    global net
    if net is None:
        print("Loading model...")
        net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
        pts = np.load(POINTS)
        class8 = net.getLayerId("class8_ab")
        conv8 = net.getLayerId("conv8_313_rh")
        pts = pts.transpose().reshape(2, 313, 1, 1)
        net.getLayer(class8).blobs = [pts.astype("float32")]
        net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
        print("Model loaded successfully.")

def colorize_image(input_image):
    """
    Colorize the given black and white image.
    """
    load_model()  # Ensure the model is loaded before running

    if isinstance(input_image, np.ndarray):  # Check if the input is an image array
        image = input_image
    else:
        raise ValueError("The input is not a valid numpy image array.")

    # Convert image to BGR for OpenCV compatibility
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Prepare image for colorization
    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50

    # Run the colorization
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))
    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)
    colorized = (255 * colorized).astype("uint8")
    colorized = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)

    return colorized

# Function to create the Image Colorizer page
def create_colorizer_page():
    import gradio as gr

    with gr.Row():
        with gr.Column():
            gr.Markdown("### Image Colorizer")
            gr.Markdown("Upload a black-and-white image, and this model will colorize it.")

            # Create the interface
            iface = gr.Interface(
                fn=colorize_image,
                inputs=gr.Image(type="numpy", label="Upload a black and white image"),
                outputs=gr.Image(type="numpy", label="Colorized Image"),
                live=True,
            )
            iface.launch(inline=True)
