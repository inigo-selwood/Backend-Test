from model import Model
from PIL import Image

model = Model()

# Get some test images
image = Image.open("./images/pixie.jpg")

model(image)