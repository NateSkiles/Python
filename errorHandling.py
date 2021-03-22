
def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1, var2


def compute():
    go = True
    while go:
        var1, var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False # Set go to false, exit loop
        except ValueError as e:         # If there is a value error save that error to e
            print("{}: \n\nYou did not provde a numeric value!".format(e))    # diplay error 
        except:
            print("\n\nOops, you provided invalid input, program will close now!'") # Not a value error
    print("{} + {} = {}".format(var1, var2, var3))

  
##    finally:     The finally happens no matter what in a try/except block
##        print("Moving on...")


if __name__ == "__main__":
    compute()
