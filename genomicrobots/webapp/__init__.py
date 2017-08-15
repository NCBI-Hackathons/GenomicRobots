from flask import Flask, request
# from flask_seasurf import SeaSurf
from .controllers import pages


__all__ = ["create_app", ]

def create_app(conf):
    app = Flask(__name__)
    app.config.from_object(conf)
    app.register_blueprint(pages.web)
    # csrf = SeaSurf()
    # csrf.init_app(app)

    @app.after_request
    def log_response(resp):
        resp.headers["X-Frame-Options"] = "SAMEORIGIN"
        return resp

    return app
