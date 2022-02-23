import json
import os
import cv2

IMG_DIR = "eagle_images/test"
IMG_SAV = 'inference_new'

if not os.path.exists(IMG_SAV):
    os.mkdir(IMG_SAV)

file = 'result.json'
with open(file) as f:
    data = json.load(f)  # load JSON


for pic in data:
    file_dir = pic["filename"]
    image_name = file_dir.split(os.sep)[-1]
    img = cv2.imread(os.path.join(IMG_DIR, image_name))
    h, w, c = img.shape
    for obj in pic["objects"]:
        class_name = obj["name"]
        confidence = obj["confidence"]
        print(class_name, confidence)
        coords = obj["relative_coordinates"]
        c_x = coords["center_x"] * w
        c_y = coords["center_y"] * h
        width = coords["width"] * w
        height = coords["height"] * h

        x1, y1 = int(c_x - width/2), int(c_y - height/2)
        x2, y2 = int(c_x + width/2), int(c_y + height/2)

        if class_name == "car":
            cv2.rectangle(img, pt1=(x1,y1), pt2=(x2, y2), color=(255,0,0), thickness=2)
        else:
            cv2.rectangle(img, pt1=(x1,y1), pt2=(x2, y2), color=(0,0,255), thickness=2)
        cv2.imwrite(os.path.join(IMG_SAV, image_name), img)

