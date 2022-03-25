from flask import request, render_template, Blueprint, current_app
from loader.functions import add_to_json, is_filename_allowed
import logging

# Create Blueprint object and configure logging
loader_blueprint = Blueprint('loader_blueprint', __name__,
                             static_folder='static',
                             template_folder='templates')
logging.basicConfig(filename="resources/logs/basic.log", level=logging.ERROR)

# Add views
@loader_blueprint.route('/post', methods=['GET', 'POST'])
def post_page():
    """Display the form to add a new post and
       display the post after the form is submitted
    """
    # Show the form to add a post
    if request.method == 'GET':
        return render_template('post_form.html')

    # Show added post
    elif request.method == 'POST':
        try:
            # Get data from the submitted form
            picture = request.files.get('picture')
            content = request.form.get('content')
            pic_name = picture.filename

            # Check for errors
            if not picture:
                raise Exception
            if not is_filename_allowed(pic_name, current_app.config['ALLOWED_EXTENSIONS']):
                raise TypeError

        # Show errors
        except TypeError:
            message = f'Загружаемый файл {pic_name} не являетcя изображением. \n' \
                      f'Допустимые разрешения: {", ".join(current_app.config["ALLOWED_EXTENSIONS"])}'
            logging.error(message)
            return render_template('post_error.html', error_message=message)

        except Exception:
            message = f'Файл не загружен'
            logging.error(message)
            return render_template('post_error.html', error_message=message)

        # Work with the results if everything is okay
        else:
            # Save picture
            pic_link = f'{current_app.config["UPLOAD_FOLDER"]}/{pic_name}'
            picture.save(pic_link)

            # Add new post to the json file
            post_to_add = {'pic': pic_link, 'content': content}
            add_to_json(current_app.config['POST_PATH'], post_to_add)

            # Display page with the new post
            return render_template('post_uploaded.html', pic_link=pic_link, content=content)
