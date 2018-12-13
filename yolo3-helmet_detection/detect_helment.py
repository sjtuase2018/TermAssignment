from time import sleep
import cv2 as cv
import argparse
import sys
import numpy as np
import os.path
from glob import glob

frame = cv.imread(fn)
frame_count =0

# Create a 4D blob from a frame.
blob = cv.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop=False)

# Sets the input to the network
net.setInput(blob)

# Runs the forward pass to get output of the output layers
outs = net.forward(getOutputsNames(net))

# Remove the bounding boxes with low confidence
postprocess(frame, outs)

# Put efficiency information. The function getPerfProfile returns the overall time for inference(t) and the timings for each of the layers(in layersTimes)
t, _ = net.getPerfProfile()
#print(t)
label = 'Inference time: %.2f ms' % (t * 1000.0 / cv.getTickFrequency())
#print(label)
cv.putText(frame, label, (0, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
#print(label)
