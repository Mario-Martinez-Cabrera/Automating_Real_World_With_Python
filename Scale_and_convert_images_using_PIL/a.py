#!/usr/bin/env python3

#scale and convert images using PIL

from PIL import Image
import os
directory = "images/"
output_directory = "/opt/icons"

#Loop for correcting images
for filename in os.listdir(directory):
    if filename != ".DS_Store":
        im = Image.open(os.path.join(directory, filename))
        im = im.rotate(-90)
        im = im.resize(128,128)
        im = im.convert("RGB")
        im.save(os.path.join(output_directory, filename+".jpeg"))