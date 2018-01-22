# Cascade-train-detect
## Project Description
The goal of this project is to train a cozmo robot (a small mobile ground robot) model with the cascade classifier. The cascade classifier is a training method developed by opencv. It is included in opencv package after version 2.0. The training feature is based on Haar feature, and opencv will be used as a classifier and also a detector. 
This repository provides the codes and explanations for training a desired model from scratch.
## Buiding Environment
* Linux 16.04
* Opencv version 2 or higher
* Python 2
## How to run
### Provide the dataset
To strat the training, we need to collect our training dataset. The dataset used in this project is provided here. "neg.zip" and "pos.zip" are negeative and positive dataset. In "map_data.zip", there are 350 sample images. You can also collect your own dataset.
### Crop the images
The training image size I'm using is 64 to 64. Therefore, I need to crop the background images and robot images all to the same size. For positve data, I used a "BBox-Label-Tool" to crop the robot images. You can find it in this link: https://github.com/puzzledqs/BBox-Label-Tool. For nagative data, I used the python code "cropbg.py" to crop the bg images every 16 pixels horizontally and every 18 pixels vertically.
### Prepare the description file
For negative dataset, we need to provide negative txt file. The code "negwrite.py" can write all the neagtive files' diretory into a txt file. For positive dataset, we need to create a positive.vec file using opencv command: opencv_createsamples. In the command line, you need to provide the data information. This is a sample command: opencv_createsamples -info info/info.lst -vec positives.vec -num 400 -w 20 -h 20. -info is to provide the info list directory, -vec is the output file name, -num is the total number of your positive data, -w and -h are the image size would be resived.
### Training with cascade
After we got all the data prepared, we can start to train using opencv command: opencv_traincascade, and provide the training info in the command line. This is a sample command I used to train my data: opencv_traincascade -data data -vec positives.vec -bg negative.txt -numPos 320 -numNeg 660 -numStages 10 -w 20 -h 20. -data is the output folder directory, -vec is the positive vec file you just generate, -bg is the negative data txt file, -numPos and -numNeg are the number of pos and neg data it will cosume while training, -numStages is the depth of the stages you want to train, -w and -h are the resized image size. The training might take more than one day if you have a very large dataset. It would generate a stage model after every stage training is finished. After all the stages finished, there would be a xml file inside the data folder, which is a final model.
### Test the model
Once you got your output model, you can start to test it on images or video. I provide here my codes for image and video testing on pyhton, which are called imageload.py and videostream.py. In the code, I use cv2.CascadeClassifier('cascade.xml') to load the model. You simply change the model name to yours when you test on your model.
