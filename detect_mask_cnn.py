# Importing the libraries
!pip install tensorflow  

import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras import layers

tf.__version__

'''Image Augmentation
Image augmentation is done for increasing the dataset. If you want the dataset change the below cell from markdown to code and upload the path of your image in load_img.

datagen = ImageDataGenerator( rotation_range=40, width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest')

img = load_img('/home/neosoft/Downloads/mask_dataset/train/properly_worn_mask/HTB1jE7ILFXXXXaEXpXXq6xXFXXXd.jpg') 
x = img_to_array(img) 
x=x.reshape((1,) + x.shape)

i=0 
for batch in datagen.flow(x, batch_size=1, save_to_dir='/home/neosoft/Downloads/mask_dataset/train/properly_worn_mask', save_prefix='Augmented_image', save_format='jpg'): 
  i += 1 
  if i>4: 
    break'''


'''Part 1 - Data Preprocessing
Preprocessing the Training set'''

# we use rescale for normalisation. We are diving each value with 255 to get all the between 
# 0 and 1. In normal dataset we can call it like feature scaling.

# shear_range, zoom_range, horizontal_flip these all are for transformations that will perform
# image augmentation on the images of the training set. We can also run this without using these
# transformation but it will raise to overfitting. So we are these transformations.

train_datagen = ImageDataGenerator(rescale = 1./255,  
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

# flow_from_directory --> to connect this image augmentation tool to the images of your training set.
# target_size --> our input image size
# batch_size --> size of the batches means how many images we want to have in each batch.
# class_mode --> binary for either 0 or 1, categorical for more than 2 outputs.

training_set = train_datagen.flow_from_directory('/home/neosoft/Downloads/mask_dataset/train',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

#Preprocessing the Test set
test_datagen = ImageDataGenerator(rescale = 1./255)
test_set = test_datagen.flow_from_directory('/home/neosoft/Downloads/mask_dataset/test',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

'''Part 2 - Building the CNN
Initialising the CNN'''
cnn = tf.keras.models.Sequential()

#Step 1 - Convolution
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))

#Step 2 - Pooling
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

#Adding a second convolutional layer
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

#Step 3 - Flattening
cnn.add(tf.keras.layers.Flatten())

#Step 4 - Full Connection
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

#Step 5 - Output Layer
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

'''Part 3 - Training the CNN
Compiling the CNN'''
cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Training the CNN on the Training set and evaluating it on the Test set
# epochs --> how many times to read the dataset

cnn.fit(x = training_set, validation_data = test_set, epochs = 25)

#Part 4 - Making a single prediction
import cv2
from matplotlib import pyplot as plt

predict_img = cv2.imread("/home/neosoft/Downloads/mask_dataset/image_2022_04_22T14_11_29_438Z.png")
predict_img = cv2.cvtColor(predict_img, cv2.COLOR_BGR2RGB)
plt.imshow(predict_img)

import numpy as np
from keras.preprocessing import image

test_image = image.load_img('/home/neosoft/Downloads/mask_dataset/image_2022_04_22T14_11_29_438Z.png', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = cnn.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
  prediction = 'Properly worn mask'
else:
  prediction = 'Improperly worn mask'
print(prediction)
