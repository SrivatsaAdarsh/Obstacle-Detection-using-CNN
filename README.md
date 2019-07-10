# Obstacle-Detection-using-CNN

Object detection and identification is a fundamental workflow in Computer vision. 
Proposed system specifies the methods that have been used to overcome the disadvantages that were present in the old methodologies like:
e.g R-CNN, KNN etc.

Training is done via convolutional neural network with inception-v3 model with the labels of their respective object.
Segmentation is applied as a pre-processing stepwhere the image is divided into equal patches.
A rectangle is drawn on the image showing the patches of image data.
Image is cropped using the co-ordinates of the rectangle.
This method increases accuracy because only the part of an image is used for CNN.
