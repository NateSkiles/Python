# Python Ver:   3.9.2
#
# Author:       Nathan Skiles
#
# Purpose:      The script should open this new html file in a new tab within your browser that displays:
#                   Stay tuned for our amazing summer sale! -- Added ability to take user input and create
#                   a webpage from their input.
#
# Tested OS:    This code was written & tested to work with Windows 10
import webbrowser


def htmlGene(x):
    f = open("SummerSale.html", "w")
    f.write(x)
    f.close()
    webbrowser.open("SummerSale.html")


# y = 'Stay tuned for our amazing summer sale!'
y = input('What would you like your HTML document to say?: \n>>>')
x = "<html><body><h1>" + y + "</h1></body></html> "

if __name__ == '__main__':
    htmlGene(x)
