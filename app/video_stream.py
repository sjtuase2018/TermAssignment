from app import app
from camera.camera_sim import Camera
from flask import Response, render_template


def gen(came):
    while True:
        frame = came.get_frame()
        if frame:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            break


@app.route('/video_feed/<camid>')
def video_feed(camid):
    return Response(gen(Camera(camid)), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_test')
def video_test():
    return render_template('video_feed.html')

