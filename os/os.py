import os

def writeData():
    data = '\nHello World!'
    with open('test.txt', 'a') as f:
        f.write(data)           # write() to test.txt what is in the variable data, close file
        f.close()

def openFile():
    with open('test.txt', 'r') as f:
        data = f.read()                     # while text.txt is open, read() out data in test.txt as f to variable data
        print(data)
        f.close()           # close our file when we are finished  using it



if __name__ == "__main__":
    writeData()
    openFile()
