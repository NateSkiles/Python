

import dunderMethod


def print_app2():
    name = (__name__) # sets name = to a sting of the name of the file
    return name

# When you run a file, the file becomes dunder main. Meaing that if the files name..
# is __main__ the file is being executed.
if __name__ == "__main__":
    # Calling code from w/in this script
    print("I am running code from {}".format(print_app2()))

    # Calling code from imported dunderMethod.py
    print("I am running code from {} ".format(dunderMethod.print_app()))
