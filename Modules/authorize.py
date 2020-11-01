import hashlib


class InvalidLoginDetails(Exception):
    pass


def login(user_id, pwd):
    pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()

    try:
        li = []
        with open('Modules/credentials.txt', 'r') as f:
            li = f.readlines()
        for i in li:
            if i.strip().split(',')[0] == user_id:
                if i.strip().split(',')[1] == pwd_hash:
                    return True
                else:
                    return False
        print('User not found !')
        return False

    except FileNotFoundError:
        print('User not found !')
        return False
