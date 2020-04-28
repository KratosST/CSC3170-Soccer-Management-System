import os

from flask import Flask, render_template

from datetime import timedelta


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'photo.sqlite'),
    )
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import dashboard
    app.register_blueprint(dashboard.bp)
    app.add_url_rule('/', endpoint='index')

    from . import player
    app.register_blueprint(player.bp)

    from . import team_detail
    app.register_blueprint(team_detail.bp)

    from . import player_list
    app.register_blueprint(player_list.bp)

    from . import team_list
    app.register_blueprint(team_list.bp)

    from . import similar_player
    app.register_blueprint(similar_player.bp)

    return app
