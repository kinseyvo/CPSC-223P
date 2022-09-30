x = [1,2,3,4]
for i in range(0,3):
    try:
        if i == 0: 
            print(y)
        elif i == 1:
            5/0
        else:
            x[4]
       
#Multiple except blocks to handle Exceptions            
    except NameError:
        print("Variable not defined")
    except ZeroDivisionError:
        print("\nCannot divide by 0")
    except IndexError:
        print("\nIndex does not exist")

# After exception handling, execution continues
print("\nexecution continues")