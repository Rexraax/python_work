# First Calculater
print("My own calculater")
print("Type 'quit' to exit\n")


run = True
def my_calculater():
    global run
    
    equation =input("Enter the Number: ")
    if equation == 'quit':
        run = False
        print("Goodbye. Human")
    else:
        
        previous =eval(equation)
    
        print( previous)
while run:
    my_calculater()

