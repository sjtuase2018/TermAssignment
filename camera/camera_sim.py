import cv2


class Camera(object):
    # def __init__(self):
    #    self.frames = [open('VideoFeeds/' + f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    # def get_frame(self):
    #    return self.frames[int(time()) % 3]

    def __init__(self, camid):
        self.video = cv2.VideoCapture('VideoFeeds/video' + camid + '.mpg')

    def __del__(self):
        self.video.release()




    def get_frame(self):
        success, image = self.video.read()
        if success:
            ret, jpeg = cv2.imencode('.jpg', image)  # Encode to JPEG
            if ret:
                return jpeg.tobytes()
            else:
                return None
        else:
            return None
