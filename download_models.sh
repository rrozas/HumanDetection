#!bin/bash
mkdir -p models
wget -P models/ "http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz"
wget -P models/ "http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2017_11_17.tar.gz"

cd models
tar -xzf faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
tar -xzf ssd_mobilenet_v1_coco_2017_11_17.tar.gz
