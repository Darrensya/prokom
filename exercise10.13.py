import json
from pathlib import Path


def get_stored_user_info(path):
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    return None


def get_new_user_info(path):
    user_info = {
        "username": input("Siapa namamu? "),
        "age": input("Berapa taun? "),
        "hobby": input("Hobinya apa? "),
    }
    path.write_text(json.dumps(user_info))
    return user_info


def remember_user():
    path = Path("user_info.json")

    user_info = get_stored_user_info(path)
    if user_info is None:
        user_info = get_new_user_info(path)
        print("Thanks! I'll remember that.")

    print("\nIni yang aku tau tentang kamu:")
    print(f"  Name: {user_info['username']}")
    print(f"  Age: {user_info['age']}")
    print(f"  Hobby: {user_info['hobby']}")


remember_user()