import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from PIL import Image
from torchvision.transforms.functional import resize, to_tensor
import cv2
import numpy as np

import torchvision.transforms as T

# Load a pre-trained Faster R-CNN model
model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Define the transform
def transform(image):
    # Get the dimensions of the image
    width, height = image.size

    # Determine the new dimensions
    if width < height:
        new_width = 800
        new_height = int(height * new_width / width)
    else:
        new_height = 800
        new_width = int(width * new_height / height)

    # Resize the image and convert it to a tensor
    image = resize(image, (new_height, new_width))
    return to_tensor(image).unsqueeze(0), (new_width, new_height)

# Load an image
image = Image.open("screenshot.png")
image_tensor, (new_width, new_height) = transform(image)

# Perform object detection
with torch.no_grad():
    prediction = model(image_tensor)

# Get the bounding boxes and labels
boxes = prediction[0]['boxes']
labels = prediction[0]['labels']

# Define the label mapping
COCO_LABELS = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

# Convert the image to an OpenCV image
image = cv2.cvtColor(np.array(image.resize((new_width, new_height))), cv2.COLOR_RGB2BGR)

# Draw the bounding boxes and labels on the image
for i in range(boxes.shape[0]):
    box = boxes[i].numpy().astype('int')
    label = labels[i].item()
    # Check if the label is in the mapping
    if label < len(COCO_LABELS):
        label_name = COCO_LABELS[label]
    else:
        label_name = 'Unknown'
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
    cv2.putText(image, label_name, (box[0], box[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
