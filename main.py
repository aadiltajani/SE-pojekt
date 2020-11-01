from Modules import signup
from Modules import authorize
from Modules import admin

# EmptyFieldException
class EmptyField(Exception):
    pass


# indicates if user has loggedin
loggedin = False
login_type = None

while True:

    if not loggedin:
        # Signup/Register
        print('\n_____________________________________________________________________________________________________')
        f = int(input('Signup/Login (0/1):'))
        if f not in [0, 1]:
            print('Enter Valid Choice !')
            continue

        # Login
        if f:
            try:
                user_id = input('\nEnter user ID: ').strip()
                pwd = input('Enter user Password: ').strip()

                # Check for empty fields
                if len(user_id) == 0 or len(pwd) == 0:
                    raise EmptyField

                # Check for admin
                if user_id == 'admin':
                    if not admin.authorize(pwd):
                        raise authorize.InvalidLoginDetails
                    else:
                        login_type = 'admin'
                        loggedin = True
                        print('\nLogin Successful. {} logged in'.format(user_id))
                else:
                    if not authorize.login(user_id, pwd):
                        raise authorize.InvalidLoginDetails
                    else:
                        loggedin = True
                        login_type = 'default'
                        print('\nLogin Successful. User {} logged in'.format(user_id))
            except EmptyField:
                print('\nPlease enter valid input !')
            except authorize.InvalidLoginDetails:
                print('\nLogin failed. Please try again.')

            except:
                pass

        # Signup
        else:
            try:
                user_id = input('\nEnter user ID: ').strip()
                pwd = input('Enter user Password: ').strip()

                # Check for empty fields
                if len(user_id) == 0 or len(pwd) == 0:
                    raise EmptyField

                if not signup.register(user_id, pwd):
                    raise signup.SignupFailed
                else:
                    loggedin = True
                    login_type = 'default'
                    print('\nSignup Successful. User {} logged in'.format(user_id))
            except EmptyField:
                print('\nPlease enter valid input !')
            except signup.SignupFailed:
                print('\nSignup failed. Please try again.')
            except:
                pass
    else:
        print('Welcome...')
        exit(0)
