import os


def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("Bad File!")
    infile = open(filename, "r")
    line = infile.readline()
    return line


try:
    line = readFromFile("example.txt")
    print(f"First line: {line}")
except Exception as e:
    print(e)
