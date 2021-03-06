from signal_processor import yolo_figure_detector
from PIL import Image
from datetime import datetime
import os
from app.db_io import addLog


class FigureCapturer(object):
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
                r_image, out_boxes, _, classes_name = yolo_figure_detector.detect_image(Image.fromarray(frame))
                # print(classes_name)
                # out_boxes.shape = [num of boxes, 4]
                #两帧很接近
                if 'person' in classes_name:
                    pic_name = 'pic' + ('%02d%02d%02d' % (datetime.today().hour, datetime.today().minute, datetime.today().second)) + '.jpg'
                    savePath = 'G:\TermAssignment\Pic\\' + str(datetime.today().year) + '\\' + str(datetime.today().month) + '\\' + str(datetime.today().day)
                    if not os.path.exists(savePath):
                        os.makedirs(savePath)
                    if not os.path.isfile(savePath + '\\' + pic_name):
                        r_image.save(savePath + '\\' + pic_name)
                        pic_path = 'http://localhost:83/' + str(datetime.today().year) + '/' + str(datetime.today().month) + '/' + str(datetime.today().day) + '/' + pic_name
                        addLog(pic_path, self._signal._camid, '无人区', datetime.today())
                    print('person detected')

            else:
                print('skip this frame')
            frame = self._signal.get_frame()
            timer += 1
        print('no signal or deactivated by other caller')
        self.deactive()
        

    def deactive(self):
        self._isActive = False





