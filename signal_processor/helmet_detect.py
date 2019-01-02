from signal_processor import yolo_helmet_detector, yolo_figure_detector
from PIL import Image
import cv2
from datetime import datetime
import os
from app.db_io import addLog

class HelmetCapturer(object):
    _signal = None
    _isActive = False

    def __init__(self, cam):
        self._signal = cam

    def switch_signal(self, cam):
        self.deactive()
        self._signal = cam

    def active(self):
        if self._isActive or self._signal is None:
            return
        self._isActive = True
        frame = self._signal.get_frame()
        timer = 0

        while frame is not None and self._isActive:
            if timer % 24 == 0:
                f_image, f_out_boxes, _, classes_name = yolo_figure_detector.detect_image(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                person_count = 0
                if 'person' in classes_name:
                    for name in classes_name:
                        if name == 'person':
                            person_count += 1

                    r_image, out_boxes, _, classes_name = yolo_helmet_detector.detect_helmet(frame)
                    # print(f_out_boxes, out_boxes)
                    # this class returns image as numpy array
                    if len(classes_name) < person_count:
                        r_image = Image.fromarray(cv2.cvtColor(r_image, cv2.COLOR_BGR2RGB))
                        # r_image.show()
                        # f_image.show()
                        savePath = 'G:\TermAssignment\Pic\\' + str(datetime.today().year) + '\\' + str(datetime.today().month) + '\\' + str(datetime.today().day)
                        if not os.path.exists(savePath):
                            os.makedirs(savePath)
                        if not os.path.isfile(savePath + '\pic' + str(timer) + '.jpg'):
                            r_image.save(savePath + '\pic' + str(timer) + '.jpg')
                            pic_path = 'http://localhost:83/' + str(datetime.today().year) + '/' + str(datetime.today().month) + '/' + str(datetime.today().day) + '/pic' + str(timer) + '.jpg'
                            addLog(pic_path, self._signal._camid, '安全帽', datetime.today())
            else:
                print('skip this frame')
            frame = self._signal.get_frame()
            timer += 1
        print('no signal or deactivated by other caller')
        self.deactive()

    def deactive(self):
        self._isActive = False



