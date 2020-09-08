# Importing libraries
from fastai.vision import *
from fastai.callbacks.hooks import *
from fastai.utils.mem import *
import os
import cv2

# Define a custom metric that was used in trianing the model
# Don't believe this is used when making predictions but the model won't load if this isn't here
def acc_camvid(input, target):
    target = target.squeeze(1)
    print(target)
    print(void_code)
    mask = target != void_code
    return (input.argmax(dim=1)[mask]==target[mask]).float().mean()

# Load the model assuming you've put this program in the same place
print("Loading model...")
learn = load_learner(os.getcwd())
print("Model loaded!")

# Opening the image to be run through the neural network
cwd = os.getcwd()
imgPath = cwd + "/" + input("Enter the name of your image: ")
img = open_image(imgPath)

# Predict the position of the saplings and save it as an image
prediction = learn.predict(img)
output = prediction[0]
output.show(figsize=(5,5), alpha=0.9)
output.save("predict.png")

# Image was saved as two shades of black so change that to yellow so it's easier to see
mask = cv2.imread("predict.png")
height, width, channels = mask.shape

light = [66,203,245]
dark = [51,143,171]

for x in range(0, width):
    for y in range(0, height):
        channels_xy = mask[y,x]
        if all(channels_xy == [0,0,0]):
            mask[y,x] = light
        else:
            mask[y,x] = dark
            
cv2.imwrite("predict.png", mask)

# Put the sapling prediction over the original image and save that
background = cv2.imread(imgPath)
overlay = cv2.imread("predict.png")
added_image = cv2.addWeighted(background,1,overlay,0.5,0)
cv2.imwrite('combined.png', added_image)