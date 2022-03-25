import json
from settings import POST_PATH

def load_from_json(filename):
    """Create list of posts from a json file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def search_posts(searched_word, posts):
    """Search a word in posts"""

    chars_to_remove = '#/,.!0-'
    posts_found = []

    for post in posts:
        words = post['content'].split(' ')
        words_cleaned = []

        # Prepare list of words without chars_to_remove
        for word in words:
            for char in chars_to_remove:
                word = word.replace(char, '')
            words_cleaned.append(word)

        # Search word in words_cleaned
        if searched_word.lower() in words_cleaned:
            posts_found.append(post)

    return posts_found

# Test functions
if __name__ == '__main__':
    posts = load_from_json(POST_PATH)
    print(posts)
    posts_found = search_posts('пирог', posts)
    print(posts_found)
    print(posts[0]['content'])

