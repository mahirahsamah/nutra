from flask import Flask

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='fwlebiuewfuiewfeif8y3289y dbf3r72ogr'

    from .nutrition import nutrition

    app.register_blueprint(nutrition, url_prefix='/')

    return app