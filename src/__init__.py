from flask import Flask, jsonify


def create_app(config=None):
    app = Flask(__name__)

    if config != None:
        app.config.from_object(config)

    @app.route('/heartbeat', methods=['GET'])
    def heartbeat():
        # TODO: Pass the version number dynamically? Maybe from the latest CHANGELOG?
        return jsonify({
            "status": "Ok",
        }), 200

    from .radio_amor import amor
    app.register_blueprint(amor)

    return app
