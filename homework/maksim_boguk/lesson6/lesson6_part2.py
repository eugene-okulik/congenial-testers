for fuzbuz in range(1, 101):

    if (fuzbuz % 3 == 0) and (fuzbuz % 5 == 0):
        print('fuzzbuzz')
    elif fuzbuz % 3 == 0:
        print('Fuzz')
    elif fuzbuz % 5 == 0:
        print('Buzz')

    else:
        print(fuzbuz)