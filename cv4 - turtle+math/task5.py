import turtle

def menu():
    a = input("Enter [ s ] or [ t ]: ")
    
    if a == "s":
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)
            
    elif a == "t":
        for i in range(3):
            turtle.forward(100)
            turtle.left(120)
    
    else:
        print("Incorrect input! Try again")
        menu();
        
menu()
turtle.mainloop()