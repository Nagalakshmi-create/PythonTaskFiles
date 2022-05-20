from google.colab import drive
drive.mount('/content/drive')

!ls '/content/drive/MyDrive/yolov3_mask_dataset'

!unzip '/content/drive/MyDrive/yolov3_mask_dataset/mask_data_yolov3.zip' -d '/content/drive/MyDrive/yolov3_mask_dataset/'

!git clone 'https://github.com/AlexeyAB/darknet.git' '/content/drive/MyDrive/yolov3_mask_dataset/darknet'

%cd /content/drive/MyDrive/yolov3_mask_dataset/darknet

!ls

%cd darknet
!sed -i 's/GPU=0/GPU=1/g' Makefile
!sed -i 's/OPENCV=0/OPENCV=1/g' Makefile
!make

%cd /content/drive/MyDrive/yolov3_mask_dataset

!python mask_data_yolov3/creating-files-data-and-name.py

!python mask_data_yolov3/creating-train-and-test-txt-files.py

!ls

%cd /content/drive/MyDrive/yolov3_mask_dataset/darknet

!ls

%cd /content/drive/MyDrive/yolov3_mask_dataset

!darknet/darknet detector train mask_data_yolov3/labelled_data.data darknet/cfg/yolov3_custom.cfg weights/darknet53.conv.74 -dont_show
