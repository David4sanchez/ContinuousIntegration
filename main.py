def valid():
 
    validOption=False
    n=0
    while(not validOption):
        try:
            n = int(input("Enter a whole number: "))
            validOption=True
        except ValueError:
            print('Error, please enter an integer')
     
    return n
 
leave = False
opcion = 0
print ("Welcome")
while not leave:
    
    print ("1. Encebollado  $1,50")
    print ("2. Casuela      $2,00")
    print ("3. Tigrillo     $3,00")
    print ("4. Salir")
     
    print ("Choose an option")
 
    opcion = valid()
 
    if opcion == 1:
        print ("How much?")
        amount = valid()
        print ("ok, anything else?")
    elif opcion == 2:
        print ("How much?")
        amount = valid()
        print ("ok, anything else?")
    elif opcion == 3:
        print ("How much?")
        amount = valid()
        print ("ok, anything else?")
    elif opcion == 4:
        leave = True
    else:
        print ("Enter a number between 1 and 3")
 
print ("Fin")