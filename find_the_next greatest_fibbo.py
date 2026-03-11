goal = int(input("Enter a goal: "))         #Enter the goal input
a, b = 0, 1                                 #Initializing 0 & 1
if goal <= 0 :                              #If goal <= 0 just print 0
    print(0)
        
else:                                       #Prints fibbo which is just greater than or equal to given goal
    while True:
        a, b = b, a + b
        if(b >= goal):
            print(b)
            break
        



