# from app import app
from app.url_mapping import api
from camera.camera_sim import Camera
from flask import Response


def gen(came):
    while True:
        frame = came.get_frame('jpeg')
        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')
        else:
            print('no signal')
            break
        

@api.route('/video_feed/')
def video_feed():
    return Response(gen(Camera('1')), mimetype='multipart/x-mixed-replace; boundary=frame')
