import datetime as time
global now
now = time.datetime.now()
hour = now.hour

if hour < 12:
    print("Good morning")
elif hour >= 12 and hour <= 18:
    global tim
    tim = 'Good afternoon'
    print("Good afternoon")         
elif hour > 18 and hour < 19: 
    print("Good evening")
else:
    print('Have a nice night.')

def name():
    global nam
    nam = input('please input your name: ')
    if nam == '' or nam == ' ':
        print('you have inputed nothing try again')
        name()
    else:
        print('''
        ''')
name()
def gender():
    global gend
    gend = input('''Are you:
    male(m)
    female(f)
    do not want to diclose(d)
    pls provide the replay here:''')
    global female
    female = 'lady'
    if gend == 'male' or gend == 'm':
        print('Thank you mr ',name)
    elif gend == 'female' or gend == 'f':
        print('Thank you lady ',name)
    elif gend == 'diclose' or gend == 'do not want to diclose'or gend == 'd':
        print('Thank you ',nam,'! We respect your right to not tell us')
    elif gend == ' ' or gend == '':
        print('you have inputed nothing try again')
        gender()
    elif gend != 'male' or con != 'lady':
        print('you have inputed the wrong thing try agin')
        gender()
    print(tim,' mr ',nam)
gender()