

print "Hello!"

age1 = float(raw_input("age du chat 1 ? (le plus jeune)"))
age2 = float(raw_input("age du chat 2 ?"))
conv = 0

if age2/2>age1 and age1<age2 and age1.is_integer() and age2.is_integer():
    while (age1 != (age2/2)):
        age1 = age1 +1
        age2 = age2 +1
        conv= conv+1
    print "Dans %d annees, chat 1 aura la moitie de l\'age de chat 2.\nChat 1 aura %d ans.\nChat 2 aura %d ans" % (conv, age1, age2)

else: print "***Pas de solution si les 2 ages sont trop proches!***\n***Donner l'age en nombre entier***\n***Chat 2 doit etre plus vieux que Chat 1***"


