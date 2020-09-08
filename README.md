# Regeneration-AI
A model trained to detect saplings

## Work In Progress  
There is currently a program that uses a pretrained model and shows you its prediction for where saplings are (saplingModel.py) but I'm currently looking at solutions for uploading the trained model as it's too big for github. More detailed isntructions are to come regarding how to train your own model and troubleshoot it.

## Train your own model
I have included all the necessary images and files to train your own model. Open notebook.ipynb with anaconda navigator and change the directories to match your own.

### Troubleshooting
If you are having problems getting this set up, then check out fastai and follow their installation guide. 

## Using a pretrained model
- Download saplingModel.py and the pretrained model (currently not available for this dataset).  
- Make sure the pretrained model is named export.pkl.  
- Create a folder and put saplingModel.py, export.pkl, and the image to be processed, inside of it.  
- Run saplingModel.py. This can be using the command line or simply double clicking on it if you have python installed.  
- Follow the on screen instructions.  
- Two new images will be created in that folder. One will be called predict.png and it's only the prediction mask. The other is called combined.png and that combines the prediction mask with the original image.  

Note: Any images in that file named predict.png or combined.png will be overwritten. I hope to have this fixed here soon but for now make sure if you run the program once then either rename the images it creates or move them somewhere else.

## Files
### images
Holds the images that the model was trained on and that you can use to test the model

### labels
Masks of images in the ./images files so that the model knows where the saplings are

### codes.txt
Each line corresponds to a RGB value (line one = [0,0,0], line two = [1,1,1]) and this is used so that the neural net knows what object correlates to each pixel of each image in ./labels

### notebook.ipynb
Jupyter notebook used to train the model

### saplingModel.py
Short python script that will take an image an run it through the neural net and spit out its results

### valid.txt
Image names that the neural net will use to validate itself

