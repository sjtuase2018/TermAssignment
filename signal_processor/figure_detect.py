from signal_processor import yolo_figure_detector
from PIL import Image


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
                if 'person' in classes_name:
                    r_image.show()
                    print('person detected')

            else:
                print('skip this frame')
            frame = self._signal.get_frame()
            timer += 1
        print('no signal or deactivated by other caller')
        self.deactive()

    def deactive(self):
        self._isActive = False
