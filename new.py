# IMPORTS
import ollama
import cv2
import os
import json
import requests
from bs4 import BeautifulSoup

# -------------------------------------------
# Object Identification Agent
# -------------------------------------------
def identify_objects():
    """
    Identifies objects in an image using the LLaVA model.
    Saves the output to a text file.
    """
    # MODEL INIT
    ollama.pull('llava')

    # INPUT
    image_path = '/inputs/random_image.jpg'
    
    if not os.path.exists(image_path):
        return "Input image missing"

    img = cv2.imread(image_path)
    
    if img is None:
        return "Failed to load image"

    # PROCESSING
    response = ollama.generate(
        model='llava',
        prompt='Identify objects in this image.',
        images=[img]
    )

    # OUTPUT
    try:
        with open('/outputs/object_identification.txt', 'w') as f:
            f.write(response['response'])
        return "Object identification complete and saved."
    except Exception as e:
        return f"Error writing to file: {e}"


# -------------------------------------------
# Object Classification Agent
# -------------------------------------------
def classify_object():
    """
    Classifies an object description using the BERT model.
    Saves the classification result to a JSON file.
    """
    # MODEL INIT
    ollama.pull('bert-base-uncased')

    # INPUT
    description = "A small, red sports car with a spoiler."
    query = f"Classify the object described: {description}"

    # PROCESSING
    response = ollama.generate(model='bert-base-uncased', prompt=query)
    classification_result = response['response'].strip()

    # OUTPUT
    try:
        with open('/outputs/object_classification.json', 'w') as f:
            json.dump({"description": description, "classification": classification_result}, f)
        return "Object classified and saved to JSON."
    except Exception as e:
        return f"Error writing to file: {e}"


# -------------------------------------------
# Object Finder Agent
# -------------------------------------------
def find_object_on_webpage():
    """
    Finds objects on a webpage based on a given description.
    Extracts relevant HTML elements and text, then saves the output.
    """
    # MODEL INIT
    ollama.pull('llama2')

    # INPUT
    url = "https://www.example.com"
    description = "Blue widgets"

    # PROCESSING
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        prompt = f"Find HTML elements related to: {description}. Return just the element tags and text."

        ollama_response = ollama.generate(model='llama2', prompt=prompt)

        # OUTPUT
        with open('/outputs/webpage_object_search.txt', 'w') as f:
            f.write(ollama_response['response'])

        return "Webpage search completed; results saved."

    except requests.RequestException as e:
        return f"Error fetching webpage: {e}"
    except Exception as e:
        return f"Error during webpage processing: {e}"

