from flask import Flask, request, render_template, send_from_directory
from main.main_views import main_blueprint
from loader.loader_views import loader_blueprint

# Initiate Flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# Route to display images from uploads
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
