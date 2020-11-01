import hashlib
import feedback


def authorize(pwd):
    pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()

    try:
        data = ''
        with open('Modules/admin.txt', 'r') as f:
            data = f.read()
        if data.strip() == pwd_hash:
            return True
        else:
            return False

    except FileNotFoundError:
        print('User not found !')
        return False


def driver():
    print('Welcome Admin.')
    feedback.read_feedbacks()