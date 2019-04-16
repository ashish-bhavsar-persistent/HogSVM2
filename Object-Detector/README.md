#Object-Detector
This project is created to support the blog [post](http://hackevolve.com/create-your-own-object-detector/). It uses HOG+SVM framework for performing Object Detection.


--detector clock_detector.svm --image clock_test/1.jpg --annotate gun
  



/Users/shree/Ashu/Python/Gun_Detection/venv/bin/python /Users/shree/Ashu/Python/Gun_Detection/Object-Detector/annotations.py  --dataset cropped/ --annotations annot.npy --images images.npy

/Users/shree/Ashu/Python/Gun_Detection/venv/bin/python /Users/shree/Ashu/Python/Gun_Detection/Object-Detector/train.py  --annotations annot.npy --images images.npy --detector clock_detector.svm  



/Users/shree/Ashu/Python/Gun_Detection/venv/bin/python /Users/shree/Ashu/Python/Gun_Detection/Object-Detector/cropImage.py
###Usage:

####Gather annotations from images...
![](https://i0.wp.com/hackevolve.com/wp-content/uploads/2017/02/Screenshot-from-2017-02-05-22-08-08.png)

####Train Object Detector
![](https://i0.wp.com/hackevolve.com/wp-content/uploads/2017/02/Screenshot-from-2017-02-05-22-00-48.png?resize=768%2C432)

####Performing Object Detection
![](https://i2.wp.com/hackevolve.com/wp-content/uploads/2017/02/Screenshot-from-2017-02-05-22-02-53.png?resize=768%2C432)