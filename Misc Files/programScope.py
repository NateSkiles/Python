name = 'Python'

def getName():
    name = 'C#'        # prints with name = 'C#' because of local scope --
    print("I am coding with {}".format(name))       #If you move print statment outside of the function,
                                                                        #name would = python because of global scope


getName()
