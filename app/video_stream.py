# from app import app
from app.url_mapping import api
from camera.camera_sim import Camera
from flask import Response


def gen(came):
    while True:
        frame = came.get_frame()
        if not frame is None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')
        else:
            break

#
# @app.route('/video_feed/<camid>')
# def video_feed(camid):
#     return Response(gen(Camera(camid)), mimetype='multipart/x-mixed-replace; boundary=frame')
#
#
# @app.route('/video_test')
# def video_test():
#     return render_template('video_feed.html')


@api.route('/video_feed/')
def video_feed():
    return Response(gen(Camera('1')), mimetype='multipart/x-mixed-replace; boundary=frame')
