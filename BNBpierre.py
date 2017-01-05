name_1[rand"""Pierre-BnB by Pierre V. (p.vautherin@hotmail.com)
Built 4-nov-2016"""

from random import randint

name_1 = ["Lad's ", "Pimp ", "Bellevue ","Motorway ", "Golf ", "Elphiee's ", "Rapratuel ", "Cote de Beaune ", "Duc de Flandres ", "Allan's ", "Joe's ", "Murph's ", "Auto grill ", "Four star "]
name_2 = ["Inn", "Motel", "- Hotel de charme", "Guesthouse", "Station", "Inn", "Motel"]

number = 4  #change this value for more hotel choice
avail_hotel = {}



print "Welcome to Pierre BNB"
user_dest = raw_input("Please choose your destination =>")
print "Searching for hotels nearby %s" % (user_dest)

print
user_price = int(raw_input("What price per night? => "))
print "Searching for prices around %d" % (user_price)

print
if user_price <20:
    print "Sorry fellow, ain't nothing as cheap as $%d in the surroundings..." % (user_price)
    
elif user_price >500:
    print "Sorry rich kid, $%d ain't no normal price for a hotel room..." % (user_price)
    
else:
    for index in range(0, number):
        avail_hotel[index] = [name_1[randint(0,(len(name_1)-1))] + name_2[randint(0,(len(name_2)-1))],int(user_price +(user_price * randint(-15, 15)*0.01))]
        print avail_hotel[index]
    
print
user_choice = int(raw_input ("Select one the option (1 - %d) => " % (index+1)))
print "ok"
user_night = int(raw_input ("How many nights ? => "))
print "ok"

total = user_night * (avail_hotel[user_choice-1])[1]
total_tax_incl = 0.08*total + total

print "====================="
print "Booking details"
print
print "You chose %d nights at %s" % (user_night, (avail_hotel[user_choice-1])[0])
print " -- Price per night: %d$" % ((avail_hotel[user_choice-1])[1])
print "     x %d  = %d$ " % (user_choice, total)
print
print "---TOTAL (8%% VAT incl.) = %s" % (total_tax_incl)





    nt(0,(len(name_1)-1))] + name_2[randint(0,(len(name_2)-1))]