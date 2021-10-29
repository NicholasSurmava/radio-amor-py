from src import create_app


# TODO: Breakout into own module, use ENV to determine the config to select
class Config(object):
    SECRET_KEY = "alksjddflk;j"


class DevelopmentConfig(Config):
    PORT = 5000
    ENV = 'development'
    DEBUG = True


if __name__ == "__main__":
    server = create_app(DevelopmentConfig)
    server.run()
