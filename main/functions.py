import json

def load_from_json(filename: str)-> list:
    """Create a list of posts from a json file

    Arguments:
    filename -- path to a posts file
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


# Test functions
if __name__ == '__main__':
    posts = load_from_json(POST_PATH)
    print(posts)
    posts_found = search_posts('пирог', posts)
    print(posts_found)
    print(posts[0]['content'])

