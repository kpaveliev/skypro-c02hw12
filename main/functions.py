import json

def load_from_json(filename: str)-> list:
    """Create a list of posts from a json file

    Arguments:
    filename -- path to a posts file
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts

def search_posts(searched_word: str, posts: list)-> list:
    """Search a word in posts and return all posts with it

    Arguments:
    searched_word -- a word to search for
    posts -- list of posts to search in
    """
    chars_to_remove = '#/,.!0-'
    posts_found = []

    for post in posts:
        words = post['content'].split(' ')
        words_cleaned = []

        # Prepare a list of words without chars_to_remove
        for word in words:
            for char in chars_to_remove:
                word = word.replace(char, '')
            words_cleaned.append(word.lower())

        # Search the word in words_cleaned list
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

