import os

from PIL import Image

from model import Model


def test_images():

    # Get repo root
    root = __file__
    for _ in range(2):
        root = os.path.dirname(root)
    root = os.path.abspath(root)

    # Get image paths
    image_paths = []
    images_directory = f'{root}/resources/images'
    for file in os.listdir(images_directory):
        path = f'{images_directory}/{file}'
        image_paths.append(path)
    
    # Load images into an array
    images = []
    for path in image_paths:
        image = Image.open(path)
        images.append(image)

    # Forward pass each image through the model
    model = Model()
    for image in images:
        model(image)