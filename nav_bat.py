"""Nav Batle by Pierre V. (p.vautherin@hotmail.com)"""
from time import sleep
from random import choice, randint

#the user has to guess this:
boat_position = [choice("ABCDE"), randint(1,5)]

#user can cheat
def cheat(x):
    if x == "Y":
        print
        print "Enemy position =  %s" % ( boat_position)
        print "(You cheetah  !)"
    else:
        print

#check if user guessed boat_position
def battle(user):
    if user[0] in "ABCDE" and type(user[0]) is str:
        if user[1] in range(6) and type(user[1]) is int :
            if user == boat_position:
                print "Well done, you shot enemy boat on %s" % (user)
            else:
                print "Fail !"
                print "... Can't win each time"
                print "Enemy boat position was %s" % (boat_position)
        else:
            print "Invalid format -- Number must be between 1 and 5"
    else:
        print "Invalid format -- Letter must be between A and E" 

#prints a 5x5 grid
def create_grid():
    result = []
    for i in range(1,6):
        for y in "ABCDE":
            result.append(str(i)+y)
        print result
        result=[]
    return result

#ASCII art is Art
print   "                       |"
sleep(0.5)
print   "                |    __-__"
sleep(0.5)
print   "              __-__ /  | ("
sleep(0.5)
print   "             /  | ((   | |"
print   "           /(   | ||___|_.  .|"
sleep(0.5)
print   "         .' |___|_|`---|-'.' ("

print   "    '-._/_| (   |\     |.'    \  "
sleep(0.5)
print   "        '-._|.-.|-.    |'-.____'."
print   "            |------------------'"
print   "             `----------------' "
print
sleep(1)
print "Welcome in Naval Battle 1.0 by Pierre!"

if raw_input("press ENTER to start") == "cheat":
    cheat("Y")
else:
    user=[]

print
print "... somewhere in these waters hids an hideous enemy boat"
print "Find it!!..."
sleep(1)
create_grid()

print
print


user_x = str((raw_input("Choose a letter (from A to E)  ")).upper())
user_y = int(raw_input("Choose a number (from 1 to 5)  "))
user.append(user_x)
user.append(user_y)
    
print
print "You choose %s" % (user)
print
battle(user)

    
    

