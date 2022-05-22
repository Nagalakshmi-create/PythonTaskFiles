import cv2
import numpy as np
import matplotlib.pyplot as plt

net = cv2.dnn.readNetFromDarknet("/home/neosoft/Downloads/yolov3/yolov3_custom.cfg",r"/home/neosoft/Downloads/yolov3/yolov3_custom_5000.weights")

class_names = ['mask','no_mask','improper_mask']

# Load names of classes and get random colors
classes = []
with open('/home/neosoft/Downloads/yolov3/custom_data/classes.names','r') as f:
    classes = [line.strip() for line in f.readlines()]
    
image = cv2.imread('/home/neosoft/Downloads/yolo_mask_dataset/face_data/test/crowd_mask65.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)

image = cv2.imread('/home/neosoft/Downloads/yolo_mask_dataset/face_data/test/crowd_mask65.jpg')
image = cv2.resize(image,(1280,720))

height, width, _ = image.shape

#it returns an 4d array/blob for input img, (img,scalefactor(1/n),size,mean subtraciton,swapRB)
# convert the images list into an OpenCV-compatible blob
blob = cv2.dnn.blobFromImage(image, 1/255, (416,416),(0,0,0),swapRB = True, crop = False) 

print(blob.shape)

#blob object is given as input to the network
net.setInput(blob)

#yOLOv3 has 3 output layers (82, 94 and 106) as the figure shows.

#getLayerNames(): Get the name of all layers of the network.

#getUnconnectedOutLayers(): Get the index of the output layers.
    
last_layer = net.getUnconnectedOutLayersNames()

layer_out = net.forward(last_layer)
print(layer_out)

print(layer_out[0].shape)

print(layer_out[0][0])

boxes =[]
confidences = []
class_ids = []

for output in layer_out:
    
    for detection in output:
        
        score = detection[5:]
        class_id = np.argmax(score)
        confidence = score[class_id]
        
        if confidence > 0.6:
            
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3]* height)
            x = int(center_x - w/2)
            y = int(center_y - h/2)
            boxes.append([x,y,w,h])
            confidences.append((float(confidence)))
            class_ids.append(class_id)
            
indexes = cv2.dnn.NMSBoxes(boxes, confidences,.5,.4)
print(indexes)

font = cv2.FONT_HERSHEY_PLAIN 
colors = np.random.uniform(0,255,size = (len(boxes),3))

l=0
m=0
n=0
if len(indexes) > 0:
    for i in indexes.flatten():
        x,y,w,h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str((int(confidences[i] *100)))
        
        if label == "mask":
            cv2.rectangle(image,(x,y),(x+w, y+h), (0,255,0),2)
            cv2.putText(image,label + " "+ confidence +'%', (x,y-8), font, 2, (0,255,0),2)
            l=l+1
            
        if label == "no_mask":
            cv2.rectangle(image,(x,y),(x+w, y+h), (0,0,255),2)
            cv2.putText(image,label + " "+ confidence +'%', (x,y-18), font, 2, (0,0,255),2)
            m=m+1
            
        if label == "improper_mask":
            cv2.rectangle(image,(x,y),(x+w, y+h), (0,0,255),2)
            cv2.putText(image,label + " "+ confidence +'%', (x,y-18), font, 2, (0,0,255),2)
            n=n+1
    
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)

            
print("With mask: " + str(l))
print("without mask: "+str(m))
print("Improper mask: " + str(n))
