import json
from settings import ALLOWED_EXTENSIONS

def add_to_json(filename, post_to_add):
    """Create list of posts from a json file"""

    with open(filename, mode='r', encoding='utf-8') as file:
        posts = json.load(file)

    posts.append(post_to_add)

    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(posts, file, indent=4, ensure_ascii=False)

def is_filename_allowed(filename):
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


if __name__ == '__main__':
    # test 1
    # filename = '../posts.json'
    # post_to_add = {"pic": "https://images.unsplash.com", "content": "Ага, "}
    # add_to_json(filename, post_to_add)
    # test 2
    print(is_filename_allowed('some.txt'))