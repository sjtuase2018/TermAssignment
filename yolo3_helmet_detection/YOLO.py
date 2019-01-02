import cv2
import argparse
import sys
import numpy as np
import os.path
from glob import glob
from PIL import ImageFont, Image


basedir = os.path.abspath(os.path.dirname(__file__))


def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]


class YOLO(object):
    _default = {
        'confThreshold': 0.3,
        'nmsThreshold': 0.4,
        'inpWidth': 416,
        'inpHeight': 416,
        'classDir': basedir + '/obj.names',
        'modelConfigDir': basedir + '/yolov3-obj.cfg.txt',
        'modelWeights': basedir + '/yolov3-obj_2400.weights'
    }

    _classes = None
    _net = None

    def _get_class(self):
        with open(self._default['classDir'], 'rt') as f:
            self._classes = f.read().rstrip('\n').split('\n')

    def _model_init(self):
        self._net = cv2.dnn.readNetFromDarknet(self._default['modelConfigDir'], self._default['modelWeights'])
        self._net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self._net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    def __init__(self, configDir=None, weightsDir=None):
        self._get_class()
        self._model_init()

    def detect_helmet(self, frame_input):
        frame = frame_input.copy()
        h, w, c = frame.shape
        self._net.setInput(cv2.dnn.blobFromImage(frame, 1/255, (self._default['inpWidth'], self._default['inpHeight']), [0, 0, 0], 1, False))
        outs = self._net.forward(getOutputsNames(self._net))
        class_ids = []
        scores = []
        bboxes = []
        for out in outs:
            for detection in out:
                score = detection[5:]
                class_id = np.argmax(score)
                if score[class_id] > self._default['confThreshold']:
                    x = int(detection[0]*w)
                    y = int(detection[1]*h)
                    wid = int(detection[2]*w)
                    hei = int(detection[3]*h)
                    class_ids.append(class_id)
                    scores.append(float(score))
                    bboxes.append([int(x-wid/2), int(y-hei/2), wid, hei])

        indices = cv2.dnn.NMSBoxes(bboxes, scores, self._default['confThreshold'], self._default['nmsThreshold'])
        outboxes = []
        outscores = []
        outclasses = []
        for i in indices:
            box = bboxes[i[0]]
            l = box[0]
            t = box[1]
            w = box[2]
            h = box[3]
            outboxes.append([l, t, w, h])
            outscores.append(scores[i[0]])
            outclasses.append(self._classes[class_ids[i[0]]])
            cv2.rectangle(frame, (l, t), (l+w, t+h), (255, 178, 50), 3)
            # print(scores[i[0]], (l, t))
            conf = '%.2f' % scores[i[0]]
            cv2.putText(frame, conf, (l, t), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 0), 1)

        return frame, outboxes, outscores, outclasses



