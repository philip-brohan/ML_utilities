#!/usr/bin/env python

# Make a digital image with the DALL-E api

import openai
import requests
import os
from PIL import Image

from openai_tools.config.access import get_key

openai.api_key = get_key()

prompt = (
    "Amidst the winter backdrop, the sailor emanated an aura of mystique. "
    + "His tunic, a rich hue of midnight blue, "
    + "draped effortlessly over a well-built frame. His bare arms"
    + "displayed interwoven maritime and oriental tattoos. From his intricately stitched belt "
    + "hung a scimitar. Its curved blade shimmered, ornate patterns etched onto its surface, "
    + "its hilt was encrusted with turquoise and carnelian."
)

# call the OpenAI API
generation_response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024",
    response_format="url",
)

generated_image_name = "generated_image.png"  # any name you like; the filetype should be .png
generated_image_filepath = os.path.join('.', generated_image_name)
generated_image_url = generation_response["data"][0]["url"]  # extract image URL from response
generated_image = requests.get(generated_image_url).content  # download the image

with open(generated_image_filepath, "wb") as image_file:
    image_file.write(generated_image)  # write the image to the file

