from flask import Flask, send_from_directory
from flask import request
from Court_shixin.court_shixin import query_identity_info
import json, time, os
# from flask import logging
# from flask_logconfig import LogConfig
# from config.log_config import MyConfig


def creat_app():
    app = Flask(__name__)
    # app.config.from_object(MyConfig)
    # logcfg = LogConfig()
    # logcfg.init_app(app)
    # alogger = logging.getLogger("360_phone")
    # blogger = logging.getLogger("360_phone2")

    @app.route('/')
    def index():
        return 'hello'

    @app.route('/courtshixin', methods=['POST'])
    def index_phone():
        try:
            data = json.loads(request.get_data())
            p_name = data['pName']
            p_card_num = data['CID']
            p_province = '全部'
            q = query_identity_info()
            info = q.main(p_name=p_name, p_card_num=p_card_num, p_province=p_province)
            return json.dumps(info)
        except:
            return None


    @app.route('/user/<name>', methods=['GET', 'POST'])
    def user(name):
        return '<h1>hello,%s!</h1>' % name

    @app.errorhandler(404)
    def page_not_found(e):
        return 404

    @app.errorhandler(500)
    def interenal_server_error(e):
        return 500

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app


if __name__ == '__main__':
    application = creat_app()
    application.run(host='0.0.0.0')
