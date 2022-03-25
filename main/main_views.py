from flask import request, render_template, Blueprint
from main.functions import load_from_json, search_posts
from settings import POST_PATH
import logging
from json import JSONDecodeError


# Create Blueprint object and configure logging
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="basic.log", level=logging.INFO)


# Add views
@main_blueprint.route('/')
def main_page():
    """Display main page with search form"""
    return render_template('index.html')


@main_blueprint.route('/search')
def main_search():
    """Display all posts with a specified word within"""

    try:
        posts = load_from_json(POST_PATH)

    except FileNotFoundError:
        message = 'Что-то пошло не так! Не обнаружен файл с постами.'
        logging.error(message)

        return render_template('main_error.html', error_message=message)

    except JSONDecodeError:
        message = 'Что-то пошло не так! Не удается обработать файл с постами.'
        logging.error(message)

        return render_template('main_error.html', error_message=message)

    else:
        searched_word = request.args.get('s')
        found_posts = search_posts(searched_word, posts)
        logging.info(f'Запрошен поиск по слову: {searched_word}')

        return render_template('main_list.html',
                               searched_word=searched_word,
                               posts=found_posts)
