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
    """Display the form to add a new post and
       display the post after the form is submitted
    """
    # Show the form to add a post
    if request.method == 'GET':
        return render_template('post_form.html')

    # Show added post
    elif request.method == 'POST':
        # Get data from submitted form
        try:
            picture = request.files.get('picture')
            content = request.form.get('content')

            pic_name = picture.filename
            is_filename_allowed(pic_name, ALLOWED_EXTENSIONS)
            pic_link = f'{UPLOAD_FOLDER}/{pic_name}'
            picture.save(pic_link)

        # Show error if file isn't submitted or it's not an image
        except (TypeError, IsADirectoryError):
            message = f'Не приложен файл. ' \
                      f'Или загружаемый файл {pic_name} не являетcя изображением. \n' \
                      f'Допустимые разрешения: {", ".join(ALLOWED_EXTENSIONS)}'
            logging.error(message)
            return render_template('post_error.html', error_message=message)

        # Add the new post to a json file and display it
        else:
            post_to_add = {'pic': pic_link, 'content': content}
            add_to_json(POST_PATH, post_to_add)

            return render_template('post_uploaded.html', pic_link=pic_link, content=content)