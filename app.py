from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint

# Initiate Flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# Add a route to display images from uploads folder
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
