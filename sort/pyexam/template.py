import sys
import os

#Actual function
def List(dir):
  path = os.path.realpath(dir)
  print path

#Define the main function
def main():

#Call the function
List(sys.argv[1])

#Boilerplate function that calls the main()
if __name__ == "__main__":
  main()
