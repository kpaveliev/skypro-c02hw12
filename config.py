class Config(object):
    DEBUG = False
    TESTING = False

    UPLOAD_FOLDER = './resources/uploads'
    POST_PATH = 'resources/files/posts.json'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class DevelopmentConfig(Config):
    DEBUG = True