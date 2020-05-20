import os.path
j = 0
for copies in range(200, 0, -1):
    if os.path.isfile('from_to_check (' + str(copies) + ').csv'):
        check = 0
        file = open('from_to_check (' + str(copies) + ').csv')

        a = file.readlines()
        b = []

        for i in range(1, len(a)):
            a[i] = a[i].replace('\n', '')
            b.append(a[i])

        for i in b:
            c = i.split(',')
            c[1] = int(c[1])
            if c[1] > 999:
                print("Sender " + c[0] + " sent " + str(c[1]) + " emails.")
                check = 1
        if check == 0:
            print('No match')
        file.close()
        j = 1
        break
if j == 0:
    check = 0
    file = open('from_to_check.csv', 'r')

    a = file.readlines()
    b = []

    for i in range(1, len(a)):
        a[i] = a[i].replace('\n', '')
        b.append(a[i])

    for i in b:
        c = i.split(',')
        c[1] = int(c[1])
        if c[1] > 999:
            print("Sender " + c[0] + " sent " + str(c[1]) + " emails.")
            check = 1
    if check == 0:
        print('No match')
        
    file.close()
