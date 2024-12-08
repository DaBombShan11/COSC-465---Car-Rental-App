from flask import Flask

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = '12d32ud3-23dajehfgr-47593dskjfrlu-2099666-911-g0r0e0g'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')

    return app
