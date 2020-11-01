from PIL import Image
import pandas as pd


def show_tt():
    print('Showing time table...')
    img = Image.open('Resources/time_table.jpg')
    img.show()


def show_attendance(en):
    df = pd.read_csv('Resources/attendance.csv')
    roll = int(en)
    try:
        attendance = str(df[df['enrollment'] == roll].attendance.values[0])
        print('Attendance for enrollment number {} is {}%'.format(en, attendance))
    except:
        print('Student Not Found !')
