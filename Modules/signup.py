import traceback
import hashlib


class SignupFailed(Exception):
    pass


def register(user_id, pwd):
    pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()
    flag = 1
    while True:
        try:
            li = []
            with open('Modules/credentials.txt', 'r') as f:
                li = f.readlines()
            for l in li:
                if user_id == l.strip().split(',')[0]:
                    flag = 0
                    break
            if flag:
                with open('Modules/credentials.txt', 'a') as f:
                    f.writelines('{},{}\n'.format(user_id, pwd_hash))
                return True
            else:
                print('This user_id is taken try another !')
                return False

        except FileNotFoundError:
            with open('Modules/credentials.txt', 'w') as f:
                f.writelines('{},{}\n'.format(user_id, pwd_hash))
            return True

        except:
            print('Some Error occured')
            traceback.print_exc()
            return False
