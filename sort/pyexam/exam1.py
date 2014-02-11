import sys



def Hello(name):
  if name == "Alice" or name == "Bryan":
    print "Alert:",name,"Mode"
    name = name + "?????"
  else:
    print "Else"

  name = name + "!!!!";
  print "Hello ", name



#Define the main function
def main():
  Hello(sys.argv[1])


#Boilerplate function that calls the main()
if __name__ == "__main__":
  main()

