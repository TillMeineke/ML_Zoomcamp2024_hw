

## Absolute local path
/Users/tillmeineke/ML/ML_Zoomcamp2024_hw/helloListenDog/data/helloListenDog_v1_dog_detection.v1i.coco/images/

## start label studio
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true; export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/Users/tillmeineke/ML/ML_Zoomcamp2024_hw/helloListenDog/data; label-studio start helloDogBreed

## convert coco(json from roboflow) to label studio
label-studio-converter import coco -i data/helloListenDog_v1_dog_detection.v1i.coco/images/test/_annotations.coco.json -o data/helloListenDog_v1_dog_detection.v1i.coco/images/test/label-studio_annotations.json --image-root-url "/data/local-files/?d=helloListenDog_v1_dog_detection.v1i.coco/images/test"
