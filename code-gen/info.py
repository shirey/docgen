import os

def printdir(dir):
    print("---" + dir)
    print(os.listdir(dir))
print(os.getcwd())
printdir(os.getcwd())
printdir(".")
printdir("../")
printdir("../../")

#for k, v in sorted(os.environ.items()):
#    print(k+':', v)
#print('\n')
## list elements in path environment variable
#[print(item) for item in os.environ['PATH'].split(';')]
