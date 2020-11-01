def feedback():
    print("Welcome!")
    print("You can leave you feedbacks regarding the institute here.")
    print("NOTE:- All the details will remain anonymous")

    fb = input("write here:- ")
    fhand = open("Modules/feedback.txt", 'a')
    fhand.write(fb)
    fhand.write("\n")
    fhand.close()
    print("Your response has been recorded...Thank You!")
    ch = input("Press Enter to leave..")
    return


def read_feedbacks():
    print("Here are the latest feedbacks provided by the users - ")
    fhand = open("Modules/feedback.txt", 'r')
    data = fhand.read().strip().split("\n")
    fhand.close()
    data.reverse()
    nos = 1
    for x in data:
        print(nos, ") ", x)
        nos += 1
    ch = input("Press Enter to leave..")
    return