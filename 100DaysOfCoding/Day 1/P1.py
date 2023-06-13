cmd = input(">")
while(cmd.upper()=='HELP'):
    print('''
    start - to start the car
    stop - to stop the car
    quit - quit the game
    ''')
    ncmd = input(">")
    if(ncmd.upper()=='START'):
        print("Car Started....Ready to go")
    elif(ncmd.upper()=='STOP'):
        print("Car Stopped")
    elif(ncmd.upper()=='QUIT'):
        break
    else:
        print("I don't understand command")
        break
else:
    print("I don't understand that")