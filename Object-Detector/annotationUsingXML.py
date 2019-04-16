import numpy as np
import cv2
from PIL import Image
import argparse
from imutils.paths import list_images
import xml.etree.ElementTree as ET

#parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,help="path to images dataset...")
ap.add_argument("-a","--annotations",required=True,help="path to save annotations...")
ap.add_argument("-i","--images",required=True,help="path to save images")
args = vars(ap.parse_args())

#annotations and image paths
annotations = []
imPaths = []

#loop through each image and collect annotations
for imagePath in list_images(args["dataset"]):
    if "jpg" in imagePath:
        img = Image.open(imagePath)
        xml_file = imagePath.replace("jpg", "xml").replace("FrameFromVideo","Lables")
        tree = ET.parse(xml_file)  # Converts .xml file into tree structure
        root = tree.getroot()

        for member in root.findall('object'):  # iterates through all '<object>' tags
            x = member[4][0].text
            y = member[4][1].text
            xb = member[4][2].text
            yb = member[4][3].text
        annotations.append([int(x),int(y),int(xb),int(yb)])

        imPaths.append(imagePath)
    # print(imagePath)
#save annotations and image paths to disk
annotations = np.array(annotations)
imPaths = np.array(imPaths,dtype="unicode")
np.save(args["annotations"],annotations)
np.save(args["images"],imPaths)
