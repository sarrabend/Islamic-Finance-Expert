import os 
from ..config import PROJECT_PATH


def write_into_file(content, output_file):

    """
    Writes the content into a file.
    """

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)


def read_from_file(md_file_path):
    """
    Reads the content of a markdown file.
    """
    with open(md_file_path, 'r', encoding='utf-8') as file:
        document_content = file.read()
    return document_content





def save_images(images, output_folder):
    """
    Save a list of images to a specified folder.

    Args:
        images (list): List of images.
        output_folder (str): Path to the output folder.
    """
    for file, image in images.items():
        image_path = os.path.join(output_folder, file)  # Preserve original filename
        image.save(image_path)  # Save the image to the output folder