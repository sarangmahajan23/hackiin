import glob
import os
import cv2

path = r'/Faces'

Images = glob.glob('*.jpg')

folder = 'resized'
if not os.path.exists(folder):
    os.makedirs(folder)

for image in images:
    img = cv2.imread(image,-1)
    re = cv2.re