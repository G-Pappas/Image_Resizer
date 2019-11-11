"""
Python Image Resizer.
Images must be .jpg files and located at the same folder with the script.
"""

import cv2
import glob

images = glob.glob("*.jpg") #create a list with the paths of all the images in folder

def resize_image():
    img=cv2.imread(image,1)#load picture to python
    resized_image=cv2.resize(img,(500,500))#select resized image size
    cv2.imshow("New Image", resized_image)#show the new picture in a window
    cv2.waitKey(500)#wait half sec
    cv2.destroyAllWindows()#close window
    cv2.imwrite("resized_"+image, resized_image)#Save the new image


for image in images:
    resize_image()
