This task is all about counting the number of persons who are wearing mask properly, improperly and without wearing mask. 
So there are three classes in this kodel.

I have done this task by using YOLOV3 model.

TRAINING THE MODEL:

STEP-1:
  Firstly I collected images of wearing mask properly, improperly and without mask and Create lables for the images. 
  created a dataset using all of the images and lables.
  
STEP-2:
   ZIp that file and store that in your drive. After that while training the model you have to unzip that folder.

STEP-3:
  Now the trained model which I used but in that you have to change some content in MAkefile that is change the values of GPU and OPENCV to 1 and in 
  addition to that you have to change the content in two files those files are ==> creating-files-data-and-name.py and creating-train-and-test-txt-files.py. 
  You have to replace class names with your class names which you have given for the labels. 
  
STEP-4: 
  After completing the whole training process you will get weights and config files. Download that files into your drive with that files only you 
  will be able to count your classes in the given image.
  
  
COUNTING THE NUMBER OF CLASSES:

Libraries used:  cv2, numpy, matplotlib

For counting we use weight files and config files which you have downloaded after completion training the model. By using those files we will count our 
number of classes. I have added code for counting also.

It will gives us the output like this

![persons_count](https://user-images.githubusercontent.com/99468260/170002311-6f38d902-299f-4b9c-be38-c3f0ff5d3f62.png)

It will count the number of classes and gives us the output.


