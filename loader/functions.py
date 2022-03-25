import json

def add_to_json(filename: str, post_to_add: dict):
    """Append a post to a json file

    Arguments:
    filename -- json file to add data to
    post_to_add - post to append to a json file
    """
    # Read file
    with open(filename, mode='r', encoding='utf-8') as file:
        posts = json.load(file)
    # Append data to the list
    posts.append(post_to_add)
    # Write file
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(posts, file, indent=4, ensure_ascii=False)

def is_filename_allowed(file: str, allowed_extensions: set)-> bool:
    """Check if the file has an extension which is allowed

    Arguments:
    filename -- file to check
    allowed_extenstions -- set with allowed extensions
    """
    file_extension = file.split(".")[-1]
    if file_extension in allowed_extensions:
        return True
    else:
        return False

if __name__ == '__main__':
    # test 1
    # filename = '../posts.json'
    # post_to_add = {"pic": "https://images.unsplash.com", "content": "Ага, "}
    # add_to_json(filename, post_to_add)
    # test 2
    print(is_filename_allowed('some.txt'))