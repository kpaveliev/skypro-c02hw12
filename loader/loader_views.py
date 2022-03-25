from flask import request, render_template, Blueprint, send_from_directory
from loader.functions import add_to_json, is_filename_allowed
import logging
from settings import POST_PATH, UPLOAD_FOLDER, ALLOWED_EXTENSIONS

# Create Blueprint object and configure logging
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="basic.log", level=logging.INFO)


# Add views
@loader_blueprint.route('/post', methods=['GET', 'POST'])
def post_page():
    """Display form to add post or
       display added post when form is submitted
    """

    # Show form to add post
    if request.method == 'GET':
        return render_template('post_form.html')

    # Show added post
    elif request.method == 'POST':
        # Get data from submitted form
        picture = request.files.get('picture')
        content = request.form.get('content')

        # Check if picture is submitted
        if not picture:
            message = 'Не приложен файл с изображением'
            logging.error(message)
            return render_template('post_error.html', error_message=message)

        else:
            pic_name = picture.filename

            # Check if picture is an image
            if not is_filename_allowed(pic_name):
                message = f'Загружаемый файл {pic_name} не являетя изображением, ' \
                          f'допустимые разрешения: png, jpeg, jpg, gif'
                logging.info(message)
                return render_template('post_error.html', error_message=message)

            # If everything is okay
            else:
                pic_link = f'{UPLOAD_FOLDER}/{pic_name}'
                picture.save(pic_link)

                # Add new post to json file
                post_to_add = {'pic': pic_link, 'content': content}
                add_to_json(POST_PATH, post_to_add)

                # Display added post
                return render_template('post_uploaded.html',
                                       pic_link=pic_link,
                                       content=content)