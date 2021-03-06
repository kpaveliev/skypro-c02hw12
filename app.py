from flask import Flask, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint

# Key variables
UPLOAD_FOLDER = './resources/uploads'
POST_PATH = 'resources/files/posts.json'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Initiate Flask app
app = Flask(__name__, static_folder='resources/static')
app.config.from_object('config.DevelopmentConfig')

# Register blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# Add a route to display images from uploads folder
@app.route("/resources/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("resources/uploads", path)

if __name__ == '__main__':
    app.run()
