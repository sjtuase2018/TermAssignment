import cv2


class Camera(object):
    # def __init__(self):
    #    self.frames = [open('VideoFeeds/' + f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    # def get_frame(self):
    #    return self.frames[int(time()) % 3]
    _camid = None

    def __init__(self, camid):
        self._camid = str(camid)
        self.video = cv2.VideoCapture('VideoFeeds/video' + str(camid) + '.mpg')

    def __del__(self):
        self.video.release()

    def get_camid(self):
        return self._camid

    def get_frame(self, formatter=None):
        success, image = self.video.read()
        if success:
            if formatter == "jpeg":
                _, jpeg = cv2.imencode('.jpg', image)  # Encode to JPEG
                return jpeg
            else:
                return image
        else:
            return None