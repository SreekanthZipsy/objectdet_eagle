

### Summary of the Object Detection Model

* Model name: YoloV4 - Darknet framework. 
* You can find Dataset here: https://drive.google.com/file/d/1sVPCa38Xg7bgaG7KU62gjHXcAwJFrFTw/view?usp=sharing, Framework: https://github.com/AlexeyAB/darknet. 
* Yolo is one stage detector, YOLOV4 Model is updated version of V3 with some new training techniques like **Cross-iteration Batch Normalisation etc.. & new Activation Mish**. 
* This architecture also uses new Data Augmentation techniques like **Mosaic & Self Adversarial Training**. All these tricks made V4 **fast & more accurate** compared to other architectures.
* **Primary Analysis:** After making the data ready for Yolov4 training along with annotations, i have took 10% of data separately and kept it for validation while training. 
* **Assumptions:** Data we have is properly annotated with ground truths & have enough samples per class for training & testing.
* Initially went with default anchors provided by YoloV4, later to **improve MAP calculated the anchors based on my dataset** & retrained and had a significant improvement in mAP. 
* **Metrics:** mAP (mean Average Precision) improved a lot after using custom Anchors. 
* **Inference:** While checking on images, noticed a lot of falses of people because in an image we can only see half of there body, legs or upper body. We don't have Ground truth for that, but model learned to detect to those also. 
* I tested the model on the test set which i kept out. False positives & misses are mainly in crowded places. Ground truths on the test images has people annotated in the background with little to no clarity of that people.
* **Conclusion:** With more data according to our needs, like ignoring people in the background with no clear visibility & removing people or cars barely visible can improve the model. This can make the model focus on complete object, instead of parts of it. 
* **Recommendation:** After testing & have watched some testing images, i thought More data will definitely help and RetinaNet framework would have helped in detecting Densely covered objects like the cases with lot of people. 