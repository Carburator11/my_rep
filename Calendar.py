"""Calendar 1.0 by Pierre Vautherin (p.vautherin@hotmail.com
Built on 14-nov-2016)"""

from time import sleep, strftime

name = "Pierre"
calendar = {("hot dog",1),(23,"string")}

def welcome():
  print "welcome " + name
  print "Calendar opening..."
  sleep(1)
  print "today is " + strftime("%A %d %B %Y")
  print
  print "What would you like to do ?"
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to add, U to update, V to view, D to delete, X to exit ").upper()
    if user_choice == "V":
      if len(calendar.keys()) > 0:
        print calendar
      else:
        print "Calendar empty"
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
 

    elif user_choice == "X":
    	start = False    
    	break


start_calendar()

