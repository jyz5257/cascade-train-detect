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
For negative dataset, we need to provide negative txt file. The code "negwrite.py" can write all the neagtive files' diretory into a txt file. For positive dataset, we need to create a positive.vec file using opencv command: opencv_createsamples -info info/info.lst -vec positives.vec -num 400 -w 20 -h 20.
