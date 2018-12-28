from keras_yolo3.yolo import YOLO as FIGURE_YOLO
from yolo3_helmet_detection.YOLO import YOLO as HELMET_YOLO


print('initing all model processors')
yolo_figure_detector = FIGURE_YOLO()
yolo_helmet_detector = HELMET_YOLO()

print('all processors ready')
