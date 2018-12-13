from app import app
# _pool
from multiprocessing import Pool

def model():
    from signal_processor.figure_detect import FigureCapturer
    from app.db_io import GetAreas
    from camera.camera_sim import Camera
    from app.url_mapping import api

    cams = [Camera(x) for x in GetAreas().keys()]
    print('all cams signal loaded')
    # bind figure_scanner to cam[0] by default
    figure_scanner = FigureCapturer(cams[0])
    figure_scanner.active()
#     # realTime
# @api.route('/modelSwitch/', methods=('POST','GET'))
# def modelSwitch():
#     x=2
#     print ("+1")
#     # f = _pool.apply_async(wanted_function, (x,))
#     # r = f.get(timeout=2)
#     # print (r)
#     print ("1")
#     # return 'Result is %d' % r
#     return jsonify({'code': 200})

if __name__ == "__main__":
    _pool = Pool(processes=4)
    # try:
        # insert production server deployment code
    _pool.apply_async(model)
        # model()  
    app.run()
    # except KeyboardInterrupt:
    _pool.close()
    _pool.join()
    # app.run(debug=True, processes=4)


